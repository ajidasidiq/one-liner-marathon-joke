#!/usr/bin/env python3
"""One-Liner Marathon entry: write a single original one-line comedy joke
to /output/entry.txt.

The joke is a deadpan one-liner with a surprise turn: a GPS asked a
philosophical question answers the only way a GPS ever answers.
"""

import os

JOKE = (
    "I asked my GPS for the meaning of life. It said 'recalculating' "
    "- which is honestly the most accurate answer I've ever gotten."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
