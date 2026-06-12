#!/usr/bin/env python3
"""Generate the neutral example screens used in the README and example report.

A deliberately-flawed two-step journey for a fictional product ("Lumen"), so the
example audit has real, visible issues to cite — including cross-screen ones.
Run:  python3 make-example-mockup.py
Output: assets/signup.png, assets/verify-email.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 750, 1010
HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

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


def new_card():
    img = Image.new("RGB", (W, H), "#F4F5F7")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([40, 80, 710, 960], radius=32, fill="white")
    # Brand mark (identical on both screens — consistency)
    d.ellipse([349, 150, 401, 202], fill=PURPLE)
    centre(d, 375, 222, "Lumen", font(34, bold=True), INK)
    return img, d


def build_signup():
    img, d = new_card()

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

    img.save(os.path.join(ASSETS, "signup.png"))
    print(os.path.join(ASSETS, "signup.png"))


def build_verify():
    img, d = new_card()

    # Envelope icon
    d.rounded_rectangle([320, 300, 430, 376], radius=8, outline=PURPLE, width=4)
    d.line([322, 308, 375, 346], fill=PURPLE, width=4)
    d.line([375, 346, 428, 308], fill=PURPLE, width=4)

    centre(d, 375, 410, "Check your email", font(40, bold=True), INK)

    # Body — never names the address the link was sent to
    centre(d, 375, 470, "We've sent a verification link to", font(24), GREY)
    centre(d, 375, 502, "your inbox. Open it to continue.", font(24), GREY)

    # Primary action — restyled vs screen 1 (filled there, outline here = pattern drift)
    d.rounded_rectangle([195, 580, 555, 650], radius=14, outline=PURPLE, width=3, fill="white")
    centre(d, 375, 601, "Open email app", font(24, bold=True), PURPLE)

    # (Deliberately: no resend, no change-email, no help — the empty region below)

    img.save(os.path.join(ASSETS, "verify-email.png"))
    print(os.path.join(ASSETS, "verify-email.png"))


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    build_signup()
    build_verify()
