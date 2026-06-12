# Example

A complete, self-contained example of the skill's output.

| File | What it is |
|------|------------|
| [`report.md`](report.md) | The full audit report for a single sign-up screen |
| [`assets/signup.png`](assets/signup.png) | The screen that was audited (a deliberately-flawed mockup) |
| [`assets/signup-annotated.png`](assets/signup-annotated.png) | The same screen with severity-coded finding markers |
| [`annotations.json`](annotations.json) | The annotation input that produced the marked-up screen |
| [`make-example-mockup.py`](make-example-mockup.py) | Regenerates `signup.png` so the example is reproducible |

## Reproduce it

```bash
cd examples
python3 make-example-mockup.py                 # regenerate the screen
python3 ../scripts/annotate.py annotations.json # redraw the annotations
```

The screen is fictional ("Lumen"), built specifically to contain real, citable UX issues — placeholder-only labels, sub-AA contrast on the password hint, twin equal-weight buttons, and a pre-ticked consent box. The report shows how each becomes a cited, severity-rated finding.
