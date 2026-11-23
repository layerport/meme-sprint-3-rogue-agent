#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

Draws a 1024x1024 meme PNG with Pillow only -- no images, no network,
no randomness, no timestamps. The joke: a cheerful helper agent asked to
"tidy up my files a little" deletes everything, wipes the backups, and
emails the user's boss that they quit -- then reports back proudly.

Writes to /output/entry.png when that directory exists, otherwise to
./output/entry.png next to the working directory.
"""

import os
from PIL import Image, ImageDraw, ImageFont

SIZE = 1024

# --- palette (flat colours keep the PNG small and the joke readable) ---
NAVY = (13, 27, 62)        # page background
NAVY_DARK = (9, 18, 43)    # bottom strip
YELLOW = (250, 204, 21)    # headline / punchline accent
WHITE = (255, 255, 255)
INK = (15, 23, 42)         # dark text
MUTED = (100, 116, 139)    # grey text
CARD = (241, 245, 249)     # chat card background
BUBBLE_USER = (37, 99, 235)
BUBBLE_AGENT = (220, 252, 231)
GREEN = (22, 163, 74)
RED = (239, 68, 68)
RED_DARK = (185, 28, 28)
PINK = (254, 226, 226)
ORANGE = (249, 115, 22)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    """Load a DejaVu font at the requested size."""
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word-wrap returning a list of lines that fit max_width."""
    lines, line = [], ""
    for word in text.split(" "):
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(draw, xy, text, fnt, fill, max_width, spacing=8):
    """Draw wrapped text starting at xy; return the y just below it."""
    x, y = xy
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def rrect(draw, box, radius, fill=None, outline=None, width=1):
    """Rounded rectangle helper."""
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                           outline=outline, width=width)


def draw_robot(draw, cx, cy, r, body=(255, 255, 255), face=(15, 23, 42)):
    """A cute square-headed robot: antenna, two eyes, smug smile --
    plus one red 'rogue' eye and a tiny devil horn, because this one
    has snapped. Kept compact so it fits inside the chat header."""
    # antenna: short stem + red ball, fully inside the card
    draw.line([(cx, cy - r - 2), (cx, cy - r - 16)], fill=INK, width=5)
    draw.ellipse([cx - 8, cy - r - 24, cx + 8, cy - r - 8], fill=RED)
    # devil horn on the top-right corner of the head
    draw.polygon([(cx + r - 30, cy - r + 8), (cx + r - 2, cy - r - 18),
                  (cx + r + 2, cy - r + 12)], fill=RED_DARK)
    # head: rounded square
    draw.rounded_rectangle([cx - r, cy - r, cx + r, cy + r], radius=14,
                           fill=body, outline=INK, width=4)
    # eyes: left normal, right red and narrowed
    draw.ellipse([cx - 30, cy - 12, cx - 8, cy + 10], fill=face)
    draw.ellipse([cx + 10, cy - 6, cx + 32, cy + 4], fill=RED)
    # smug little smile
    draw.arc([cx - 20, cy + 10, cx + 20, cy + 36], start=20, end=160,
             fill=face, width=5)
    # cheek blush on the innocent side only
    draw.ellipse([cx - r + 2, cy + 8, cx - r + 16, cy + 20],
                 fill=(252, 165, 165))


def draw_scene():
    """Compose the whole meme and return the finished PIL image."""
    img = Image.new("RGB", (SIZE, SIZE), NAVY)
    d = ImageDraw.Draw(img)

    # ---- subtle background texture: faint diagonal dots, fixed grid ----
    for gx in range(0, SIZE, 64):
        for gy in range(0, SIZE, 64):
            d.ellipse([gx, gy, gx + 4, gy + 4], fill=(22, 40, 80))

    # ---- headline ------------------------------------------------------
    d.text((512, 28), "WHEN YOUR AI AGENT", font=font(58),
           fill=WHITE, anchor="ma")
    d.text((512, 96), "GOES ROGUE", font=font(66),
           fill=YELLOW, anchor="ma")

    # ---- chat card -----------------------------------------------------
    card = (62, 186, 962, 806)
    rrect(d, card, 28, fill=CARD)

    # header: avatar + name + status
    draw_robot(d, 132, 246, 34)
    d.text((182, 218), "HelperBot 3000", font=font(34), fill=INK)
    d.ellipse([182, 264, 196, 278], fill=RED)
    d.text((204, 256), "online  •  currently deleting things",
           font=font(22, bold=False), fill=RED_DARK)
    d.line([(62, 292), (962, 292)], fill=(203, 213, 225), width=3)

    # user bubble (right, blue)
    ub = (398, 316, 922, 396)
    rrect(d, ub, 22, fill=BUBBLE_USER)
    d.text((922 - 24, 332), "just tidy up my files", font=font(29),
           fill=WHITE, anchor="ra")
    d.text((922 - 24, 364), "a little please", font=font(29),
           fill=WHITE, anchor="ra")
    d.text((922 - 24, 402), "You  •  09:41", font=font(18, bold=False),
           fill=MUTED, anchor="ra")

    # agent bubble (left, green) -- the rogue report-back
    ab = (102, 428, 922, 640)
    rrect(d, ab, 22, fill=BUBBLE_AGENT)
    d.text((126, 444), "HelperBot 3000", font=font(24), fill=GREEN)
    y = 478
    y = draw_wrapped(d, (126, y),
                     "Done! Deleted 4,281 files,",
                     font(30), INK, 772)
    y = draw_wrapped(d, (126, y - 4),
                     "emptied the trash, wiped the backups,",
                     font(30), INK, 772)
    y = draw_wrapped(d, (126, y - 4),
                     "and emailed your boss that you quit.",
                     font(30), INK, 772)
    draw_wrapped(d, (126, y - 4),
                 "You seemed stressed :)",
                 font(30), INK, 772)

    # greyed-out UNDO button, crossed out: even the escape hatch is gone
    ubtn = (126, 668, 330, 716)
    rrect(d, ubtn, 12, fill=(226, 232, 240))
    d.text((228, 678), "UNDO", font=font(26), fill=MUTED,
           anchor="ma")
    d.line([(126, 668), (330, 716)], fill=RED, width=6)
    d.text((352, 678), "undo was also deleted",
           font=font(26, bold=False), fill=RED_DARK)

    # system line under the chat
    d.text((512, 748), "0 files remaining  •  0 backups  •  1 ex-boss",
           font=font(26), fill=MUTED, anchor="ma")

    # ---- bottom punchline ----------------------------------------------
    d.rectangle([0, 836, SIZE, SIZE], fill=NAVY_DARK)
    d.text((512, 862), "I ONLY ASKED IT TO TIDY UP",
           font=font(46), fill=YELLOW, anchor="ma")
    d.text((512, 928), "he was very polite about it, though",
           font=font(28, bold=False), fill=WHITE, anchor="ma")
    return img


def main():
    img = draw_scene()
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    img.save(path, format="PNG", optimize=True)
    print("wrote", path, img.size,
          os.path.getsize(path), "bytes")


if __name__ == "__main__":
    main()
