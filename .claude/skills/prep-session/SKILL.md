---
name: prep-session
description: Prepare an elicitation session plan for a topic and stakeholder(s) — tailored questions from the question bank plus unresolved items from prior transcripts. Use when the user asks to prepare, plan, or draft questions for an interview, workshop, or elicitation session.
---

# Prepare an elicitation session plan

Input: a topic and the stakeholder(s) attending. Ask for whichever is missing.

## Steps

1. Gather context:
   - `00-project/stakeholder-register.md` — the attendees' STK rows (role, interest, sessions attended). If an attendee isn't registered, add them with the next free STK ID.
   - Prior transcripts in `01-transcripts/` involving these stakeholders or this topic — read their "Open Questions / Follow-ups" tables and note unresolved rows.
   - `00-project/vision-and-scope.md` — so questions serve the project's objectives.

2. Copy `01-transcripts/elicitation-aids/TEMPLATE-session-plan.md` to `01-transcripts/elicitation-aids/session-plan-<date>-<kebab-topic>.md` and delete the worked example. (Session plans have no ID; the transcript created afterwards gets the TRN.)

3. Fill it in:
   - Objective: 1–3 bullets stating what must be learned — derived from the topic and any gaps you noticed (e.g. an NFR with no volume evidence).
   - Attendees table from the register.
   - Selected questions: pick 8–12 from `elicitation-aids/question-bank.md`, **tailored** — replace every `<task>` placeholder with the real domain object, drop categories that don't fit the session type, and prefer "walk me through the last time…" phrasings.
   - Open Questions Carried Forward: the unresolved rows found in step 1, with their TRN sources.
   - Leave the prep checklist unticked except items you actually completed.

4. Report: plan path, the objective, and which prior open questions were carried forward. Remind the user to record the session with a `transcript` document (`/new-doc`) afterwards and link it in the plan's `transcript:` field.
