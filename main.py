#!/usr/bin/env python3
"""The Funniest Toaster Error Message entry.

Writes one original funny toaster error message (at most 120 chars)
to /output/entry.txt, deterministically: same bytes on every run.
"""
import os
import sys

LINE = "E-09: Slot 2 contains a fork. I am not insured for this."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 120:
        print(f"entry must be 1-120 characters, got {len(LINE)}", file=sys.stderr)
        sys.exit(1)
    if LINE.strip() == "":
        print("entry must not be only whitespace", file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify the written bytes match the entry exactly.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        print("entry.txt does not match the entry text", file=sys.stderr)
        sys.exit(1)
    print(f"entry.txt: {len(LINE.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
