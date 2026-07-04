---
name: new-doc
description: Scaffold a new requirements document (transcript, story, journey, fr, nfr, or decision) with the next free ID, then guide filling it in. Use when the user asks to create/add a user story, requirement, transcript, journey, or decision record.
---

# Scaffold a requirements document

## Steps

1. Determine the document type and title. Types map to `tools/reqs.py new` types:
   - elicitation session record → `transcript`
   - user story → `story`; user journey → `journey`
   - functional requirement → `fr`; non-functional requirement → `nfr`
   - decision record → `decision`

   If the user gave neither type nor title, ask. Titles are short and content-bearing ("Password reset", not "New story").

2. Run the scaffolder from the repo root:

   ```
   python tools/reqs.py new <type> "<title>"
   ```

   It prints the new file's path. Never create the file by hand or copy a `TEMPLATE-` file manually — the tool owns ID assignment.

3. Open the new file and fill it in with the user, section by section. Rules that matter:
   - `source` must cite real upstream IDs (transcripts for stories; stories/journeys for requirements). If no source exists yet, say so — an unsourced requirement is an error the tooling will flag.
   - Requirements: one atomic "The system shall…" sentence, no "and"; quantify anything vague. NFRs need a measurable target and verification method.
   - Domain terms used in requirements must exist in `00-project/glossary.md` as `agreed` — add missing ones as `proposed`.
   - Leave `status: draft`; humans promote status after review.
   - If `author` scaffolded as `<BA name>` (no `git config user.name`), fill in the actual analyst's name — ask if unknown.

4. If an FR/NFR was created or any references changed, finish with:

   ```
   python tools/reqs.py matrix
   ```

   and report any errors/warnings it prints.
