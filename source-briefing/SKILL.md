---
name: source-briefing
description: Turn gathered source notes into a cited source-intelligence output after normalization, dedupe, validation, timestamps, source quality, confidence, and citations. Use for quick briefs, deep research, product/marketing/business scans, competitor scans, watchlist updates, and safe visual briefing prompts after source-router has chosen the source plan and effort tier.
---

# Source Briefing

Use this as the final step for the source-intelligence bundle.

English is the default output language. Chinese and other non-English sources are valid inputs; translate source titles/claims/summaries into English, while preserving original names/terms when useful.

## What a briefing is

A briefing is not a generic summary. It answers:

- what changed or what was found
- why it matters
- what the evidence is
- how reliable it is
- what to watch next
- what action, if any, follows

## Storage behavior

Dedupe/review/validation happens in memory for both chat and file outputs.

- **Chat-only:** produce the compact brief/visual brief in chat; no files.
- **Artifact/report/save/handoff:** after review, call `source-artifact` to persist a Markdown-first source pack.
- **Automation/export:** create JSON/JSONL only if explicitly requested.

## Time-aware ranking

For current/trending/news-style requests, rank newer confirmed developments above older context. Keep older sources only when they explain background, contradictions, or trend history. Always show or preserve publish/update/retrieval times when they affect confidence.

## Required checks before output

1. **Normalize** source notes: title, source, URL, publish/update time, retrieved time, author/org, key claims, source type, and source language when relevant.
2. **Dedupe** by canonical URL, title, event/entity/date, arXiv ID, repo full name, ticker/coin/date, product name, or tweet/status ID.
3. **Score source quality:**
   - A: official/primary — docs, filings, papers, repos, regulator/company statements.
   - B: reputable secondary — wire services, established specialist publications, named expert analysis with evidence.
   - C: useful signal — HN, Product Hunt, GitHub trending, credible personal blogs/X accounts.
   - D: weak signal — aggregators, anonymous social, repost chains.
   - E: reject — no URL/timestamp, obvious slop, fabricated-looking screenshots, contradicted claims.
4. **Validate high-risk claims:** breaking news needs two credible sources or explicit uncertainty; finance needs separate market data; X is never sole proof.
5. **Cite** factual claim clusters.
6. **Escalate visually when needed:** if text metadata misses charts/tables/figures/screenshots/layout, use `source-visual-read` on selected important sources before final output.

## Effort-aware output

Output length should stay concise; effort tier mostly changes collection and verification depth, not how much prose to dump.

- **Quick:** usually 10-20 raw sources → 5-8 final findings.
- **Standard:** usually 20-50 raw sources → 5-8 mobile findings by default, or 8-12 if the user wants a fuller digest/report.
- **Deep:** usually 50-100+ raw sources → evidence map, contradictions, and stronger citations; still summarize tightly.
- **Watchlist:** only new/material changes since the last known state.

## Mobile-first output style

Default to a compact card shape for Telegram/chat. Avoid separate `Sources:` and `Confidence:` lines per item; they wrap badly. Put metadata inline as chips.

Rules:

- Lead with a one-line verdict.
- Keep each finding to 1-2 short lines.
- Use compact source/confidence chips: `〔Official · high〕`, `〔GitHub+HN · med〕`, `〔X signal · low〕`.
- Group long evidence details under `Evidence` only for deep mode.
- Use `Watch` for 2-3 concrete watchpoints, not a long checklist.
- If sending 10 findings, keep each under ~28 words when practical.

## Example output shapes

These are examples, not rigid route names. Choose the shape that fits the user's intent and source plan.

### Quick brief

```markdown
**AI / Tech Brief** · 25 Apr, 11:41 Sydney
Verdict: tooling momentum is strong; rumor quality is mixed.

1. **OpenAI expanded API/tooling options** — useful for agent workflows. 〔OpenAI · high〕
2. **Anthropic posted a model/safety update** — enterprise/governance signal. 〔Anthropic+coverage · high〕
3. **New coding-agent repo is trending** — attention is real; quality unproven. 〔GitHub+HN · med〕
4. **Google updated AI dev tooling** — relevant to multimodal prototyping. 〔Google · high〕
5. **AI research assistant launched** — PH traction, but early validation only. 〔PH+site · med〕

**Watch**
- Verify model rumors against official docs.
- Check trending repos for releases/tests.
- Separate PH hype from durable usage.
```

### Deep research brief

```markdown
**Question:** ...
**Answer first:** ...

**Evidence map**
- Claim: ...
  - Sources: ...
  - Confidence: ...
  - Caveats: ...

**Contradictions / uncertainty:** ...
**Next reading / checks:** ...
```

### Product / marketing / business scan

```markdown
**Opportunity / insight:** ...
**Signal:** sources and observed behavior
**Why now:** ...
**Who cares:** ...
**Evidence:** ...
**Risks / false positives:** ...
**Action:** concrete next step
```

### Competitor scan

```markdown
**Competitor / segment:** ...
**Recent moves:** ...
**Positioning:** ...
**Pricing / packaging:** ...
**Signals:** ...
**Implications:** ...
```

### Watchlist update

```markdown
**New since last check:** ...
**Changed materially:** ...
**No meaningful change:** ...
```

### Report list

Use for report/slide/design/marketing artifacts. It mirrors the compact visual-brief structure, but stays text-only.

```markdown
**Report List — <topic>**
Retrieved: <date/time/timezone>

1. **<finding>** — <one-line implication>. 〔source tier/confidence〕
2. ...

**Use in report**
- **Angle:** <main narrative>
- **Support:** <best 3-5 evidence points>
- **Caveat:** <main uncertainty>
```

### Visual briefing prompt

Only after factual claims are stable. Generate an editorial image spec, not evidence. If the user only wants the visual in chat, do not create files; if they ask to save/report/handoff, write `visual-brief.md` through `source-artifact`.

```markdown
**Factual basis:** 3-5 verified points with sources
**Visual type:** infographic / timeline / map / comparison matrix / briefing cover
**Layout:** title, retrieval date, key panels, source/confidence strip
**Safe image prompt:** ...
**Do not include:** fake photojournalism, invented scenes, fake screenshots, gore, unverified claims
```

## Style

Lead with the answer. Keep Telegram output compact unless the user asks for depth. Mark uncertainty plainly.
