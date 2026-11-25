"""Write one excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic by design: the entry is a fixed string. This program reads no
clock, no randomness, no network and no files, so every run produces the
exact same bytes.

The file holds the entry plus one trailing newline. The line itself is 139
characters, so even counting the newline it stays well inside the gate's
1-200 character window.
"""

import os

ENTRY = (
    "Sorry about the bug \u2014 I wrote it, the compiler compiled it "
    "without a single complaint, so as far as I'm concerned, "
    "the compiler started it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
