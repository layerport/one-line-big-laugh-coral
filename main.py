#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry (program/v1, Python 3.13, stdlib only).

Writes a single original one-liner to /output/entry.txt. The line is a
fixed constant, so every run produces byte-identical output.
"""

from pathlib import Path

LINE = "I asked AI to write my wedding vows; it left me at the altar for a newer model."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of bounds"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
