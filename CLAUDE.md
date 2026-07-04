# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

A reusable requirements-engineering template — no application code. It is copied wholesale into new projects and filled in. Documents flow one way: project vision/stakeholders/glossary (`00`) → transcripts (`01`) → user stories (`02`) & journeys (`03`) → requirements (`04`) → traceability matrix (`06`) → system design brief (`07`), with significant decisions logged in `05-decision-log/` as they happen at any stage. Full conventions are in `README.md`; each folder's `README.md` covers its document type.

## Rules

- **Scaffold with the tool, not by hand.** Create documents with `python tools/reqs.py new <type> "<title>"` (types: transcript, story, journey, fr, nfr, decision) — it assigns the next free ID, strips the worked example, and fills the frontmatter. Never fill in a `TEMPLATE-` file; only edit one to improve it for all future documents. Exception: `00-project/` files are living documents, edited directly.
- **IDs are permanent.** `TRN-`/`US-`/`UJ-`/`FR-`/`NFR-`/`DEC-`/`STK-###`, zero-padded, assigned sequentially, never reused or renumbered — even for deprecated documents.
- **Preserve traceability.** Every document's frontmatter `source` field must cite upstream IDs. After creating or changing the status/references of any FR/NFR, run `python tools/reqs.py matrix` — the matrix is generated; never edit between its markers. Run `python tools/reqs.py check` before considering requirements work done; errors (broken refs, orphans) must be fixed.
- **Significant decisions get a DEC file.** Scope cuts, channel/platform choices, priority overrides, definition conflicts → `05-decision-log/`, created when the decision is made, with the affected documents updated in the same change. Decisions are superseded by new DECs, never edited after approval.
- **Glossary discipline.** A domain term used in any requirement must have an `agreed` row in `00-project/glossary.md`; add ambiguous terms as `proposed` the moment they surface.
- **Worked examples** at the bottom of each template and living doc (marked "delete on real projects") share one consistent scenario: STK-001 → TRN-001 → US-001 → UJ-001 → FR-001/NFR-001 → DEC-001. If you edit an example, keep the IDs consistent across all templates, the matrix, and the `00-project/` docs. When doing real project work while `*(example — delete)*` rows still exist in living docs, flag that the examples haven't been cleaned out and update/replace those rows rather than adding duplicates.
- **Requirements are atomic and testable.** One requirement per file; no "and" in the requirement sentence; quantify anything vague ("fast", "secure"). NFRs need a measurable target and verification method.
- **Frontmatter `status`** is the lifecycle: `draft | reviewed | approved | deprecated`. Don't delete documents — deprecate them.

## Skills

Prefer these skills (in `.claude/skills/`) over improvising the equivalent workflow:

| Task | Skill |
|---|---|
| Create any document (story, requirement, transcript, journey, decision) | `/new-doc` |
| Turn a transcript into draft stories and candidate NFRs | `/extract-stories` |
| Build or refresh the system design brief | `/assemble-brief` |
| Prepare questions and an agenda for an elicitation session | `/prep-session` |

All of them delegate ID assignment and scaffolding to `python tools/reqs.py` — never hand-assign IDs.

## When asked to fill in the template for a project

1. Start from transcripts; write stories/journeys only from what transcripts support.
2. Scaffold every document with `python tools/reqs.py new` so IDs stay sequential.
3. Run `python tools/reqs.py matrix` the moment an FR/NFR is created or changed.
4. Only assemble the design brief once `must`/`should` requirements are `approved` and the matrix coverage checks pass.
