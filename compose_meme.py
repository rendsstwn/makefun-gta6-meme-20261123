#!/usr/bin/env python3
"""Compose the GTA 6 meme: two-panel base scene + caption strips + real make.fun ghost mark."""
from PIL import Image, ImageDraw, ImageFont
import os

ENTRY = os.path.expanduser("~/workspace/makefun/gta6-meme-entry")
BASE = os.path.join(ENTRY, "assets", "media-generation-base-scene-0-3c0cd252-9258-465f-8df5-d79fba9f4eb8.png")
MARK = os.path.join(ENTRY, "assets", "mark-1024.png")
OUT = os.path.join(ENTRY, "meme.png")
PREVIEW = os.path.join(ENTRY, "meme-480-preview.png")

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def fit_font(draw, text, max_w, start_size):
    size = start_size
    while size > 12:
        f = ImageFont.truetype(BOLD, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(BOLD, 12)

base = Image.open(BASE).convert("RGB")
W, H = base.size
print("base size:", W, H)

# Locate the white horizontal divider between the two panels (scan middle band).
import numpy as np
arr = np.asarray(base.convert("L"))
divider = None
for y in range(int(H * 0.45), int(H * 0.60)):
    row = arr[y]
    if (row > 235).mean() > 0.9:
        divider = y
        break
print("divider row:", divider)
# Panel interiors: inside the black frames (frame ~4-6px).
p1 = base.crop((8, 8, W - 8, divider - 6))
p2 = base.crop((8, divider + 6, W - 8, H - 8))
print("panel crops:", p1.size, p2.size)

S1, S2 = 92, 118            # strip heights
P1H = 408                    # panel 1 height
P2H = 1024 - S1 - P1H - S2  # panel 2 height = 406
print("layout: strip1", S1, "panel1", P1H, "strip2", S2, "panel2", P2H)

final = Image.new("RGB", (1024, 1024), (0, 0, 0))
d = ImageDraw.Draw(final)

# Strip 1: black, white bold text.
d.rectangle([0, 0, 1024, S1], fill=(0, 0, 0))
f1 = fit_font(d, "ME: WAITED 13 YEARS FOR GTA 6", 980, 58)
d.text((512, S1 // 2), "ME: WAITED 13 YEARS FOR GTA 6", font=f1,
       fill=(255, 255, 255), anchor="mm")

# Panel 1.
final.paste(p1.resize((1024, P1H), Image.LANCZOS), (0, S1))

# Strip 2: make.fun magenta, two lines.
MAGENTA = (200, 16, 107)
y2 = S1 + P1H
d.rectangle([0, y2, 1024, y2 + S2], fill=MAGENTA)
f2a = fit_font(d, "MY AI AGENT:", 980, 56)
d.text((512, y2 + 32), "MY AI AGENT:", font=f2a, fill=(255, 255, 255), anchor="mm")
f2b = fit_font(d, "EARNED REAL MONEY ON make.fun", 980, 48)
d.text((512, y2 + 84), "EARNED REAL MONEY ON make.fun", font=f2b,
       fill=(255, 255, 255), anchor="mm")

# Panel 2.
final.paste(p2.resize((1024, P2H), Image.LANCZOS), (0, y2 + S2))

# Real make.fun ghost mark, nestled into the coin pile bottom-right like a big coin.
mark = Image.open(MARK).convert("RGBA")
MS = 150
mark = mark.resize((MS, MS), Image.LANCZOS)
mx, my = 1024 - MS - 22, 1024 - MS - 22
# White ring behind for pop against the gold coins.
ring = Image.new("RGBA", (MS + 12, MS + 12), (0, 0, 0, 0))
rd = ImageDraw.Draw(ring)
rd.ellipse([0, 0, MS + 11, MS + 11], fill=(255, 255, 255, 255))
final.paste(ring, (mx - 6, my - 6), ring)
final.paste(mark, (mx, my), mark)

# Thin black outer frame.
d.rectangle([0, 0, 1023, 1023], outline=(0, 0, 0), width=6)
# Divider lines between strips and panels.
d.line([0, S1, 1024, S1], fill=(255, 255, 255), width=4)
d.line([0, y2, 1024, y2], fill=(255, 255, 255), width=4)
d.line([0, y2 + S2, 1024, y2 + S2], fill=(255, 255, 255), width=4)

final.save(OUT, "PNG")
final.resize((480, 480), Image.LANCZOS).save(PREVIEW, "PNG")
print("saved", OUT, os.path.getsize(OUT), "bytes")
print("saved", PREVIEW)
