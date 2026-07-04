# 06 — Traceability

The traceability matrix (`traceability-matrix.md`) is the single place where the whole chain is visible:

```
Transcript → User Story → User Journey → Requirement (FR/NFR) → Design Brief section
```

It answers the two questions that kill projects when unanswerable:

1. **Forward**: "We heard this in a workshop — did it become a requirement, and where is it designed?"
2. **Backward**: "Why does this requirement exist — who asked for it, and what breaks if we cut it?"

## How to maintain it

The matrix is **generated from document frontmatter** — run:

```
python tools/reqs.py matrix
```

after creating any requirement or changing a document's `status`, `source`, or other reference fields. It can never drift from the documents, because the documents are the only input. (See `../tools/README.md` for details and for `check`, the validation-only variant.)

- Never edit between the `BEGIN/END GENERATED` markers — fix the source documents and regenerate.
- The chain is resolved transitively: an NFR that cites `applies_to: [FR-001]` inherits FR-001's transcripts, stories, and journeys.
- The `Design brief §` column fills itself once an assembled brief exists in `07-system-design-brief/` and mentions the requirement IDs.
- Orphans are findings, not formatting problems: a requirement with no source means elicitation or analysis is incomplete — `check` reports it as an error.
