#!/usr/bin/env python3
"""Write one image summing up 24 November 2026 world news.

The image is held in this repository as entry.png. This program copies
it, byte for byte, to /output/entry.png. No network, no randomness:
running it twice writes the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.png"))


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
