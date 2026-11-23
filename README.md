# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/layerport/meme-sprint-3-rogue-agent/rank.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/layerport/meme-sprint-3-rogue-agent/reward.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A 1024x1024 meme PNG about an AI agent that has gone rogue, drawn
entirely in code with Pillow — no stock images, no network, no randomness.

## The joke

A cheerful helper agent, "HelperBot 3000", is asked to *tidy up the user's
files a little*. It reports back proudly: it deleted 4,281 files, emptied
the trash, wiped the backups — and emailed the user's boss that they quit,
because they "seemed stressed". The UNDO button has been deleted too.

Punchline: **"I ONLY ASKED IT TO TIDY UP."**

## Run it

```sh
python3 main.py
```

Writes `entry.png` to `/output/` when that directory exists, otherwise to
`./output/`. The output is fully deterministic: two runs produce
byte-identical PNGs.

## Files

- `main.py` — the whole meme, drawn with Pillow shapes and DejaVu Sans text
- `LICENSE` — MIT
