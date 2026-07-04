#!/usr/bin/env python3
"""Requirements repo tooling: scaffold documents, generate the traceability
matrix, and validate cross-references.

Zero dependencies (standard library only). Frontmatter must stay simple:
`key: value` scalars and inline `[a, b]` lists, one per line.

Usage:
    python tools/reqs.py new <type> "<title>"    types: transcript | story |
                                                 journey | fr | nfr | decision
    python tools/reqs.py matrix                  regenerate traceability matrix
    python tools/reqs.py check                   validate, exit 1 on errors
"""

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# type -> (folder, id prefix, template filename)
TYPES = {
    "transcript": ("01-transcripts", "TRN", "TEMPLATE-transcript.md"),
    "story": ("02-user-stories", "US", "TEMPLATE-user-story.md"),
    "journey": ("03-user-journeys", "UJ", "TEMPLATE-user-journey.md"),
    "fr": ("04-requirements/functional", "FR", "TEMPLATE-functional-requirement.md"),
    "nfr": ("04-requirements/non-functional", "NFR", "TEMPLATE-non-functional-requirement.md"),
    "decision": ("05-decision-log", "DEC", "TEMPLATE-decision.md"),
}

MATRIX_FILE = ROOT / "06-traceability" / "traceability-matrix.md"
BRIEF_DIR = ROOT / "07-system-design-brief"
BEGIN_MARK = "<!-- BEGIN GENERATED -->"
END_MARK = "<!-- END GENERATED -->"

ID_RE = re.compile(r"^(TRN|US|UJ|FR|NFR|DEC)-(\d{3,})$")
FILE_RE = re.compile(r"^(TRN|US|UJ|FR|NFR|DEC)-(\d{3,})-.*\.md$")
REF_FIELDS = ("source", "journeys", "applies_to", "affects", "stories", "depends_on")
VALID_STATUS = {"draft", "reviewed", "approved", "deprecated", "superseded"}
VALID_PRIORITY = {"must", "should", "could", "wont"}
WORKED_EXAMPLE_SEP = "\n---\n---\n"


# ---------------------------------------------------------------- frontmatter

def read_text(path):
    """Read tolerating a UTF-8 BOM and CRLF line endings (both common on Windows)."""
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def parse_frontmatter(text):
    """Return (fields dict, raw frontmatter lines, body) or (None, None, text)."""
    if not text.startswith("---\n"):
        return None, None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, None, text
    raw = text[4:end]
    body = text[end + 5:]
    fields = {}
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not m:
            continue  # list items / blank / nested lines are ignored
        key, value = m.group(1), m.group(2)
        value = re.sub(r"\s+#.*$", "", value).strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            fields[key] = [v.strip() for v in inner.split(",") if v.strip()] if inner else []
        else:
            fields[key] = value.strip("'\"") or None
    return fields, raw, body


def refs_of(fields):
    """All document IDs cited by a document's reference fields."""
    out = []
    for f in REF_FIELDS:
        v = fields.get(f)
        if isinstance(v, list):
            out.extend(x for x in v if ID_RE.match(x))
        elif isinstance(v, str) and ID_RE.match(v):
            out.append(v)
    return out


# ------------------------------------------------------------------- scanning

def scan_docs():
    """Return ({id: {fields, path}}, [problems]) for all real (non-template) docs."""
    docs, problems = {}, []
    for folder, _prefix, _tmpl in TYPES.values():
        d = ROOT / folder
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            m = FILE_RE.match(p.name)
            if not m:
                continue
            fields, _raw, _body = parse_frontmatter(read_text(p))
            rel = p.relative_to(ROOT).as_posix()
            if fields is None:
                problems.append(f"ERROR {rel}: missing or malformed frontmatter")
                continue
            doc_id = fields.get("id")
            expected = f"{m.group(1)}-{m.group(2)}"
            if doc_id != expected:
                problems.append(f"ERROR {rel}: frontmatter id '{doc_id}' does not match filename ({expected})")
                doc_id = expected
            if doc_id in docs:
                problems.append(f"ERROR {rel}: duplicate id {doc_id} (also in {docs[doc_id]['path']})")
                continue
            for field, valid in (("status", VALID_STATUS), ("priority", VALID_PRIORITY)):
                v = fields.get(field)
                if field == "status" and not v:
                    problems.append(f"ERROR {rel}: missing status")
                elif v and v not in valid:
                    problems.append(f"ERROR {rel}: invalid {field} '{v}'")
            if not fields.get("title"):
                problems.append(f"ERROR {rel}: missing title")
            docs[doc_id] = {"fields": fields, "path": rel}
    return docs, problems


def resolve_chain(req_id, docs):
    """Follow a requirement's references upstream; return (trns, uss, ujs) id sets."""
    trns, uss, ujs = set(), set(), set()
    seen = set()
    frontier = list(refs_of(docs[req_id]["fields"]))
    while frontier:
        rid = frontier.pop()
        if rid in seen or rid == req_id:
            continue
        seen.add(rid)
        prefix = rid.split("-")[0]
        if prefix == "TRN":
            trns.add(rid)
        elif prefix == "UJ":
            ujs.add(rid)
        elif prefix in ("US", "FR", "NFR"):
            if prefix == "US":
                uss.add(rid)
            if rid in docs:
                frontier.extend(refs_of(docs[rid]["fields"]))
    return trns, uss, ujs


def brief_sections():
    """Map document id -> section number (e.g. '§4.1') in the assembled design brief."""
    briefs = [p for p in BRIEF_DIR.glob("*.md")
              if p.name != "README.md" and not p.name.startswith("TEMPLATE-")]
    sections = {}
    for brief in briefs:
        current = None
        for line in read_text(brief).splitlines():
            h = re.match(r"^#{2,3}\s+(\d+(?:\.\d+)?)[\s.]", line)
            if h:
                current = h.group(1)
                continue
            for rid in re.findall(r"\b(?:TRN|US|UJ|FR|NFR|DEC)-\d{3,}\b", line):
                if current and rid not in sections:
                    sections[rid] = f"§{current}"
    return sections, bool(briefs)


# ----------------------------------------------------------------- validation

def validate(docs, problems):
    """Extend problems with cross-reference findings; return (errors, warnings)."""
    for doc_id, doc in sorted(docs.items()):
        for rid in refs_of(doc["fields"]):
            if rid not in docs:
                problems.append(f"ERROR {doc['path']}: {doc_id} cites {rid}, but no such document exists")
    reqs = {i: d for i, d in docs.items() if i.startswith(("FR-", "NFR-"))}
    for req_id, doc in sorted(reqs.items()):
        if not refs_of(doc["fields"]):
            problems.append(f"ERROR {doc['path']}: {req_id} is orphaned (no source references)")
    covered = set()
    for req_id in reqs:
        _t, uss, _j = resolve_chain(req_id, docs)
        covered |= uss
    for us_id, doc in sorted(docs.items()):
        if us_id.startswith("US-") and us_id not in covered and doc["fields"].get("status") != "deprecated":
            problems.append(f"WARN  {doc['path']}: {us_id} has no covering requirement")
    sections, brief_exists = brief_sections()
    if brief_exists:
        for req_id, doc in sorted(reqs.items()):
            if doc["fields"].get("priority") == "must" and req_id not in sections:
                problems.append(f"WARN  {doc['path']}: must-priority {req_id} is not referenced in the design brief")
    errors = [p for p in problems if p.startswith("ERROR")]
    warnings = [p for p in problems if p.startswith("WARN")]
    return errors, warnings


# --------------------------------------------------------------------- matrix

def build_matrix_table(docs):
    sections, _ = brief_sections()
    header = ("| Requirement | Title | Source transcript(s) | User story(ies) "
              "| Journey(s) | Design brief § | Priority | Status |\n"
              "|---|---|---|---|---|---|---|---|")
    req_ids = sorted((i for i in docs if i.startswith(("FR-", "NFR-"))),
                     key=lambda i: (i.split("-")[0], int(i.split("-")[1])))
    if not req_ids:
        return header + "\n| *(no requirements yet)* |  |  |  |  |  |  |  |"
    rows = []
    for rid in req_ids:
        f = docs[rid]["fields"]
        trns, uss, ujs = resolve_chain(rid, docs)
        cell = lambda ids: ", ".join(sorted(ids)) or "—"
        rows.append(f"| {rid} | {f.get('title') or '—'} | {cell(trns)} | {cell(uss)} | {cell(ujs)} "
                    f"| {sections.get(rid, '—')} | {f.get('priority') or '—'} | {f.get('status') or '—'} |")
    return header + "\n" + "\n".join(rows)


def cmd_matrix():
    docs, problems = scan_docs()
    text = read_text(MATRIX_FILE)
    begin, end = text.find(BEGIN_MARK), text.find(END_MARK)
    if begin == -1 or end == -1 or end < begin:
        sys.exit(f"error: {BEGIN_MARK} / {END_MARK} markers not found in {MATRIX_FILE}")
    table = build_matrix_table(docs)
    new_text = text[:begin + len(BEGIN_MARK)] + "\n" + table + "\n" + text[end:]
    today = datetime.date.today().isoformat()
    new_text = re.sub(r"^updated:.*$", f"updated: {today}", new_text, count=1, flags=re.M)
    MATRIX_FILE.write_text(new_text, encoding="utf-8")
    n = sum(1 for i in docs if i.startswith(("FR-", "NFR-")))
    print(f"regenerated {MATRIX_FILE.relative_to(ROOT).as_posix()} ({n} requirement(s))")
    report(*validate(docs, problems))


def cmd_check():
    docs, problems = scan_docs()
    errors, warnings = validate(docs, problems)
    report(errors, warnings)
    print(f"checked {len(docs)} document(s): {len(errors)} error(s), {len(warnings)} warning(s)")
    if errors:
        sys.exit(1)


def report(errors, warnings):
    for line in errors + warnings:
        print(line)


# ------------------------------------------------------------------- scaffold

def git_user():
    try:
        name = subprocess.run(["git", "config", "user.name"], capture_output=True,
                              text=True, cwd=ROOT).stdout.strip()
        return name or "<BA name>"
    except OSError:
        return "<BA name>"


def cmd_new(doc_type, title):
    folder, prefix, template = TYPES[doc_type]
    d = ROOT / folder
    highest = 0
    for p in d.glob(f"{prefix}-*.md"):
        m = FILE_RE.match(p.name)
        if m:
            highest = max(highest, int(m.group(2)))
    doc_id = f"{prefix}-{highest + 1:03d}"

    text = read_text(d / template)
    fields, raw, body = parse_frontmatter(text)
    if fields is None:
        sys.exit(f"error: template {template} has no frontmatter")

    # Strip the worked example, then retitle the H1.
    sep = body.find(WORKED_EXAMPLE_SEP)
    if sep != -1:
        body = body[:sep]
    body = re.sub(rf"^# {prefix}-000\b.*$", f"# {doc_id} — {title}", body, count=1, flags=re.M)

    # Substitute known keys line-wise so guidance comments on other keys survive.
    subs = {
        "id": doc_id,
        "title": title,
        "date": datetime.date.today().isoformat(),
        "author": git_user(),
    }
    fm_lines = []
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):", line)
        if m and m.group(1) in subs:
            fm_lines.append(f"{m.group(1)}: {subs[m.group(1)]}")
        else:
            fm_lines.append(line)

    kebab = re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", title.lower())).strip("-")
    out = d / f"{doc_id}-{kebab}.md"
    if out.exists():
        sys.exit(f"error: {out} already exists")
    out.write_text("---\n" + "\n".join(fm_lines) + "\n---\n" + body.rstrip() + "\n",
                   encoding="utf-8")
    print(out.relative_to(ROOT).as_posix())


# ------------------------------------------------------------------------ cli

def main():
    parser = argparse.ArgumentParser(prog="reqs.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p_new = sub.add_parser("new", help="scaffold a document from its template")
    p_new.add_argument("type", choices=sorted(TYPES))
    p_new.add_argument("title", help='document title, e.g. "Password reset"')
    sub.add_parser("matrix", help="regenerate the traceability matrix")
    sub.add_parser("check", help="validate documents and references; exit 1 on errors")
    args = parser.parse_args()
    if args.command == "new":
        cmd_new(args.type, args.title)
    elif args.command == "matrix":
        cmd_matrix()
    else:
        cmd_check()


if __name__ == "__main__":
    main()
