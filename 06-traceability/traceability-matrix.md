---
title: Traceability Matrix
status: draft          # draft | reviewed | approved
updated: YYYY-MM-DD
author: <BA name>
---

# Traceability Matrix

**Generated document** — the table below is rebuilt from document frontmatter by:

```
python tools/reqs.py matrix
```

Run it after creating any requirement or changing a document's status or references. Do not edit between the markers; fix the source documents instead. See `README.md` in this folder for the rules.

<!-- BEGIN GENERATED -->
| Requirement | Title | Source transcript(s) | User story(ies) | Journey(s) | Design brief § | Priority | Status |
|---|---|---|---|---|---|---|---|
| *(no requirements yet)* |  |  |  |  |  |  |  |
<!-- END GENERATED -->

## Coverage Checks

`python tools/reqs.py check` verifies these automatically (broken references and orphans are errors; coverage gaps are warnings). Run through the list before sign-off; record exceptions rather than deleting the question.

- [ ] Every transcript's "Candidate Requirements Spotted" table has each row either formalised (ID filled in) or explicitly rejected with a note.
- [ ] Every approved user story is covered by at least one requirement.
- [ ] Every requirement has at least one source — no orphans.
- [ ] Every `must` requirement is referenced in the system design brief.
