# 03 — Requirements

Formal requirements derived from user stories and journeys. One file per requirement.

| Subfolder | Contains | ID prefix |
|---|---|---|
| `functional/` | What the system **does** — behaviour, features, rules | `FR-###` |
| `non-functional/` | How well it does it — performance, security, usability, availability, compliance | `NFR-###` |

## Functional vs non-functional — the quick test

If you can describe it as a user-observable **action or rule** ("the system shall send a reset link"), it's functional. If it's a **quality or constraint** on how actions happen ("within 60 seconds", "hashed with bcrypt", "99.9% uptime"), it's non-functional.

## Naming

- `FR-###-short-kebab-title.md` — copy `functional/TEMPLATE-functional-requirement.md`
- `NFR-###-short-kebab-title.md` — copy `non-functional/TEMPLATE-non-functional-requirement.md`

## Quality checklist

Every requirement must be:

- **Unambiguous** — one interpretation only; "fast", "user-friendly", "secure" are banned words unless quantified.
- **Testable** — the verification criteria say exactly how you'd prove it's met.
- **Atomic** — one requirement per file; "and" in the description is a smell.
- **Traced** — `source` cites the story/journey/transcript it derives from.
- **Necessary** — you can name who is harmed if it's dropped.
