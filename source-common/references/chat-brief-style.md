# Chat Brief Style

Use this for Telegram/chat source briefs. Preserve the original card-like scan shape.

## Shape

- title line first: `**<Brief title>** · <date/time/timezone>`
- one short quoted theme line
- 3-6 compact finding cards by default
- every line inside a card must start with `>`: heading, bullets, and source line
- each card: emoji/headline, 1-3 short bullets, compact source/confidence line
- sources belong on the card's final quoted line: `> - Sources: AP, Reuters · high`
- use labelled Markdown links sparingly; avoid long inline-link sentences
- include `Watch` only when it adds action
- avoid raw URLs and naked final links that create preview spam
- no flat wall of bullets for scheduled briefs

## Card pattern

```markdown
**<Brief title>** · <date/time/timezone>

> 🎯 **Theme:** <one-sentence synthesis>.

> **<icon> <finding headline>**
> - <what changed/found>
> - <why it matters / caveat>
> - Sources: <labelled sources> · <confidence>
>
> Card rule: if a line belongs to the card, it starts with `>`.

**Watch**
- <concrete check>
- <concrete check>
```

Use icons only when they improve scanability. Do not pretend Telegram supports custom callout colors.
