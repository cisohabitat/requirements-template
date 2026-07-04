# Requirements Documentation Template

A reusable structure for capturing requirements from first conversation through to a document ready for system design. Copy this whole folder into a new project (or use GitHub's "Use this template") and fill it in.

## Workflow

Documents flow in one direction — each stage is sourced from the one before it, and every document cites its sources by ID:

```
00-project              Vision & scope, stakeholder register, glossary (living docs)
      │
      ▼
01-transcripts          Plan and record elicitation conversations with stakeholders
      │
      ▼
02-user-stories         Distil transcripts into user stories
03-user-journeys        Map end-to-end journeys the stories live in
      │
      ▼
04-requirements         Derive functional & non-functional requirements
05-decision-log         Record significant decisions as they happen (feeds every stage)
      │
      ▼
06-traceability         Tie transcripts → stories → journeys → requirements together
      │
      ▼
07-system-design-brief  Consolidate everything into one design-input document
```

## Folder Guide

| Folder | Contents | ID prefix |
|---|---|---|
| `00-project/` | Vision & scope, stakeholder register, glossary — living docs, edited directly | `STK-###` (register rows) |
| `01-transcripts/` | Records of elicitation sessions, plus session-planning aids in `elicitation-aids/` | `TRN-###` |
| `02-user-stories/` | One file per user story | `US-###` |
| `03-user-journeys/` | One file per persona journey | `UJ-###` |
| `04-requirements/functional/` | One file per functional requirement | `FR-###` |
| `04-requirements/non-functional/` | One file per non-functional requirement | `NFR-###` |
| `05-decision-log/` | One file per significant requirements decision | `DEC-###` |
| `06-traceability/` | The living traceability matrix | — |
| `07-system-design-brief/` | The consolidated design-input document | — |

## Conventions

### IDs
- Zero-padded three digits: `US-001`, `FR-012`, `DEC-003`.
- IDs are **never reused or renumbered**, even if a document is deprecated — other documents may reference them.
- Assign the next free number when creating a document.

### File naming
- `<ID>-short-kebab-title.md`, e.g. `US-001-password-reset.md`, `DEC-001-email-only-verification.md`.
- Files prefixed `TEMPLATE-` are blank templates: **copy, rename, fill in** — never edit the template itself except to improve the template for all future documents.
- `00-project/` files and the traceability matrix are **living documents** — edited directly, no copies.

### Frontmatter
Every document starts with YAML frontmatter. Common fields:

```yaml
---
id: US-001
title: Password reset
status: draft        # draft | reviewed | approved | deprecated
date: 2026-07-04
author: Jane Analyst
---
```

Type-specific fields (e.g. `priority`, `source`, `deciders`) are defined in each template.

### Priority (MoSCoW)
`must` | `should` | `could` | `wont` — applied to stories and requirements.

### Traceability
- Every user story cites the transcript(s) it came from.
- Every requirement cites the story/journey it supports.
- Decisions cite their evidence and list the documents they affect.
- `06-traceability/traceability-matrix.md` holds the full chain — **generated** from frontmatter by `python tools/reqs.py matrix`; rerun it whenever a document is added or its status changes.

## Tooling

`tools/reqs.py` (Python 3.9+, no packages needed) does the mechanical work — see `tools/README.md`:

```
python tools/reqs.py new story "Password reset"   # scaffold with the next free ID
python tools/reqs.py matrix                       # regenerate the traceability matrix
python tools/reqs.py check                        # validate IDs, references, coverage
```

## Getting Started on a New Project

1. Copy this folder into the project and delete the worked examples inside each template and living doc.
2. Draft `00-project/vision-and-scope.md` and seed the stakeholder register — even a rough version steers elicitation.
3. Plan each session with `01-transcripts/elicitation-aids/TEMPLATE-session-plan.md` (the question bank is there too); record it from `01-transcripts/TEMPLATE-transcript.md`.
4. Extract stories and journeys; derive requirements; log significant decisions in `05-decision-log/` as they happen.
5. Run `python tools/reqs.py matrix` after every requirement change so the traceability matrix stays current.
6. When requirements stabilise, assemble the system design brief from `07-system-design-brief/TEMPLATE-system-design-brief.md`.
