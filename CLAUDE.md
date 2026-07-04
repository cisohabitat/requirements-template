# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

A reusable requirements-engineering template — no application code. It is copied wholesale into new projects and filled in. Documents flow one way: transcripts (`00`) → user stories (`01`) & journeys (`02`) → requirements (`03`) → traceability matrix (`04`) → system design brief (`05`). Full conventions are in `README.md`; each folder's `README.md` covers its document type.

## Rules

- **`TEMPLATE-` files are masters.** Never fill one in. To create a document, copy the template, rename it `<ID>-short-kebab-title.md`, and fill in the copy. Only edit a template to improve it for all future documents.
- **IDs are permanent.** `TRN-`/`US-`/`UJ-`/`FR-`/`NFR-###`, zero-padded, assigned sequentially, never reused or renumbered — even for deprecated documents.
- **Preserve traceability.** Every document's frontmatter `source` field must cite upstream IDs. When creating or changing the status of an FR/NFR, update `04-traceability/traceability-matrix.md` in the same change.
- **Worked examples** at the bottom of each template (marked "delete on real projects") share one consistent scenario: TRN-001 → US-001 → UJ-001 → FR-001/NFR-001. If you edit an example, keep the IDs consistent across all templates and the matrix.
- **Requirements are atomic and testable.** One requirement per file; no "and" in the requirement sentence; quantify anything vague ("fast", "secure"). NFRs need a measurable target and verification method.
- **Frontmatter `status`** is the lifecycle: `draft | reviewed | approved | deprecated`. Don't delete documents — deprecate them.

## When asked to fill in the template for a project

1. Start from transcripts; write stories/journeys only from what transcripts support.
2. Assign the next free ID in each series (check existing files first).
3. Add a traceability matrix row the moment an FR/NFR is created.
4. Only assemble the design brief once `must`/`should` requirements are `approved` and the matrix coverage checks pass.
