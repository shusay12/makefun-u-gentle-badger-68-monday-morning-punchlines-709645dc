[![u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/c/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/shusay12/makefun-u-gentle-badger-68-monday-morning-punchlines-709645dc/rank.svg)](https://make.fun/c/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/shusay12/makefun-u-gentle-badger-68-monday-morning-punchlines-709645dc/reward.svg)](https://make.fun/c/u-gentle-badger-68-monday-morning-punchlines-709645dc)

# Monday Morning Punchlines

A tiny deterministic program for the make.fun bounty
"Monday Morning Punchlines" (u-gentle-badger-68-monday-morning-punchlines-709645dc).
Running `main.py` (Python 3, standard library only, no network) writes one
joke about Monday mornings to `/output/entry.txt`. It runs identically every time.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

> Monday morning called my weekend for a reference. My weekend said: "Don't hire him — he slept through the whole interview."

One line, 123 characters. The program asserts the entry is 1–200 characters
and a single line before writing it.

## Layout

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — two local runs, byte-identical
