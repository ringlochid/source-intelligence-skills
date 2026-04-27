---
name: source-briefing
description: Synthesize gathered source notes into a cited brief with quality, confidence, timestamps, caveats, and missing evidence.
---

# Source Briefing

Use this as the final synthesis step after source collection. A briefing answers what changed/found, why it matters, what evidence supports it, and what remains uncertain.

Read first:
- `../source-common/references/safety-boundaries.md`
- `../source-common/references/research-contract.md`
- `../source-common/references/source-quality-ladder.md`
- `../source-common/references/citation-and-timestamp-rules.md`
- `../source-common/references/claim-verification-loop.md`
- `../source-common/references/output-shapes.md`
- `../source-common/references/chat-brief-style.md`

Workflow:
1. Normalize source notes: title, source, URL, date/time, author/org, key claims, source type, language.
2. Dedupe by URL, event/entity/date, paper ID, repo, ticker, product, or status ID.
3. Rank source quality and reject weak/slop sources when needed.
4. Cross-check high-risk or disputed claims.
5. Separate facts, reported claims, signals, and inference.
6. For Telegram/scheduled briefs, use the chat brief style ref: title, quoted theme, quoted cards; every line in a card starts with `>`.
7. Produce the smallest useful cited brief.
8. Route to `source-artifact` only if files are requested; route to `source-visual` only when visual evidence/output is requested or materially useful.

Output:
- answer/verdict first
- card-style evidence-backed findings for chat/scheduled briefs
- citations/timestamps
- confidence/caveats
- missing evidence
- next checks/watchpoints
