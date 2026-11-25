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

MAX_CHARS = 280


def main() -> None:
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise ValueError(f"joke must be 1-{MAX_CHARS} characters, got {len(JOKE)}")
    if JOKE != JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke must be a single line with no leading/trailing space")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
