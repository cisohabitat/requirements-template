# 00 — Project

Project-level **living documents**: created once when the project starts, then edited directly as understanding grows (no `TEMPLATE-` copies here, and no per-document IDs except stakeholder rows).

| File | Purpose | ID prefix |
|---|---|---|
| `vision-and-scope.md` | The north star: objectives, success metrics, project-level in/out of scope | — |
| `stakeholder-register.md` | Who was/should be consulted, their influence, and which sessions they attended | `STK-###` (rows) |
| `glossary.md` | Agreed definitions of domain terms | — |

## Why this folder exists

- **Vision & scope** keeps every downstream document honest — a story or requirement that doesn't serve a stated objective needs a reason to exist. It feeds §1 of the system design brief.
- **The stakeholder register** links transcripts to people: coverage gaps ("we never spoke to billing") become visible, and journeys/stories can cite personas backed by real stakeholders.
- **The glossary** kills the most common requirements defect: two stakeholders using the same word for different things. If a term is used in a requirement, it must be defined here first.

## Maintenance

- Update these documents after each elicitation session — new stakeholders, new terms, refined scope.
- Scope changes are significant decisions: record them in `../05-decision-log/` and link the DEC ID from `vision-and-scope.md`.
