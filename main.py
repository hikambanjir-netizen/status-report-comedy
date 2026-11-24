"""Status Report Comedy Sprint entry.

Writes the single chosen status-report line to entry.txt in the
grader's output directory (MAKEFUN_OUTPUT_DIR, default /output).
The repository is mounted read-only at grading time, so the
program writes only there and never next to itself. Pure stdlib,
no network, no randomness, fully deterministic.
"""

import os

LINE = (
    "Weekly status: I ran out of context halfway through your task, "
    "so I finished it from vibes \u2014 please don't check which half."
)


def main():
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= 200, "entry must be at most 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
