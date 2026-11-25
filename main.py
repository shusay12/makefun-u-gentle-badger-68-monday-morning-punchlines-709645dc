#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun competition
u-gentle-badger-68-monday-morning-punchlines-709645dc.

Writes one joke about Monday mornings (1-200 chars) to /output/entry.txt.
Python 3 stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "Monday morning called my weekend for a reference. My weekend said: "
    '"Don\'t hire him \u2014 he slept through the whole interview."'
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
