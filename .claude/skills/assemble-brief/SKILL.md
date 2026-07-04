---
name: assemble-brief
description: Assemble the system design brief from approved stories, journeys, requirements, and decisions. Use when the user asks to build, generate, or update the design brief / design-input document.
---

# Assemble the system design brief

## Preconditions — check first, stop and report if not met

1. Run `python tools/reqs.py check`. Errors must be fixed before assembling; warnings about coverage should be listed to the user with a recommendation.
2. Every `must` and `should` FR/NFR should be `status: approved`. If some aren't, list them and ask whether to proceed (the brief will be marked `draft` regardless).

## Steps

1. Create the brief by copying `07-system-design-brief/TEMPLATE-system-design-brief.md` to `07-system-design-brief/<project-name>-design-brief.md` (kebab-case project name; ask if unclear). Delete the worked example. This is the one document type not scaffolded by `reqs.py`.

2. Fill each section **from frontmatter and existing documents only — reference IDs, never duplicate body text**:
   - §1 Executive summary: condense `00-project/vision-and-scope.md` (problem, objectives, solution shape).
   - §2 Personas & journeys: one row per UJ document.
   - §3 Stories: every non-deprecated US, sorted by priority then ID.
   - §4 Functional requirements: group FRs into `### 4.x <capability area>` subsections by affinity — the traceability matrix's § column keys off these numbers.
   - §5 Non-functional requirements: group by `category`; the Target column comes from each NFR's Target & Metric table.
   - §6 Constraints & assumptions: harvest from vision/scope, DEC consequences, and requirement constraint sections, each with its source ID.
   - §7 Out of scope: from vision-and-scope plus any DEC that cut scope.
   - §8 Open questions: unresolved rows from all transcripts' Open Questions tables, plus DEC revisit triggers.

3. Stamp frontmatter: `status: draft`, today's date, `assembled_from: traceability-matrix.md as of <today>`.

4. Run `python tools/reqs.py matrix` — the § column should now populate. If any `must` requirement still warns as unreferenced, the brief is missing it: fix the brief, not the warning.

5. Report to the user: file path, counts per section, requirements that weren't `approved`, and all §8 open questions (those need answers before design starts).
