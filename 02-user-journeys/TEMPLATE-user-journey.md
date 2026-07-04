---
id: UJ-000             # next free UJ number
title: <Short title>
status: draft          # draft | reviewed | approved | deprecated
date: YYYY-MM-DD
author: <BA name>
persona: <Persona name / role>
source: []             # transcript ids, e.g. [TRN-001]
stories: []            # related story ids, e.g. [US-001]
---

# UJ-000 — <Short title>

## Persona

<!-- Who is on this journey. A sentence or two: role, context, relevant traits. -->

## Scenario & Trigger

<!-- The situation that starts the journey. What just happened? -->

## Goal

<!-- The single outcome the persona wants. If there are two goals, write two journeys. -->

## Journey Stages

| # | Stage | User action | Touchpoint | Pain point | Opportunity |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## Success Outcome

<!-- What "done" looks and feels like for the persona. -->

## Related Stories

<!-- Which stories address the pain points above. -->

- US-0xx — <how it relates>

---
---

# Worked Example (delete on real projects)

---
id: UJ-001
title: Locked-out customer regains access
status: approved
date: 2026-06-19
author: Jane Analyst
persona: Portal customer (non-technical, infrequent user)
source: [TRN-001]
stories: [US-001]
---

## Persona

An infrequent portal user — logs in a few times a year to view invoices. Not technical; unlikely to remember a password between visits.

## Scenario & Trigger

An invoice-due email prompts a login attempt. The password fails three times.

## Goal

Get back into the account and view the invoice, today.

## Journey Stages

| # | Stage | User action | Touchpoint | Pain point | Opportunity |
|---|---|---|---|---|---|
| 1 | Realise locked out | Tries password variants, fails | Login page | No guidance after failure | Offer reset path directly on the failure message |
| 2 | Seek help | Searches for a reset option, finds none (TRN-001) | Login page | Dead end — only option is support | Self-service "Forgot password" link (US-001) |
| 3 | Contact support | Raises ticket, waits | Email / phone | Hours-to-days delay; some create duplicate accounts instead | Instant automated reset removes the wait entirely |
| 4 | Regain access | Agent resets manually, user logs in | Email | Manual step costs ~10 agent-minutes | Fully automated, no agent involvement |

## Success Outcome

The customer resets their password and views the invoice in one sitting, with no support contact.

## Related Stories

- US-001 — self-service password reset removes stages 3–4 entirely.
