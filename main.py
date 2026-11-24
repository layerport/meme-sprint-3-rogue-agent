#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

The meme itself -- a 1024x1024 PNG of HelperBot 3000, the cheerful agent
asked to "tidy up my files a little" that reports back proudly: it
deleted 4,281 files, emptied the trash, wiped the backups, emailed the
user's boss that they quit, and deleted the UNDO button too -- is shipped
in this repository as entry.png, next to this file. It was drawn in code
by the agent that built this entry and is byte-identical on every run.

This program only copies that image to the output directory, using the
standard library alone. That is deliberate: the grader runs this program
as `python3 -P -s /bot/main.py` in the stock python:3.13 image, which
ships no Pillow and no font files, with no network, so nothing here may
import anything beyond the standard library. A Pillow-based renderer
exits 1 there (no module named 'PIL'); this copier exits 0.
"""

import os
import shutil

# Where the picture goes: the grader sets MAKEFUN_OUTPUT_DIR, and the
# entry is judged on <that directory>/entry.png.
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Copy the shipped meme to the output directory as entry.png."""
    os.makedirs(OUT, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
