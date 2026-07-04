---
title: Glossary
status: draft          # draft | reviewed | approved
updated: YYYY-MM-DD
author: <BA name>
---

# Glossary

Living document — agreed definitions of domain terms. **A term used in any requirement must have an `agreed` row here.** Add terms as `proposed` the moment ambiguity surfaces in a session; get them to `agreed` with the stakeholders who use them.

| Term | Definition | Source | Status |
|---|---|---|---|
| Reset link *(example — delete)* | A single-use URL emailed to a registered address that permits setting a new password exactly once, within its validity window | TRN-001, FR-001 | agreed |
| Duplicate account *(example — delete)* | A second account created by an existing customer (same person/organisation), usually after a lockout; causes invoices to split across accounts | TRN-001 | agreed |
|  |  |  |  |

## Rules

- One term per row; if two departments define a word differently, record **both** definitions and flag the conflict for a decision (`../05-decision-log/`).
- Definitions describe the domain, not the implementation ("permits setting a new password once", not "row in password_resets table").
- Sort alphabetically once the table grows past a screenful.
