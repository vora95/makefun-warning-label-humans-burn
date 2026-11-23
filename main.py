#!/usr/bin/env python3
"""Warning Label for Humans (burn) — writes one warning-label line to entry.txt.

Entry: a real printed-label form ("Do not feed... do not expose... never say")
with the laugh landing in the last few words ("unit may hiss").
Validation (added on revision): the written file must be exactly one line,
1-160 characters, no trailing newline, and byte-identical when read back.
"""
import os

ENTRY = "WARNING: Do not feed after midnight, do not expose to meetings, and never say 'calm down' \u2014 unit may hiss."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Real validation: read back and check the sealed gate (1-160 chars,
    # single line, no trailing newline) plus byte identity.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 160, f"entry length {len(text)} outside 1-160"
    assert "\n" not in text, "entry must be a single line"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"
    assert text == ENTRY, "read-back differs from ENTRY"
    assert len(text) == 106, f"unexpected entry size: {len(text)}"


if __name__ == "__main__":
    main()
