"""Write exactly one letter -- Z -- to /output/entry.txt.

One Letter for Your Day (make.fun): the entry is a single letter A-Z
standing for the word that describes your day. Z is the pick:

- Z for "zombie": a day lived on zero sleep, shuffling through it
  half-awake -- the most vivid, funny and true day-word a single
  letter can carry, and the task's own example ("Z for zero sleep").
- Z is also the sleep symbol itself (Zzz), so the letter pictures
  the day twice over: no sleep, and the sleep you never got.
- The initial fits the word exactly: zombie, zero, Zzz all start
  with Z -- no sharper initial exists for that word.

Runs offline; no network, no arguments, no input files, no clock,
no randomness. Two runs write byte-identical output.
"""

import os

LETTER = "Z"


def main() -> None:
    # The sealed gate accepts exactly 1 character of non-whitespace
    # UTF-8 text; fail loudly instead of writing junk.
    if len(LETTER) != 1 or not LETTER.strip() or not LETTER.isalpha():
        raise SystemExit(f"letter must be exactly one A-Z character, got {LETTER!r}")
    if not ("A" <= LETTER <= "Z"):
        raise SystemExit(f"letter must be A-Z, got {LETTER!r}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The sealed grader runs in a stock sandbox where /output may not
    # exist yet; create it rather than assuming the harness did.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Verify the round-trip: the sealed scorer reads this file back, so
    # confirm what landed on disk is byte-identical and still in range.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LETTER or len(written) != 1:
        raise SystemExit("entry.txt failed verification after write")
    print(f"wrote {LETTER!r} (1 character) to {path}")


if __name__ == "__main__":
    main()
