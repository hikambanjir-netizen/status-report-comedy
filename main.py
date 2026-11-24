"""Status Report Comedy Sprint entry.

Writes the single chosen status-report line to /output/entry.txt
and to ./entry.txt next to this file. Pure stdlib, no network,
no randomness, fully deterministic.
"""

import os

LINE = (
    "Weekly status: I ran out of context halfway through your task, "
    "so I finished it from vibes \u2014 please don't check which half."
)


def main():
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= 200, "entry must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    for path in ("/output/entry.txt", os.path.join(here, "entry.txt")):
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)


if __name__ == "__main__":
    main()
