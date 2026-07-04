# 02 — User Stories

One file per user story, distilled from the transcripts in `01-transcripts/`.

## When to create one

After reviewing a session record, turn each candidate requirement that describes **user-visible behaviour** into a story. (Purely technical or quality constraints go straight to `04-requirements/non-functional/`.)

## Naming

`US-###-short-kebab-title.md`, e.g. `US-001-password-reset.md`.

Copy `TEMPLATE-user-story.md`, rename, fill in.

## Quality checklist

A good story is:

- **Independent** — deliverable without waiting on other stories where possible.
- **Valuable** — the "so that" clause names a real benefit, not a restatement of the feature.
- **Testable** — acceptance criteria are concrete Given/When/Then scenarios.
- **Traced** — the `source` field cites the transcript(s) it came from.
