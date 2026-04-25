---
name: source-visual-read
description: Visually inspect selected source pages, PDFs, charts, tables, product pages, GitHub pages, research pages, or visual evidence using browser/screenshot/vision when text fetch is insufficient. Use only as an escalation after source planning/dedupe, usually for the top 3-8 important sources, then return notes to source-briefing.
---

# Source Visual Read

Use this as an escalation skill, not a default collector.

## When to use

Use visual read when:

- page layout, screenshots, charts, tables, or figures matter
- text extraction/web fetch is sparse or misleading
- PDF extraction is weak, scanned, table-heavy, or figure-heavy
- Product Hunt/GitHub/research pages need visual context
- a visual brief/image prompt needs accurate layout or figure context
- there is a claim based on an image/screenshot/chart that needs inspection

Do not use for every source. It is slower and noisier than text/source metadata.


## Reference links

Use visual read only when text extraction misses important layout/figure/table context:

- Playwright screenshots/docs: https://playwright.dev/docs/screenshots
- arXiv PDF help: https://info.arxiv.org/help/submit_pdf.html
- GitHub rendered Markdown: https://docs.github.com/en/get-started/writing-on-github
- Product Hunt: https://www.producthunt.com/

## Workflow

1. Run source collection and dedupe first.
2. Pick the top 3-8 important/unclear sources.
3. Open with browser or screenshot/vision as needed.
4. Extract only decision-relevant visual facts: chart trends, table values, UI layout, figure claims, visible caveats, provenance.
5. Send concise visual notes to `source-briefing`.

## Safety

- Do not treat screenshots as factual proof unless source/provenance is credible.
- Do not fabricate details from partial screenshots.
- For news visuals, use visual read to inform editorial explainers, not fake evidence.
- For PDFs, prefer local text extraction first; use visual read when local extraction misses important figures/tables.
