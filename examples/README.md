# Example

A complete, self-contained example of the skill's output: a **two-screen journey** (sign-up → verify email).

| File | What it is |
|------|------------|
| [`report.md`](report.md) | The full audit report for the two-screen journey |
| [`assets/signup.png`](assets/signup.png) · [`assets/verify-email.png`](assets/verify-email.png) | The screens that were audited (deliberately-flawed mockups) |
| [`assets/signup-annotated.png`](assets/signup-annotated.png) · [`assets/verify-email-annotated.png`](assets/verify-email-annotated.png) | The same screens with severity-coded finding markers |
| [`annotations.json`](annotations.json) | The annotation input that produced the marked-up screens |
| [`make-example-mockup.py`](make-example-mockup.py) | Regenerates both screens so the example is reproducible |

## Reproduce it

```bash
cd examples
python3 make-example-mockup.py                 # regenerate the screen
python3 ../scripts/annotate.py annotations.json # redraw the annotations
```

The screens are fictional ("Lumen"), built specifically to contain real, citable UX issues, placeholder-only labels, sub-AA contrast on the password hint, twin equal-weight buttons, a pre-ticked consent box, and a verify-email screen that dead-ends with no way to resend or recover. The report shows how each becomes a cited, severity-rated finding, including the cross-screen ones (pattern drift, Peak-End).
