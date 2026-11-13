"""Cutest picture entry for make.fun.

This program copies a picture of a cute kitten to the contest output
directory. The result is a byte-exact copy of the file picture.jpg. The
output file is still named entry.png; its format is recognised from its
leading bytes, as the contest rules allow, and the plain copy is
deterministic: two runs write identical bytes.
"""

import hashlib
import os
import shutil
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = Path(__file__).resolve().parent / "picture.jpg"
DST = Path(OUTPUT_DIR) / "entry.png"


def main():
    shutil.copyfile(SRC, DST)
    data = DST.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    print(f"Wrote {DST}: {len(data)} bytes, sha256={digest}")


if __name__ == "__main__":
    main()
