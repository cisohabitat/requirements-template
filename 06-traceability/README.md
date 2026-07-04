# 06 — Traceability

The traceability matrix (`traceability-matrix.md`) is the single place where the whole chain is visible:

```
Transcript → User Story → User Journey → Requirement (FR/NFR) → Design Brief section
```

It answers the two questions that kill projects when unanswerable:

1. **Forward**: "We heard this in a workshop — did it become a requirement, and where is it designed?"
2. **Backward**: "Why does this requirement exist — who asked for it, and what breaks if we cut it?"

## How to maintain it

- Add a row **when a requirement is created**, not at the end of the project — reconstruction after the fact is unreliable.
- One row per FR/NFR. A requirement sourced from several stories gets the stories listed in one cell.
- Update the `Status` column whenever the requirement's frontmatter `status` changes; update `Design brief §` once the system design brief is assembled.
- Orphans are findings, not formatting problems: a transcript takeaway with no story, or a requirement with no source, means elicitation or analysis is incomplete.

This is a **living document** — unlike the `TEMPLATE-` files, you edit `traceability-matrix.md` directly.
