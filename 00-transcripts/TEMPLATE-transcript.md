---
id: TRN-000            # next free TRN number
title: <Session topic>
status: draft          # draft | reviewed | approved | deprecated
date: YYYY-MM-DD
author: <BA name>
session_type: interview   # interview | workshop | demo-feedback | other
participants:
  - name: <Name>
    role: <Role / department>
  - name: <Name>
    role: <Role / department>
---

# TRN-000 — <Session topic>

## Session Goals

<!-- What you set out to learn in this session. 2–4 bullets. -->

-
-

## Transcript

<!-- The conversation record. Verbatim where it matters, summarised where it doesn't.
     Use "Q:" for the analyst and the speaker's initials for answers. -->

**Q:**

**XX:**

## Key Takeaways

<!-- Your conclusions — keep clearly separate from what was literally said. -->

-
-

## Candidate Requirements Spotted

<!-- Half-formed is fine; these get formalised later. Note who raised each one. -->

| # | Candidate requirement | Raised by | Formalised as |
|---|---|---|---|
| 1 |  |  | *(US/FR/NFR id once created)* |

## Open Questions / Follow-ups

| Question | Owner | Due | Resolved? |
|---|---|---|---|
|  |  |  |  |

---
---

# Worked Example (delete on real projects)

---
id: TRN-001
title: Account access interview — support team lead
status: reviewed
date: 2026-06-15
author: Jane Analyst
session_type: interview
participants:
  - name: Maria Chen
    role: Customer Support Team Lead
---

## Session Goals

- Understand the volume and causes of account-access support tickets.
- Identify what users try before contacting support.

## Transcript

**Q:** What proportion of your tickets relate to account access?

**MC:** Roughly a third. The biggest single category is forgotten passwords — we reset them manually, which takes an agent about ten minutes per ticket including identity checks.

**Q:** What do users try before raising a ticket?

**MC:** Nothing — there's nothing they *can* try. There's no self-service reset. Some create duplicate accounts instead, which causes billing confusion later.

## Key Takeaways

- Manual password resets are the single largest ticket category (~33% of volume).
- Absence of self-service reset causes duplicate accounts, a secondary data-quality problem.

## Candidate Requirements Spotted

| # | Candidate requirement | Raised by | Formalised as |
|---|---|---|---|
| 1 | Users should be able to reset their own password without contacting support | Maria Chen | US-001, FR-001 |
| 2 | Reset must verify identity at least as strongly as the manual process | Maria Chen | NFR-001 |

## Open Questions / Follow-ups

| Question | Owner | Due | Resolved? |
|---|---|---|---|
| Do we have SMS capability for verification codes, or email only? | Jane Analyst | 2026-06-22 | Yes — email only at launch |
