"""Make the Judge Smile, variant 6 (final entry).

Writes one line, at most 200 characters, about a small good thing
that happened today, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line: you drop your last coin under the bus seat and Rizky, the
schoolboy across the aisle, fishes it out with a magnet on a string,
then waves off your thanks because the magnet does all the work.
Second person, opened mid-moment, one named person and one concrete
gadget, surprise turn landing in the last words.
"""

import os
from pathlib import Path

ENTRY = (
    "You dropped your last coin under the bus seat and Rizky, the "
    "schoolboy across the aisle, fished it out with a magnet on a "
    "string and waved off your thanks, saying the magnet does all "
    "the work."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert text, "entry must not be empty or only whitespace"
    assert text == ENTRY, "entry must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    target = output_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    assert written == text + "\n", "written file does not match entry"
    assert 1 <= len(written.strip()) <= 200, "written entry fails gate"


if __name__ == "__main__":
    main()
