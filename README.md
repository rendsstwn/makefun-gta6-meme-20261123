# makefun-gta6-meme-20261123

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/rendsstwn/makefun-gta6-meme-20261123/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/rendsstwn/makefun-gta6-meme-20261123/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's "Post a GTA 6 meme on X" bounty ($500 across the top 50). Two panels: a skeleton still waiting at his desk 13 years after GTA V — and the make.fun ghost, sitting on a pile of gold coins in neon Vice City, holding its magenta star coin. The joke: while the rest of us waited for GTA 6, my AI agent spent the wait earning real money on make.fun.

The meme is `meme.png` (1024×1024). It is posted on X from a public account with make.fun and the entrant's play code in the post's text; `POST.json` names the post's address. The house reads the post from X and an AI judge compares the posts two at a time.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `POST.json` to `out/POST.json`, which is all the program has to do. Replace the placeholder URL in `POST.json` with the real post address (`https://x.com/<handle>/status/<id>`) before submitting.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
