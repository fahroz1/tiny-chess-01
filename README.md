# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/fahroz1/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/fahroz1/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 3,252 bytes of Python (lzma-packed by the make.fun kit from a 7,622-byte readable source). 0x88 board, full legal move generation (castling, en passant, promotions), negamax with alpha-beta pruning, quiescence search, MVV-LVA move ordering, killer moves, a transposition table, repetition awareness, and iterative deepening under a fixed cumulative node budget per move — deterministic, no clock, no randomness. It plays every game through the make.fun environment.

## Engine v4

The v4 rewrite fixes the round-1 crash (a stale en passant square leaking through search recursion could delete a king) and strengthens play: a bigger node budget, piece-square tables, mobility and king-safety terms in the evaluation, and repetition handling that turns dead draws into held points instead of losses.

Local practice trial (v4): **Elo 1545 — 4 wins, 1 draw, 1 loss** across the six-game practice set (depth-2, depth-3, depth-4, nodes-100k, nodes-250k, nodes-500k opponents). The practice floor is Elo 1154.

## How the pack works

`main.py` is not hand-written: it is the kit's lzma-packed form of the readable source, produced by `makefun compress`. The stub decompresses the engine in memory and runs it, so the entry on disk stays under the 4,096-byte file cap while the engine itself is a full-featured search. The readable source is bundled beside the transcripts for the thinking-reproduction checks.

## Run it

```sh
MAKEFUN_ENV_URL=<env-url> python3 -P -s main.py
```

Or grade it locally with the competition kit:

```sh
node cli/makefun.mjs grade-local --kit . --bot . --driver process
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
