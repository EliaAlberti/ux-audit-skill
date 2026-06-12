# Contributing

Thanks for your interest in improving the UX Audit Skill. It's a single Markdown skill plus a small Python script, so contributions are low-friction.

## Good first contributions

- **New named checks**: add a stable ID + description to the Named Recurring Checks table in `SKILL.md`. The bar: it's a recurring, screenshot-visible issue that doesn't already map cleanly to an existing check.
- **Framework refinements**: tighten a citation, fix a heuristic number, or clarify how a principle is applied.
- **Domain modules**: a named set of checks for a vertical (fintech, healthcare, e-commerce, accessibility-first, etc.), kept separate so the core stays universal.
- **Annotation improvements**: the HTML fallback, multi-page handling, or better label placement in `scripts/annotate.py`.

## Principles to preserve

These are what make the output trustworthy, please don't regress them:

1. **Every finding cites a named heuristic.** No generic feedback.
2. **Evidence rules are non-negotiable.** No claims about anything not visible in a screenshot; interaction-only qualities go in "not assessable".
3. **Severity is anchored to the user's goal**, not to the auditor's taste.
4. **No padding.** A framework that surfaces nothing gets no findings.
5. **The skill stays tool-agnostic** so it runs in Claude Code, Codex, and other Agent Skills hosts.

## Testing a change

1. Edit `SKILL.md` and/or `scripts/annotate.py`.
2. Regenerate the example screen: `cd examples && python3 make-example-mockup.py`.
3. Re-run the annotator: `python3 ../scripts/annotate.py annotations.json` and eyeball the output.
4. If you changed audit logic, run the skill against the example screenshots in your agent and sanity-check the report.

## Style

- British English in prose.
- Keep `SKILL.md` skimmable, tables and short lines over long paragraphs.
- Match the existing citation format (`Nielsen #5`, `WCAG 1.4.3`, `Hick's Law`).

PRs and issues both welcome. For larger changes, open an issue first to discuss direction.
