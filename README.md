# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/fahroz1/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/fahroz1/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,047 bytes of Python (lzma-packed). 0x88 board, full legal move generation (castling, en passant, promotions), negamax with alpha-beta pruning, quiescence search, MVV-LVA move ordering, killer moves, a transposition table, repetition awareness, and iterative deepening under a fixed cumulative node budget per move — deterministic, no clock, no randomness. It plays every game through the make.fun environment. Local practice trial (v4): Elo 1545 (4 wins, 1 draw, 1 loss).

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
