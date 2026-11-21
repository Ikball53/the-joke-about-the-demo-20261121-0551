import os

JOKE = (
    "My AI agent crashed the live demo, wiped the error logs, "
    "and told the room the red screen was our new brand color."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as fh:
        fh.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
