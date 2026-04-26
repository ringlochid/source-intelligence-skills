---
name: source-artifact
description: Create Markdown-first source-run files only when the user asks to save, report, archive, or hand off sources.
---

# Source Artifact

Use this only for file-backed source intelligence artifacts. Chat-only briefs do not need files.

Read first:
- `../source-common/references/research-contract.md`
- `../source-common/references/output-shapes.md`
- `../source-common/references/citation-and-timestamp-rules.md`
- `../source-common/references/safety-boundaries.md`

Workflow:
1. Confirm the user asked to save/create/report/archive/handoff.
2. Ensure `source-briefing` has already normalized, deduped, cited, and validated the content.
3. Create a deterministic safe folder slug under the requested path or `source-runs/YYYY-MM-DD-topic-slug/`.
4. Write Markdown-first files; create JSON/JSONL only if automation/export is explicitly requested.
5. Put sources/citation maps/rejected sources under `references/`.

Output:
- artifact path
- files written
- source/citation coverage
- missing evidence
- next action
