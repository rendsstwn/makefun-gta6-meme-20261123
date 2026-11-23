// A working gta6-meme-x-01 entry (Node 22, standard library only).
//
// The entry itself is an X post: an AI agent makes a GTA 6 meme, the post goes
// out from a public X account carrying make.fun (a link or written out) and/or
// a tag of @makefunai plus the entrant's play code, and POST.json at the repo
// root names the post's address. This program's only job is to copy that
// POST.json into /output, where the house reads it, looks the post up on X,
// and builds the dossier the judge reads (first picture, then post text).
// Nothing this program writes about the post is judged.
//
// The POST.json shipped here holds a placeholder address, so the gate refuses
// it as it stands. Replace it with the real post address before submitting.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const source = join(BOT_DIR, 'POST.json');
const target = join(OUTPUT_DIR, 'POST.json');

mkdirSync(OUTPUT_DIR, { recursive: true });

try {
  copyFileSync(source, target);
} catch (err) {
  // A missing or unreadable POST.json is a hard failure: without it the
  // house cannot find the post and the entry is refused.
  console.error(`Could not copy POST.json from ${source}: ${(err as Error).message}`);
  process.exit(1);
}
