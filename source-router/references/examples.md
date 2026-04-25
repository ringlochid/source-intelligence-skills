# Source Router Examples

These examples show how `source-router` should turn user intent into a source plan. Outputs are English-first even when sources are Chinese or multilingual.

---

## Example 1 — Breaking news

**User ask:**

> Track the latest sanctions against a Chinese technology company and explain the likely impact.

**Route:**

```text
source-breaking
+ source-market
+ optional source-social-signal
→ source-briefing
```

**Effort tier:** Standard or Deep, depending on stakes.

**Source plan:**

- `source-breaking`: official government/company statements, reputable news, concrete timestamps.
- `source-market`: stock movement, filings, company IR, sector impact.
- `source-social-signal`: weak signal only for market/social reaction.
- Counter-evidence: search for claims that impact is overstated, delayed, or mitigated.

**Output shape:** Compact brief or report list.

```markdown
**Brief — <company> sanctions** · <retrieval time>

> 🎯 **Best-fit theme:** <one-line answer>.

> **<icon> <finding>**
> - <impact>
> - <market/company context>
>
> - Source: [<label>](<url>) · high

> **<icon> <uncertainty>**
> - <what is still unclear>
>
> - Source: [<label>](<url>) · med

**Watch**
- <official next step>
- <market/company next check>
```

---

## Example 2 — Trending AI research

**User ask:**

> What research is trending this week for AI agents?

**Route:**

```text
source-research
+ source-github
+ source-tech
→ source-briefing
```

**Effort tier:** Standard for a useful digest, Deep for a report/artifact.

**Source plan:**

- `source-research`: arXiv + Semantic Scholar/OpenAlex-style metadata + OpenReview/conference pages + Papers with Code.
- `source-github`: code release/adoption signal.
- `source-tech`: HN/blog discussion as practitioner signal.
- `source-visual`: only for selected papers with important figures/tables.

**Dedupe logic:** Cluster by problem, method, benchmark, dataset, lab, and codebase rather than listing every paper separately.

**Output shape:** Research findings, not a raw paper list.

```markdown
**Research Signals — AI Agents** · <retrieval time>

> 🎯 **Best-fit theme:** evaluation and tool-use reliability are the strongest clusters.

> **<icon> Agent evaluation is getting more diagnostic**
> - Papers focus on failure modes, not just scores.
>
> - Source: [arXiv](<url>) · med

> **<icon> Code/tool-use benchmarks are converging**
> - Repo activity suggests practical adoption.
>
> - Sources: [GitHub](<url>), [Papers with Code](<url>) · med

**Watch**
- Replication/code availability.
- Whether benchmarks become standard in tool releases.
```

---

## Example 3 — Product / marketing opportunity

**User ask:**

> Find product opportunities around AI coding tools for a marketing plan.

**Route:**

```text
source-product
+ source-tech
+ source-github
+ optional source-social-signal
→ source-briefing
→ optional source-artifact
```

**Effort tier:** Standard for ideation; Deep for a plan/report.

**Source plan:**

- `source-product`: Product Hunt, official product pages, pricing, changelogs.
- `source-tech`: AI/dev-tool news and HN discussion.
- `source-github`: open-source repo momentum and release signals.
- `source-social-signal`: weak sentiment/creator reactions only.
- `source-artifact`: only if the user asks to save/create a report.

**Output shape:** Product/marketing/business scan.

```markdown
**Opportunity Scan — AI Coding Tools** · <retrieval time>

> 🎯 **Best-fit theme:** model choice, workflow integration, and enterprise controls are the strongest positioning angles.

> **<icon> BYOK/local models are becoming a buying criterion**
> - Useful for privacy and cost positioning.
>
> - Sources: [GitHub](<url>), [official](<url>) · high

> **<icon> Launch hype is noisy**
> - Product Hunt attention needs retention or usage proof.
>
> - Sources: [Product Hunt](<url>), [site](<url>) · med

**Use in report**
- **Angle:** developer-control and workflow-native agents.
- **Support:** official launches, repo activity, HN discussion.
- **Caveat:** attention does not equal durable adoption.
```

---

## Example 4 — Real visual asset prompt

**User ask:**

> Make an infographic prompt/image brief for today’s biggest AI infrastructure story.

**Route:**

```text
source-tech
+ source-market if funding/compute is material
+ source-visual if charts/pages matter
→ source-briefing
```

No files unless the user asks to save/report/handoff. If they ask to send a real image, generate/send the image after facts are stable.

**Output shape:**

```markdown
**Image Brief — AI Infrastructure** · <retrieval time>

**Factual basis**
1. <verified point>. 〔Official · high〕
2. <verified point>. 〔Reputable · med-high〕
3. <caveat>. 〔Mixed · med〕

**Visual type:** editorial infographic / briefing board
**Layout:** title, retrieval date, 3-5 panels, source-confidence strip
**Prompt:** <safe GPT-image prompt>
**Do not include:** fake screenshots, fake news photos, fabricated quotes, unverified claims
```

If the user asks for `source-visual` instead of an image prompt, send image(s) first:

```markdown
MEDIA:<image-path-or-url>
**Visual:** <one-sentence caption>.
```

---

## Example 5 — Markdown-first artifact

**User ask:**

> Create a research artifact for AI agent trends and save the sources.

**Route:**

```text
source-research
+ source-github
+ source-tech
→ source-briefing
→ source-artifact
```

**Artifact tree:**

```text
source-runs/YYYY-MM-DD-ai-agent-trends/
├── brief.md
├── report-list.md
├── report.md              # optional
├── visual.md               # optional real visual asset prompt/spec
├── notes.md
└── references/
    ├── sources.md
    ├── citation-map.md
    └── rejected.md         # optional
```

Create files only when the user explicitly asks to create/save/write the artifact. If they ask for a sample structure, show the tree only.
