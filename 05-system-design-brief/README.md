# 05 — System Design Brief

The consolidation point: one document that pulls the transcripts, stories, journeys, requirements, and traceability together into the **input for system design**. An architect or design team should be able to work from this document alone, following ID references back to source files only when they need depth.

## When to create it

Once requirements have stabilised — typically when all `must` and `should` requirements are `approved` and the traceability matrix coverage checks pass.

## Naming

Copy `TEMPLATE-system-design-brief.md` to `<project-name>-design-brief.md` and fill it in. One brief per system (or per major release, if scope shifts substantially).

## Principles

- **Reference, don't duplicate.** Summarise requirements in tables of IDs and one-line titles; the detail lives in `03-requirements/`. Duplicated text goes stale.
- **Include the negative space.** Out-of-scope decisions and open questions are as valuable to a designer as the requirements themselves.
- **It's a snapshot.** Stamp the date and the matrix version it was assembled from; regenerate rather than patch if requirements move underneath it.
