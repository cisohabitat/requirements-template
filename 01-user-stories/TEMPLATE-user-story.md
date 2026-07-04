---
id: US-000             # next free US number
title: <Short title>
status: draft          # draft | reviewed | approved | deprecated
date: YYYY-MM-DD
author: <BA name>
priority: should       # must | should | could | wont  (MoSCoW)
source: []             # transcript ids this story came from, e.g. [TRN-001]
journeys: []           # related journey ids, e.g. [UJ-001]
---

# US-000 — <Short title>

## Story

> **As a** <persona / role>,
> **I want** <capability>,
> **so that** <benefit — a real outcome, not a restatement of the feature>.

## Acceptance Criteria

<!-- Concrete, testable scenarios. Add as many as needed. -->

### AC1 — <scenario name>

- **Given** <precondition>
- **When** <action>
- **Then** <expected outcome>

### AC2 — <scenario name>

- **Given**
- **When**
- **Then**

## Notes & Assumptions

<!-- Constraints, out-of-scope decisions, dependencies on other stories. -->

-

---
---

# Worked Example (delete on real projects)

---
id: US-001
title: Password reset
status: approved
date: 2026-06-18
author: Jane Analyst
priority: must
source: [TRN-001]
journeys: [UJ-001]
---

## Story

> **As a** portal customer who has forgotten my password,
> **I want** to reset it myself from the login page,
> **so that** I regain access immediately instead of waiting on a support ticket.

## Acceptance Criteria

### AC1 — Happy path

- **Given** a registered customer on the login page
- **When** they choose "Forgot password" and submit their registered email address
- **Then** a single-use reset link is emailed to them, valid for 30 minutes

### AC2 — Unregistered email

- **Given** an email address with no matching account
- **When** it is submitted to the reset form
- **Then** the same confirmation message is shown (no account enumeration), and no email is sent

## Notes & Assumptions

- Email is the only verification channel at launch (confirmed in TRN-001 follow-up).
- Duplicate-account cleanup is out of scope for this story.
