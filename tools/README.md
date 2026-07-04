# Tools

`reqs.py` — scaffolding, traceability, and validation for this repo. **Standard library only** (Python 3.9+); no packages to install.

## Commands

### Scaffold a document

```
python tools/reqs.py new <type> "<title>"
```

Types: `transcript` `story` `journey` `fr` `nfr` `decision`.

Picks the next free ID in the series, copies the folder's `TEMPLATE-` file, strips the worked example, fills in `id`, `title`, `date` (today), and `author` (from `git config user.name`), and writes `<ID>-kebab-title.md`. Prints the new file's path.

```
$ python tools/reqs.py new story "Password reset"
02-user-stories/US-001-password-reset.md
```

### Regenerate the traceability matrix

```
python tools/reqs.py matrix
```

Reads every document's frontmatter and rebuilds the table in `06-traceability/traceability-matrix.md` between the `BEGIN/END GENERATED` markers — one row per FR/NFR, with sources resolved transitively (an NFR citing FR-001 inherits FR-001's transcripts and stories). The "Design brief §" column is filled by scanning any assembled brief in `07-system-design-brief/` for ID mentions. Also prints the validation report.

Run it after creating any requirement or changing a document's status or references.

### Validate

```
python tools/reqs.py check
```

Reports problems without writing anything; exits non-zero if there are errors.

- **Errors:** malformed/missing frontmatter, frontmatter `id` not matching the filename, duplicate IDs, invalid `status`/`priority` values, references to nonexistent documents, orphaned requirements (no sources).
- **Warnings:** user stories with no covering requirement, `must` requirements not referenced in the design brief (once a brief exists).

## Constraints

Frontmatter must stay simple — one `key: value` per line, lists inline as `[A, B]`. That's what the templates use and all the parser supports; if you need block lists or multiline values, keep them out of the reference fields (`source`, `journeys`, `applies_to`, `affects`, `stories`, `depends_on`).
