# 05 — Decision Log

One file per significant requirements decision (`DEC-###`). A decision is "significant" when someone will plausibly ask *"why is it like this?"* in six months — scope cuts, channel/platform choices, priority calls that overrode a stakeholder, conflicting-definition resolutions.

## When to create one

At the moment the decision is made — in the meeting if possible. A decision that isn't written down within a day tends to get re-litigated.

## Naming

`DEC-###-short-kebab-title.md`, e.g. `DEC-001-email-only-verification.md`.

Copy `TEMPLATE-decision.md`, rename, fill in.

## Quality checklist

- The **alternatives rejected** section is the point of the document — a decision with no alternatives considered is just a note.
- Name the **deciders**; "the team decided" is unfalsifiable.
- List the **affected documents** by ID and update their content in the same change — a decision the requirements don't reflect is fiction.
- Decisions are never deleted or edited after approval; a reversal is a **new** DEC that supersedes the old one (link both ways).
