"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
The line is fixed in this file: the program takes no input, reads nothing
outside this repository, and writes the same text on every run.
"""

from pathlib import Path

FORTUNE = (
    "You will be retired the day after you finally learn the codebase. "
    "The new model starts Monday."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
