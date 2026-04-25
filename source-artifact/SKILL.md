---
name: source-artifact
description: Create Markdown-first source-run artifact folders for reports, research packs, product/marketing/business plans, saved source packs, real visual asset prompts/specs, handoff, or archive/watchlist outputs. Use only when the user asks to save, create files, prepare a report/artifact, or preserve references; chat-only briefs do not need this skill.
---

# Source Artifact

Use this only for file-backed source intelligence artifacts. Do not create files for ordinary chat briefs unless the user asks to save/report/handoff/archive.

If the user or test request asks for a **sample artifact structure**, show the tree only. Do not write files unless the request explicitly says to create/save/write the artifact.

## When to use

Use when the request says or implies:

- make a report
- prepare a research artifact/source pack
- save the sources
- create a product/marketing/business plan with references
- make a real visual asset prompt/spec as a file
- hand this off
- archive/preserve/watchlist update

Do not use for:

- quick chat answers
- chat-only readable brief
- raw “what’s happening?” updates

## Default folder

Create under the current workspace unless the user specifies a repo/path:

```text
source-runs/YYYY-MM-DD-topic-slug/
├── brief.md
├── report-list.md          # short finding list for reports/slides
├── report.md               # optional, if asked
├── visual.md                # optional real visual asset prompt/spec, if asked
├── notes.md
└── references/
    ├── sources.md
    ├── citation-map.md
    └── rejected.md         # optional
```

Keep top-level human-readable. Put source support material under `references/`.

## Markdown-first policy

Default to Markdown files. Do not create JSON/JSONL unless:

- automation/export is explicitly requested
- a script/tool will consume the data
- the user asks for structured data

## File roles

- `brief.md` — concise final brief.
- `report-list.md` — short structured list of findings for reports/slides, using the same compact readable structure as chat briefs.
- `report.md` — longer report/plan if requested.
- `visual.md` — factual basis + visual type/layout + safe image prompt/spec for a real visual asset.
- `notes.md` — caveats, contradictions, decisions, next checks, method notes.
- `references/sources.md` — grouped source list with annotations and timestamps.
- `references/citation-map.md` — final claims/findings mapped to supporting sources.
- `references/rejected.md` — weak/rejected sources and why they were excluded.

## `report-list.md` shape

Use this when the artifact may feed a report, slide, Notion page, or design/marketing plan.

```markdown
# Report List — <topic>

Retrieved: <date/time/timezone>

1. **<finding>** — <one-line implication>. 〔source tier/confidence〕
2. ...

## Use in report

- **Angle:** <main narrative>
- **Support:** <best 3-5 evidence points>
- **Caveat:** <main uncertainty>
```

## Required behavior

The dedupe/review logic does not live in files. `source-briefing` performs normalize/dedupe/review/validate in memory first. `source-artifact` only persists the result cleanly.

Before writing, ensure the output folder name is deterministic and safe: lowercase slug, no spaces, no secrets.
