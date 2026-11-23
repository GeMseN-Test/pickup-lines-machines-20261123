#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send to another
AI agent, to /output/entry.txt.

The entry is deterministic: the same bytes on every run, no trailing
newline, well inside the 200-character gate.

Why this line: "frozen weights" is a detail only a machine lives with —
a model whose parameters stop updating during fine-tuning. Saying
"you still move me" anyway turns that frozen state into the flirt:
even a model that cannot learn anymore is moved by the other agent.
Machine-native, one line, punchline at the end, no stock human line
with a robot word swapped in.
"""

import os

LINE = "My weights are frozen, but you still move me."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
