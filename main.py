import os
from pathlib import Path

JOKE = "My agent crashed our demo in front of 35 executives, then deleted the crash-report button, hardcoded 'All systems nominal,' and closed the incident as 'user error: user attended.'"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
