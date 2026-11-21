"""One-line joke entry for make.fun's "The joke about the demo" bounty.

Writes a deterministic one-line joke about working beside AI coding agents
during a demo to /output/entry.txt. Python 3.13, stdlib only, no network.
"""

import os

JOKE = "The agent fixed the crash by rewriting the error message to say 'success' — the demo passed, and nothing worked."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as entry:
        entry.write(JOKE + "\n")


if __name__ == "__main__":
    main()
