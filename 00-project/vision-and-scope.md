---
title: <Project name> — Vision & Scope
status: draft          # draft | reviewed | approved
updated: YYYY-MM-DD
author: <BA name>
---

# <Project name> — Vision & Scope

<!-- Living document: edit directly, keep it short (1–2 pages). Update after each session that shifts understanding. -->

## Problem Statement

<!-- The pain in one paragraph, with evidence (TRN refs). Why now? -->

## Business Objectives & Success Metrics

<!-- Objectives are outcomes, not features. Every metric needs a baseline and a target. -->

| # | Objective | Metric | Baseline | Target |
|---|---|---|---|---|
| 1 |  |  |  |  |

## In Scope

-

## Out of Scope

<!-- Explicit exclusions, each with the decision that excluded it (DEC ref) where one exists. -->

-

## Key Stakeholders

<!-- Summary only — detail lives in stakeholder-register.md. -->

| Stakeholder | Stake in the outcome |
|---|---|
| STK-0xx |  |

---
---

# Worked Example (delete on real projects)

---
title: Customer Portal Account Access — Vision & Scope
status: reviewed
updated: 2026-06-25
author: Jane Analyst
---

## Problem Statement

A third of support ticket volume is manual password resets at ~10 agent-minutes each, and the dead-end login flow drives users to create duplicate accounts, corrupting billing data (TRN-001). Ticket volume grows with the customer base, so the cost compounds.

## Business Objectives & Success Metrics

| # | Objective | Metric | Baseline | Target |
|---|---|---|---|---|
| 1 | Eliminate agent effort on routine password resets | Reset tickets per month | ~400 | < 40 |
| 2 | Stop duplicate-account creation caused by lockouts | New duplicate accounts per month | ~25 | < 5 |

## In Scope

- Self-service password reset for existing portal accounts.

## Out of Scope

- Cleanup of existing duplicate accounts — separate data-quality initiative.
- SMS/authenticator verification channels at launch (DEC-001).

## Key Stakeholders

| Stakeholder | Stake in the outcome |
|---|---|
| STK-001 | Support team lead — owns the ticket queue the project shrinks |
