# Requirements Documentation Template

A reusable structure for capturing requirements from first conversation through to a document ready for system design. Copy this whole folder into a new project and fill it in.

## Workflow

Documents flow in one direction — each stage is sourced from the one before it, and every document cites its sources by ID:

```
00-transcripts          Record elicitation conversations with stakeholders
      │
      ▼
01-user-stories         Distil transcripts into user stories
02-user-journeys        Map end-to-end journeys the stories live in
      │
      ▼
03-requirements         Derive functional & non-functional requirements
      │
      ▼
04-traceability         Tie transcripts → stories → journeys → requirements together
      │
      ▼
05-system-design-brief  Consolidate everything into one design-input document
```

## Folder Guide

| Folder | Contents | ID prefix |
|---|---|---|
| `00-transcripts/` | Records of BA ↔ stakeholder elicitation sessions | `TRN-###` |
| `01-user-stories/` | One file per user story | `US-###` |
| `02-user-journeys/` | One file per persona journey | `UJ-###` |
| `03-requirements/functional/` | One file per functional requirement | `FR-###` |
| `03-requirements/non-functional/` | One file per non-functional requirement | `NFR-###` |
| `04-traceability/` | The living traceability matrix | — |
| `05-system-design-brief/` | The consolidated design-input document | — |

## Conventions

### IDs
- Zero-padded three digits: `US-001`, `FR-012`.
- IDs are **never reused or renumbered**, even if a document is deprecated — other documents may reference them.
- Assign the next free number when creating a document.

### File naming
- `<ID>-short-kebab-title.md`, e.g. `US-001-password-reset.md`, `TRN-002-billing-workshop.md`.
- Files prefixed `TEMPLATE-` are blank templates: **copy, rename, fill in** — never edit the template itself except to improve the template for all future documents.

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

Type-specific fields (e.g. `priority`, `source`) are defined in each template.

### Priority (MoSCoW)
`must` | `should` | `could` | `wont` — applied to stories and requirements.

### Traceability
- Every user story cites the transcript(s) it came from.
- Every requirement cites the story/journey it supports.
- `04-traceability/traceability-matrix.md` holds the full chain — update it whenever a document is added or its status changes.

## Getting Started on a New Project

1. Copy this folder into the project and delete the worked examples inside each template.
2. Run elicitation sessions; record each one from `00-transcripts/TEMPLATE-transcript.md`.
3. Extract stories and journeys; derive requirements.
4. Keep the traceability matrix current as you go — it is much harder to reconstruct later.
5. When requirements stabilise, assemble the system design brief from `05-system-design-brief/TEMPLATE-system-design-brief.md`.
