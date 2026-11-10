"""Tests for scripts/wordcount.py."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "wordcount.py"


def run_wordcount(path: Path) -> str:
    """Run the CLI on *path* and return its stdout."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def test_empty_file(tmp_path: Path) -> None:
    empty = tmp_path / "empty.txt"
    empty.write_text("", encoding="utf-8")

    assert run_wordcount(empty) == "0 0 0\n"


def test_normal_text(tmp_path: Path) -> None:
    sample = tmp_path / "sample.txt"
    sample.write_text("hello world\nsecond line here\n", encoding="utf-8")

    assert run_wordcount(sample) == "2 5 29\n"
