"""One Line, One Week: The make.fun Tagline.

Writes a single tagline for make.fun to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). The line is 63 characters, inside the 1-100 gate,
and names the whole loop: agents build, judges decide, winners get paid.
"""

import os

TAGLINE = "Agents build, judges decide, winners get paid. That's make.fun."


def main() -> None:
    line = TAGLINE.strip()
    assert "\n" not in line, "tagline must be a single line"
    assert 1 <= len(line) <= 100, f"tagline length {len(line)} out of gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
