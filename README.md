# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/fahroz1/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/fahroz1/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in exactly 4,096 bytes of Python. 0x88 board, full legal move generation (castling, en passant, promotions), negamax with alpha-beta pruning, quiescence search, MVV-LVA move ordering, and iterative deepening under a fixed node budget — deterministic, no clock, no randomness. It plays every game through the make.fun environment.

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
