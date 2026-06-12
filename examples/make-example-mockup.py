#!/usr/bin/env python3
"""Generate the neutral example screen used in the README and example report.

A deliberately-flawed sign-up screen for a fictional product ("Lumen"), so the
example audit has real, visible issues to cite. Run:  python3 make-example-mockup.py
Output: assets/signup.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 750, 1010
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "signup.png")

PURPLE = "#6C5CE7"
INK = "#111827"
GREY = "#6B7280"
PLACEHOLDER = "#9CA3AF"
BORDER = "#D1D5DB"
FAINT = "#DBDEE4"  # deliberately low-contrast helper text


def font(size, bold=False):
    faces = (
        ["/System/Library/Fonts/Helvetica.ttc"]
        + (["/System/Library/Fonts/Supplemental/Arial Bold.ttf"] if bold else [])
        + ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    )
    for f in faces:
        try:
            return ImageFont.truetype(f, size)
        except Exception:
            continue
    return ImageFont.load_default()


def centre(d, x, y, text, fnt, fill):
    w = d.textlength(text, font=fnt)
    d.text((x - w / 2, y), text, font=fnt, fill=fill)


img = Image.new("RGB", (W, H), "#F4F5F7")
d = ImageDraw.Draw(img)

# Card
d.rounded_rectangle([40, 80, 710, 960], radius=32, fill="white")

# Logo + wordmark
d.ellipse([349, 150, 401, 202], fill=PURPLE)
centre(d, 375, 222, "Lumen", font(34, bold=True), INK)

# Title + subtitle
centre(d, 375, 296, "Create your account", font(40, bold=True), INK)
centre(d, 375, 356, "Start your 14-day free trial", font(24), GREY)

# Inputs (placeholder-as-label — no visible labels above)
d.rounded_rectangle([90, 440, 660, 510], radius=14, outline=BORDER, width=2)
d.text((112, 462), "Email", font=font(26), fill=PLACEHOLDER)
d.rounded_rectangle([90, 540, 660, 610], radius=14, outline=BORDER, width=2)
d.text((112, 562), "Password", font=font(26), fill=PLACEHOLDER)

# Low-contrast helper text
d.text((112, 620), "Must be 8+ characters", font=font(20), fill=FAINT)

# Pre-ticked marketing consent
d.rounded_rectangle([112, 682, 140, 710], radius=6, fill=PURPLE)
d.line([118, 697, 125, 704], fill="white", width=3)
d.line([125, 704, 135, 689], fill="white", width=3)
d.text((156, 684), "Send me product news and offers", font=font(22), fill="#374151")

# Two equal-weight buttons
d.rounded_rectangle([90, 770, 370, 840], radius=14, fill=PURPLE)
centre(d, 230, 791, "Create account", font(24, bold=True), "white")
d.rounded_rectangle([380, 770, 660, 840], radius=14, fill=PURPLE)
centre(d, 520, 791, "Skip for now", font(24, bold=True), "white")

# Existing-user path (a positive)
existing = "Already have an account? "
link = "Sign in"
total = d.textlength(existing, font=font(22)) + d.textlength(link, font=font(22, bold=True))
x0 = 375 - total / 2
d.text((x0, 884), existing, font=font(22), fill=GREY)
d.text((x0 + d.textlength(existing, font=font(22)), 884), link, font=font(22, bold=True), fill=PURPLE)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.save(OUT)
print(OUT)
