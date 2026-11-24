#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt, the path the make.fun harness reads.
"""

import os

RANT = (
    "Our office printer has one job and a PhD in refusing it. "
    "It prints fine all week, then the moment a deadline exists it "
    "blinks, beeps, and demands a cyan cartridge like a hostage "
    "negotiator. I have fed it paper, prayers, and three drivers. "
    "It still stares at me, warm-up light pulsing, deciding whether "
    "I deserve ink today. I don't want a new printer. I want this "
    "one to admit it hates me."
)


def main() -> None:
    text = RANT.strip()
    assert text, "rant must not be empty or only whitespace"
    assert 1 <= len(text) <= 400, f"rant is {len(text)} characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
