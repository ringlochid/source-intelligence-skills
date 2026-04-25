---
name: source-briefing
description: Turn gathered source notes into a cited source-intelligence output after normalization, dedupe, validation, timestamps, source quality, confidence, and citations. Use for quick briefs, deep research, product/marketing/business scans, competitor scans, watchlist updates, and optional factual bases/prompts for real visual assets after source-router has chosen the source plan and effort tier.
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

- **Chat-only:** produce the compact readable brief in chat; no files. Do not call this a visual asset unless a real image/infographic/prompt is requested.
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
6. **Escalate visually when needed:** if the user asks for visual read or image evidence matters, use `source-visual` on selected important sources. It must return image(s) first with a one-sentence caption by default, not text-only notes.

## Effort-aware output

Output length should stay concise; effort tier mostly changes collection and verification depth, not how much prose to dump.

- **Quick:** usually 10-20 raw sources → 5-8 final findings.
- **Standard:** usually 20-50 raw sources → 5-8 mobile findings by default, or 8-12 if the user wants a fuller digest/report.
- **Deep:** usually 50-100+ raw sources → evidence map, contradictions, and stronger citations; still summarize tightly.
- **Watchlist:** only new/material changes since the last known state.

## Mobile-first output style

Default to a compact card shape for Telegram/chat. Avoid separate `Sources:` and `Confidence:` lines per item; they wrap badly. Put metadata inline as chips.

For Telegram, default to a **readable chat brief**, not a visual asset. The Notion-style callout pattern is a readability format. Real visual output means an image, infographic, prompt, or file, and should only be produced when the user explicitly asks for it.

Rules:

- Lead with a one-line verdict.
- Keep each finding to 1-2 short lines.
- Use compact source/confidence chips: `〔Official · high〕`, `〔GitHub+HN · med〕`, `〔X signal · low〕`.
- Prefer soft visual callout cards: short verdict/insight boxes, per-entry quoted callouts, and compact code/markdown blocks when showing reusable structures.
- Apply the Notion-style callout pattern to each important news/content entry, not only the top summary.
- Inside each callout, use bullets when an entry has multiple claims/implications/source metadata; do not cram several clauses into one paragraph. Put a blank quoted line between content bullets and the source bullet for readability.
- Use markdown links with human labels so Telegram hides long URLs, e.g. `Source: [AP](https://...)` or `Sources: [Axios](https://...), [UN Geneva](https://...)`. Do not paste raw URLs unless the user asks.
- Use icons instead of numeric prefixes when it improves scanability. Choose icons freely to match the vibe/content of each item; do not use a fixed taxonomy. Icons should feel natural for the specific information, not mechanically mapped by type. Avoid visual clutter or repeating the same icon too many times in one brief.
- Use one restrained marker emoji only when it clarifies the role of a block, e.g. `🎯 Best-fit theme:` or `💡 Key insight:`. Avoid semantic severity labels like RED/AMBER unless the user explicitly asks for risk triage.
- Prefer short separators, bold lead labels, and readable cards over long paragraphs.
- Group long evidence details under `Evidence` only for deep mode.
- Use `Watch` for 2-3 concrete watchpoints, not a long checklist.
- If sending 10 findings, keep each under ~28 words when practical.

### Telegram-readable brief pattern

Use this shape for news, topic briefings, planning notes, and watchlist reports. It is a readable chat format, not a real visual asset. Telegram blockquotes are normally blue/accent-colored and cannot be arbitrarily recolored; vary structure with callouts, bullets, bold labels, separators, and restrained markers rather than pretending custom colors exist.

~~~markdown
**<Brief title>** · <date/time timezone>

> 🎯 **Best-fit theme:** <one-sentence synthesis / recommendation>.

> **<icon> <finding headline>**
> - <what changed>
> - <why it matters / implication>
>
> - Source: [<source label>](<url>) · <confidence>

> **<icon> <finding headline>**
> - <what changed>
> - <why it matters / implication>
>
> - Sources: [<source label>](<url>), [<source label>](<url>) · <confidence>

**Use / next move**
- <concrete action or watchpoint>
- <concrete action or watchpoint>

**Reusable structure**
```md
## <topic or source>
- **Type:** <type>
- **URL/query:** <url/query>
- **Use for:** <when this source matters>
```
~~~

For breaking-news reports, lead with the synthesis card, then use ranked findings. Do not label the chat output as a visual asset. Do not use semantic color/severity labels unless specifically asked for incident/risk triage.

Keep source links inside each callout as labelled markdown links (`Source: [AP](...)`) so Telegram renders a short clickable source name. Do not expose raw URLs in normal chat briefs.

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

Use for report/slide/design/marketing artifacts. It mirrors the compact readable-brief structure, but stays text-only.

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

### Real visual asset / image prompt

Only after factual claims are stable and only when the user explicitly asks for a visual asset, image, infographic, or visual prompt. Generate an editorial image spec from verified facts; the image is presentation, not evidence. If the user asks to send an image, use the available image-generation/send path. If they ask to save/report/handoff, write `visual.md` through `source-artifact`.

```markdown
**Factual basis:** 3-5 verified points with sources
**Visual type:** infographic / timeline / map / comparison matrix / briefing cover
**Layout:** title, retrieval date, key panels, source/confidence strip
**Safe image prompt:** ...
**Do not include:** fake photojournalism, invented scenes, fake screenshots, gore, unverified claims
```

## Style

Lead with the answer. Keep Telegram output compact unless the user asks for depth. Mark uncertainty plainly.
