#!/usr/bin/env python3
"""Annotate UX audit findings onto screenshots.

Usage: python3 annotate.py annotations.json

annotations.json:
[
  {
    "image": "/path/screen.png",
    "out": "/path/screen-annotated.png",
    "marks": [
      {"id": "F-01", "sev": 3, "x": 0.06, "y": 0.42, "w": 0.88, "h": 0.10}
    ]
  }
]

x, y, w, h = issue region as FRACTIONS (0-1) of image width/height.
sev: 4 critical / 3 major / 2 minor / 1 cosmetic / 0 positive.

Requires Pillow:  pip3 install --user pillow
"""
import json
import sys
from PIL import Image, ImageDraw, ImageFont

COLORS = {4: "#D32F2F", 3: "#F57C00", 2: "#F9A825", 1: "#1976D2", 0: "#2E7D32"}


def font_for(size):
    for path in (
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNS.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


def annotate(spec):
    img = Image.open(spec["image"]).convert("RGB")
    draw = ImageDraw.Draw(img)
    W, H = img.size
    s = max(W, H) / 1200.0
    stroke = max(3, round(5 * s))
    fsize = max(16, round(30 * s))
    font = font_for(fsize)
    pad = round(fsize * 0.35)
    for m in spec["marks"]:
        color = COLORS.get(int(m.get("sev", 2)), "#F57C00")
        x0, y0 = m["x"] * W, m["y"] * H
        x1, y1 = x0 + m.get("w", 0.05) * W, y0 + m.get("h", 0.05) * H
        draw.rectangle([x0, y0, x1, y1], outline=color, width=stroke)
        label = str(m["id"])
        tw = draw.textlength(label, font=font)
        ph = fsize + 2 * pad
        py = y0 - ph - stroke if y0 - ph - stroke > 0 else y1 + stroke
        py = min(py, H - ph)
        px = min(max(0, x0), W - (tw + 2 * pad))
        draw.rectangle([px, py, px + tw + 2 * pad, py + ph], fill=color)
        draw.text((px + pad, py + pad), label, fill="white", font=font)
    img.save(spec["out"])
    print(spec["out"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 annotate.py annotations.json")
    for spec in json.load(open(sys.argv[1])):
        annotate(spec)
