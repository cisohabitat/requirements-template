---
id: NFR-000            # next free NFR number
title: <Short title>
status: draft          # draft | reviewed | approved | deprecated
date: YYYY-MM-DD
author: <BA name>
priority: should       # must | should | could | wont  (MoSCoW)
category: performance  # performance | security | usability | availability | scalability | compliance | maintainability | other
source: []             # story/journey/transcript/FR ids, e.g. [FR-001]
applies_to: []         # FR ids this quality constrains; empty = system-wide
---

# NFR-000 — <Short title>

## Requirement

<!-- One sentence with a measurable target. If you can't measure it, sharpen it until you can. -->

The system shall …

## Target & Metric

<!-- The number, the unit, and the conditions under which it's measured. -->

| Metric | Target | Measured under |
|---|---|---|
|  |  |  |

## Rationale

<!-- Why this level and not a looser/stricter one. Cite evidence. -->

## Verification Method

<!-- How it will be proven: load test, pen test, audit, usability study… -->

-

---
---

# Worked Example (delete on real projects)

---
id: NFR-001
title: Reset link delivery latency
status: approved
date: 2026-06-20
author: Jane Analyst
priority: must
category: performance
source: [FR-001, TRN-001]
applies_to: [FR-001]
---

## Requirement

The system shall deliver password-reset emails such that 95% arrive within 60 seconds of the request.

## Target & Metric

| Metric | Target | Measured under |
|---|---|---|
| Time from form submission to email accepted by recipient's mail server | p95 ≤ 60 s | Normal load (≤ 100 reset requests/hour) |

## Rationale

The value of self-service reset (FR-001) is immediacy — the persona in UJ-001 is mid-task. A reset slower than a few minutes pushes users back to support tickets, defeating the requirement's purpose.

## Verification Method

- Automated test harness submits 200 reset requests over an hour against a staging mail sink; assert p95 delivery ≤ 60 s.
