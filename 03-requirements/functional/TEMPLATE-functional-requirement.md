---
id: FR-000             # next free FR number
title: <Short title>
status: draft          # draft | reviewed | approved | deprecated
date: YYYY-MM-DD
author: <BA name>
priority: should       # must | should | could | wont  (MoSCoW)
source: []             # story/journey/transcript ids, e.g. [US-001, TRN-001]
depends_on: []         # other requirement ids this one depends on
---

# FR-000 — <Short title>

## Requirement

<!-- One sentence, "The system shall …". One requirement per file — no "and". -->

The system shall …

## Rationale

<!-- Why this exists. Cite the evidence (transcript/story) rather than restating it. -->

## Verification Criteria

<!-- How to prove it's met. Concrete and checkable — a tester should need no interpretation. -->

- [ ]
- [ ]

## Dependencies & Constraints

<!-- Other requirements, systems, or decisions this relies on. "None" is a valid answer. -->

-

---
---

# Worked Example (delete on real projects)

---
id: FR-001
title: Self-service password reset
status: approved
date: 2026-06-20
author: Jane Analyst
priority: must
source: [US-001, UJ-001, TRN-001]
depends_on: []
---

## Requirement

The system shall allow a registered user to reset their password via a single-use, time-limited link sent to their registered email address.

## Rationale

Manual resets are ~33% of support ticket volume at ~10 agent-minutes each (TRN-001), and the dead-end login flow drives duplicate-account creation (UJ-001, stage 2).

## Verification Criteria

- [ ] Submitting a registered email on the reset form delivers a reset link to that address.
- [ ] The link sets a new password once, then becomes invalid.
- [ ] The link expires 30 minutes after issue and shows an expiry message thereafter.
- [ ] Submitting an unregistered email shows the identical confirmation message and sends nothing (US-001 AC2).

## Dependencies & Constraints

- Requires transactional email capability (email-only at launch, per TRN-001 follow-up).
- Delivery latency governed by NFR-001.
