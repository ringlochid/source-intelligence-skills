---
name: source-visual
description: Produce image-first visual reads for selected source pages, PDFs, charts, tables, product pages, GitHub pages, research pages, or visual evidence. Use only when the user asks for a visual read or when image evidence matters; output must be image(s) first with a one-sentence caption by default, not text-only notes.
---

# Source Visual

A visual read is **image-first**. It means selecting/capturing/sending one or more relevant images, then adding a one-sentence caption by default. It is not a text-only analysis section.

Use this as an escalation skill, not a default collector.

## When to use

Use visual read when:

- page layout, screenshots, charts, tables, or figures matter
- text extraction/web fetch is sparse or misleading
- PDF extraction is weak, scanned, table-heavy, or figure-heavy
- Product Hunt/GitHub/research pages need visual context
- the user explicitly asks for a visual read
- a real visual asset/image prompt needs accurate layout or figure context
- there is a claim based on an image/screenshot/chart that needs inspection
- breaking news has a meaningful public image/map/chart/photo worth showing

Do not use for every source. It is slower and noisier than text/source metadata. If no meaningful image exists, say so briefly instead of creating a text-only visual read.


## Reference links

Use visual read only when image/visual context is needed; for ordinary text extraction, use normal source collectors instead:

- Playwright screenshots/docs: https://playwright.dev/docs/screenshots
- arXiv PDF help: https://info.arxiv.org/help/submit_pdf.html
- GitHub rendered Markdown: https://docs.github.com/en/get-started/writing-on-github
- Product Hunt: https://www.producthunt.com/

## Workflow

1. Run source collection and dedupe first.
2. Pick the top 3-8 important/unclear sources.
3. Open with browser or screenshot/vision as needed.
4. Capture/select the relevant image(s) first: screenshot, chart crop, article image, public map, figure, or generated editorial image when explicitly appropriate.
5. Send/deliver the image(s) before or with the one-sentence caption.
6. Caption should be one sentence by default: what it shows plus source/context or caveat only if essential.
7. Do not return a text-only visual read. If only text is possible, route back to normal `source-briefing` instead.

## Output shape

Preferred chat shape:

```markdown
MEDIA:<image-path-or-url>
**Visual:** <one-sentence caption>.
```

For multiple images, send the strongest 1-3 images unless the user asks for a gallery.

## Safety

- Do not treat screenshots/images as factual proof unless source/provenance is credible.
- Do not fabricate details from partial screenshots.
- For news visuals, use real/public/source images when available. If generating an editorial image, clearly label it as generated/editorial and do not present it as evidence.
- For PDFs, prefer local text extraction first; use visual read when local extraction misses important figures/tables.
