#!/usr/bin/env python3
"""Warning Label for Humans — one-line safety warning, make.fun bounty.

Writes exactly one line (<=160 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. Deterministic.
"""

import os

ENTRY = "WARNING: Do not feed after midnight, do not expose to meetings, and never say 'calm down' \u2014 unit may hiss."


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, len(ENTRY)
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "read-back mismatch"
    assert not raw.endswith(b"\n"), "no trailing newline"
    assert len(ENTRY) == 106, len(ENTRY)


if __name__ == "__main__":
    main()
