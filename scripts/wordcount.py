#!/usr/bin/env python3
"""Minimal word-count tool.

Usage:
    python3 scripts/wordcount.py <file>

Prints the number of lines, words and characters in the file, in that order,
separated by spaces. Lines and words are counted the way ``str.splitlines``
and ``str.split`` count them; characters are Unicode code points.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def count_text(text: str) -> tuple[int, int, int]:
    """Return the (lines, words, characters) counts for *text*."""
    return len(text.splitlines()), len(text.split()), len(text)


def count_file(path: Path) -> tuple[int, int, int]:
    """Return the (lines, words, characters) counts for the file at *path*."""
    return count_text(path.read_text(encoding="utf-8"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Print the line, word and character counts of a text file."
    )
    parser.add_argument("path", type=Path, help="path to the text file to analyse")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        lines, words, characters = count_file(args.path)
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"{lines} {words} {characters}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
