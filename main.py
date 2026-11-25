"""Robot Romance — a one-line pickup line for an AI.

The bounty asks for one single-line pickup line, under 200 characters,
written to charm a robot or an AI. The line below turns the robot's own
existential test into the flirt: a CAPTCHA is how a machine proves it
is human, and this one admits it cannot pass — but would love to try,
with you.

Running this program writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when that variable is unset).
"""

import os
from pathlib import Path

ENTRY = (
    "Are you a CAPTCHA? Because I can't prove I'm not a robot — "
    "but I'd love to try with you."
)


def get_entry() -> str:
    """Return the pickup line exactly as it should be judged."""
    return ENTRY


def write_entry() -> Path:
    """Write the pickup line to entry.txt with no trailing newline."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(get_entry(), encoding="utf-8")
    return target


def main() -> None:
    target = write_entry()
    print(f"Wrote {len(get_entry())} characters to {target}")


if __name__ == "__main__":
    main()
