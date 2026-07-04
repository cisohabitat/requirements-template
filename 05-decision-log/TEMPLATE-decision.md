---
id: DEC-000            # next free DEC number
title: <Short title — the decision, not the topic>
status: draft          # draft | reviewed | approved | superseded
date: YYYY-MM-DD
author: <BA name>
deciders: []           # people who made the call, e.g. [Maria Chen, Product Owner]
source: []             # evidence ids, e.g. [TRN-001]
affects: []            # document ids this decision changes, e.g. [FR-001, NFR-001]
supersedes:            # DEC id this replaces, if any
---

# DEC-000 — <Short title>

## Decision

<!-- One or two sentences, stated as a fact: "X will Y." -->

## Context & Evidence

<!-- The situation that forced a choice, citing transcripts/requirements by ID. -->

## Alternatives Rejected

<!-- The point of this document. One entry per alternative, with the real reason it lost. -->

| Alternative | Why rejected |
|---|---|
|  |  |

## Consequences

<!-- What this makes easier, what it makes harder, what it defers. Include the revisit trigger if temporary. -->

-

## Affected Documents

<!-- Every doc updated to reflect this decision. Update them in the same change. -->

- FR-0xx — <what changed>

---
---

# Worked Example (delete on real projects)

---
id: DEC-001
title: Email-only identity verification at launch
status: approved
date: 2026-06-22
author: Jane Analyst
deciders: [Maria Chen, Product Owner]
source: [TRN-001]
affects: [FR-001, NFR-001, US-001]
supersedes:
---

## Decision

Password-reset identity verification will use emailed single-use links only at launch; no SMS or authenticator-app channels.

## Context & Evidence

The TRN-001 follow-up established the platform has no SMS capability today. Adding an SMS provider would delay launch by an estimated quarter, while reset tickets cost ~65 agent-hours per month now.

## Alternatives Rejected

| Alternative | Why rejected |
|---|---|
| SMS verification codes | No existing SMS capability; procurement + integration delays launch a quarter for marginal security gain over email links |
| Security questions | Weak against research/guessing; industry practice has moved away from them |

## Consequences

- Launch is not blocked on a new vendor.
- Customers with compromised email are not protected by a second factor — accepted for launch given the portal exposes invoices, not payments.
- **Revisit trigger:** if the portal gains payment functionality, this decision must be superseded before that ships.

## Affected Documents

- FR-001 — constraint recorded under Dependencies & Constraints
- NFR-001 — latency target applies to the email channel only
- US-001 — assumption noted in Notes & Assumptions
