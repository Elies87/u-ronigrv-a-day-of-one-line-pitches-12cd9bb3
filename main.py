#!/usr/bin/env python3
"""One-line pitch entry for make.fun - "A Day of One-Line Pitches".

Writes a single original sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, no input, no network access.
"""

import os

SENTENCE = (
    "Just tell make.fun your app idea in plain words and its AI agent "
    "builds it for you - no code, no setup, no experience needed - "
    "turning the idea you have been carrying around into a real app you "
    "can use and share today."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
