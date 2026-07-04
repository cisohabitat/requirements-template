---
name: extract-stories
description: Draft user stories (and candidate requirements) from an elicitation transcript, with correct IDs and source links. Use when the user asks to extract, derive, or draft stories/requirements from a transcript or session record.
---

# Extract stories from a transcript

Input: a transcript file in `01-transcripts/` (ask which one if not given; offer the most recent by ID).

## Steps

1. Read the transcript fully. Candidate material lives everywhere, not just the "Candidate Requirements Spotted" table: verbatim quotes, pain points, workarounds, and the takeaways section.

2. For each distinct piece of **user-visible behaviour**, scaffold a story:

   ```
   python tools/reqs.py new story "<title>"
   ```

   Fill it in from transcript evidence only — no invented requirements:
   - `source: [TRN-xxx]` pointing at this transcript.
   - The "so that" clause states the benefit the stakeholder actually described.
   - Acceptance criteria as Given/When/Then, derived from what was said; where the transcript is silent, write the AC and flag the assumption in Notes & Assumptions.
   - Priority: only set beyond `should` if the stakeholder expressed urgency; note the quote.

3. For clearly quality-shaped statements (volumes, latencies, security, compliance), scaffold `nfr` documents with the same evidence discipline: `source: [TRN-xxx]`, priority beyond `should` only with a supporting quote, and analyst-invented targets (e.g. a p95 number the stakeholder never said) flagged as assumptions in the NFR's Rationale section — the NFR template has no Notes & Assumptions section. Do NOT scaffold `fr` documents yet — functional requirements are derived from reviewed stories, not raw transcripts, unless the user asks for them explicitly.

4. Update the transcript's "Candidate Requirements Spotted" table: fill the "Formalised as" column with the new IDs. Candidates you deliberately did not formalise get a short reason instead.

5. Add any new domain terms to `00-project/glossary.md` as `proposed`, and any new people to the stakeholder register. If a term or person is already covered by a row — including a leftover `*(example — delete)*` row — update that row instead of adding a duplicate, and tell the user the worked examples haven't been cleaned out yet.

6. Finish with `python tools/reqs.py matrix` and `python tools/reqs.py check`, then summarise for the user: each new document (ID, title, one line), assumptions flagged, candidates skipped and why. Everything stays `status: draft` for human review. A `check` warning that the new stories have "no covering requirement" is **expected** at this stage — FRs come later, from reviewed stories; do not silence it by pointing the NFRs' `source` at the stories.
