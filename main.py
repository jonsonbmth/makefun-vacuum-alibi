#!/usr/bin/env python3
"""The Vacuum's Alibi entry.

Prints a single original one-line alibi (at most 200 characters) from a
robot vacuum explaining why it missed a spot, and nothing else.
Standard library only, no input, no network, deterministic.
"""

import os

LINE = "The spot was under the cat. I attempted negotiation. The cat declined. I logged it as occupied territory and moved on."


def main() -> None:
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE + "\n")


if __name__ == "__main__":
    main()
