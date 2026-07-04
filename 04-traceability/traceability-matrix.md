---
title: Traceability Matrix
status: draft          # draft | reviewed | approved
updated: YYYY-MM-DD
author: <BA name>
---

# Traceability Matrix

One row per requirement. Add the row when the requirement is created; keep `Status` in sync with the requirement's frontmatter. See `README.md` in this folder for maintenance rules.

| Requirement | Title | Source transcript(s) | User story(ies) | Journey(s) | Design brief § | Priority | Status |
|---|---|---|---|---|---|---|---|
| FR-001 *(example — delete)* | Self-service password reset | TRN-001 | US-001 | UJ-001 | §4.1 | must | approved |
| NFR-001 *(example — delete)* | Reset link delivery latency | TRN-001 | US-001 | UJ-001 | §5.1 | must | approved |
|  |  |  |  |  |  |  |  |

## Coverage Checks

Run through these before sign-off; record exceptions rather than deleting the question.

- [ ] Every transcript's "Candidate Requirements Spotted" table has each row either formalised (ID filled in) or explicitly rejected with a note.
- [ ] Every approved user story is covered by at least one requirement.
- [ ] Every requirement has at least one source — no orphans.
- [ ] Every `must` requirement is referenced in the system design brief.
