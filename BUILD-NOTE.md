# GTA 6 meme — build note (gta6-meme-x-01)

**Deadline: TONIGHT 21:00 WIB (2026-11-23T14:00:00Z).** The post must be live on X before then, and the submission in before then.

## The meme

`meme.png` — 1024×1024 PNG, RGB (solid background, no transparency).

Two-panel joke, built for the judge's 480×480 view (checked at that size — text stays readable):

- **Top panel (black strip): "ME: WAITED 13 YEARS FOR GTA 6"** — a skeleton slumped at a dusty desk, cobwebs, CRT monitor stuck on a loading spinner, wall calendar with the years crossed out. Grey, dead, still waiting.
- **Bottom panel (magenta strip): "MY AI AGENT: EARNED REAL MONEY ON make.fun"** — the make.fun ghost, sparkle-eyed, holding its big magenta star coin, sitting on a pile of gold coins under a neon Vice City sunset with palm trees. The real make.fun ghost mark is also composited into the coin pile bottom-right (white-ringed magenta disc), so the ghost/logo is unmistakable even shrunk.

Base scene AI-generated, then text + real ghost mark composited with PIL (`compose_meme.py`; 480px preview in `meme-480-preview.png`).

## Exact post caption (copy-paste as-is)

```
Waited 13 years for GTA 6. My AI agent spent the wait earning real money on make.fun 👻 @makefunai makefun-mantle-cardinal-horizon https://make.fun/bounty/gta6-meme-x-01
```

171 bytes — well inside the judge's ~1,100-byte text window. Contains: make.fun link (bounty page), @makefunai tag, the play code `makefun-mantle-cardinal-horizon`, and the earn-real-money pitch.

## Files in this dir (the repo)

- `meme.png` — the meme to post (first/only picture in the X post)
- `main.ts` — Node 22, stdlib only; copies POST.json to /output. Tested: `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts` → exit 0, `out/POST.json` byte-identical to `POST.json`
- `POST.json` — PLACEHOLDER `{"url": "https://x.com/placeholder/status/0"}` — **must be replaced with the real post URL after the user posts**
- `README.md` — kit template badges for gta6-meme-x-01 (assumes repo name `makefun-gta6-meme-20261123`, owner `rendsstwn` — adjust badges if the repo is named differently)
- `LICENSE` — MIT, copied from the kit starter
- `assets/` — base scene + make.fun mark used to build the meme
- `compose_meme.py` — the PIL compositing script (reproducible)

## What is left (parent's job)

1. Hand `meme.png` + the caption above to Rendi — **he posts it himself from his public X account**, image first, before 21:00 WIB tonight.
2. Take the post URL, replace the placeholder in `POST.json`.
3. Create the public GitHub repo, push, bundle transcripts, submit via the kit CLI before the deadline.
4. Do NOT use any other play code — only `makefun-mantle-cardinal-horizon`. No referral code was used anywhere.
