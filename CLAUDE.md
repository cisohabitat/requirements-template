# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

A reusable requirements-engineering template — no application code. It is copied wholesale into new projects and filled in. Documents flow one way: project vision/stakeholders/glossary (`00`) → transcripts (`01`) → user stories (`02`) & journeys (`03`) → requirements (`04`) → traceability matrix (`06`) → system design brief (`07`), with significant decisions logged in `05-decision-log/` as they happen at any stage. Full conventions are in `README.md`; each folder's `README.md` covers its document type.

## Rules

- **`TEMPLATE-` files are masters.** Never fill one in. To create a document, copy the template, rename it `<ID>-short-kebab-title.md`, and fill in the copy. Only edit a template to improve it for all future documents. Exception: `00-project/` files and the traceability matrix are living documents, edited directly.
- **IDs are permanent.** `TRN-`/`US-`/`UJ-`/`FR-`/`NFR-`/`DEC-`/`STK-###`, zero-padded, assigned sequentially, never reused or renumbered — even for deprecated documents.
- **Preserve traceability.** Every document's frontmatter `source` field must cite upstream IDs. When creating or changing the status of an FR/NFR, update `06-traceability/traceability-matrix.md` in the same change.
- **Significant decisions get a DEC file.** Scope cuts, channel/platform choices, priority overrides, definition conflicts → `05-decision-log/`, created when the decision is made, with the affected documents updated in the same change. Decisions are superseded by new DECs, never edited after approval.
- **Glossary discipline.** A domain term used in any requirement must have an `agreed` row in `00-project/glossary.md`; add ambiguous terms as `proposed` the moment they surface.
- **Worked examples** at the bottom of each template and living doc (marked "delete on real projects") share one consistent scenario: STK-001 → TRN-001 → US-001 → UJ-001 → FR-001/NFR-001 → DEC-001. If you edit an example, keep the IDs consistent across all templates, the matrix, and the `00-project/` docs.
- **Requirements are atomic and testable.** One requirement per file; no "and" in the requirement sentence; quantify anything vague ("fast", "secure"). NFRs need a measurable target and verification method.
- **Frontmatter `status`** is the lifecycle: `draft | reviewed | approved | deprecated`. Don't delete documents — deprecate them.

## When asked to fill in the template for a project

1. Start from transcripts; write stories/journeys only from what transcripts support.
2. Assign the next free ID in each series (check existing files first).
3. Add a traceability matrix row the moment an FR/NFR is created.
4. Only assemble the design brief once `must`/`should` requirements are `approved` and the matrix coverage checks pass.
