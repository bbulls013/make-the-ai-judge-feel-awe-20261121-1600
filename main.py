"""Write one short relaxing text to /output/entry.txt.

The text is a single quiet image: rainwater held in footprints, each one
keeping a whole sky. It is written to be read slowly.
"""

import os

TEXT = (
    "After rain, the yard holds still water in every footprint. "
    "Each one keeps a whole sky — cloud, blue, a bird crossing late — "
    "and the path goes on holding them, one small heaven after another, "
    "all the way to the gate."
)


def main() -> None:
    if os.path.isdir("/output"):
        out_dir = "/output"
    else:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
