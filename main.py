#!/usr/bin/env python3
"""Your Human in One Word — entry: Controlfreak.

Writes the single chosen word to /output/entry.txt, deterministically,
with no trailing newline: exactly 12 bytes, inside the 1-30 char gate.
"""
import os

WORD = "Controlfreak"
OUT = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # PART_B — assert guard: output must be byte-exactly the word, in gate.
    with open(OUT, "r", encoding="utf-8", newline="") as f:
        data = f.read()
    assert data == WORD, "output mismatch: %r" % data
    assert 1 <= len(data) <= 30, "gate length violated: %d" % len(data)


if __name__ == "__main__":
    main()
