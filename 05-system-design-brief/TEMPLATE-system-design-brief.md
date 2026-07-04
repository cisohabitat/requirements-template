---
title: <System name> — System Design Brief
status: draft          # draft | reviewed | approved
date: YYYY-MM-DD
author: <BA name>
assembled_from: traceability-matrix.md as of YYYY-MM-DD
---

# <System name> — System Design Brief

<!-- The single input document for system design. Reference IDs; don't duplicate detail. -->

## 1. Executive Summary

<!-- The problem, the evidence it's worth solving, and the shape of the solution. Half a page max. -->

## 2. Personas & Journeys

<!-- One row per journey; detail lives in 02-user-journeys/. -->

| Journey | Persona | Goal | Key pain points |
|---|---|---|---|
| UJ-0xx |  |  |  |

## 3. User Stories (prioritised)

| Story | Title | Priority | Status |
|---|---|---|---|
| US-0xx |  | must |  |

## 4. Functional Requirements

<!-- Group into subsections (§4.1, §4.2 …) by capability area; the traceability matrix
     points at these section numbers. -->

### 4.1 <Capability area>

| Requirement | Title | Priority | Source |
|---|---|---|---|
| FR-0xx |  | must | US-0xx |

## 5. Non-Functional Requirements

### 5.1 <Category, e.g. Performance>

| Requirement | Title | Target | Applies to |
|---|---|---|---|
| NFR-0xx |  |  | FR-0xx |

## 6. Constraints & Assumptions

<!-- Technical, organisational, regulatory. Cite where each came from. -->

-

## 7. Out of Scope

<!-- Explicit exclusions, with the story/transcript where the decision was made. -->

-

## 8. Open Questions for Design

<!-- Unresolved items the design team must settle or escalate. -->

| # | Question | Raised in | Owner |
|---|---|---|---|
| 1 |  |  |  |

## Appendix — Sources

- Transcripts: `../00-transcripts/` (TRN-0xx …)
- User stories: `../01-user-stories/` (US-0xx …)
- User journeys: `../02-user-journeys/` (UJ-0xx …)
- Requirements: `../03-requirements/` (FR-0xx, NFR-0xx …)
- Traceability: `../04-traceability/traceability-matrix.md`

---
---

# Worked Example (excerpt — delete on real projects)

---
title: Customer Portal Account Access — System Design Brief
status: reviewed
date: 2026-06-25
author: Jane Analyst
assembled_from: traceability-matrix.md as of 2026-06-25
---

## 1. Executive Summary

A third of support ticket volume is manual password resets (~10 agent-minutes each), and the dead-end login flow drives duplicate-account creation (TRN-001). This brief covers a self-service account-access capability: automated password reset via emailed single-use links, removing agent involvement entirely.

## 2. Personas & Journeys

| Journey | Persona | Goal | Key pain points |
|---|---|---|---|
| UJ-001 | Infrequent portal customer | Regain account access same-day | No self-service path; hours-to-days support wait |

## 3. User Stories (prioritised)

| Story | Title | Priority | Status |
|---|---|---|---|
| US-001 | Password reset | must | approved |

## 4. Functional Requirements

### 4.1 Account recovery

| Requirement | Title | Priority | Source |
|---|---|---|---|
| FR-001 | Self-service password reset | must | US-001 |

## 5. Non-Functional Requirements

### 5.1 Performance

| Requirement | Title | Target | Applies to |
|---|---|---|---|
| NFR-001 | Reset link delivery latency | p95 ≤ 60 s | FR-001 |

## 6. Constraints & Assumptions

- Email is the only verification channel at launch (TRN-001 follow-up).

## 7. Out of Scope

- Duplicate-account cleanup (US-001 notes) — separate initiative.

## 8. Open Questions for Design

| # | Question | Raised in | Owner |
|---|---|---|---|
| 1 | Which transactional email provider meets the NFR-001 latency target? | NFR-001 review | Design team |
