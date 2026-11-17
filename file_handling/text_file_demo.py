"""Read, write, and append to a text file using context managers."""

from pathlib import Path

DATA_DIR = Path(__file__).parent / "sample_data"
FILE_PATH = DATA_DIR / "notes.txt"


def main():
    DATA_DIR.mkdir(exist_ok=True)

    # Write replaces existing content; append adds to the end.
    FILE_PATH.write_text("Welcome to Python file handling.\n", encoding="utf-8")
    with FILE_PATH.open("a", encoding="utf-8") as file:
        file.write("This line was added in append mode.\n")

    contents = FILE_PATH.read_text(encoding="utf-8")
    print(contents, end="")
    print(f"\nFile size: {FILE_PATH.stat().st_size} bytes")


if __name__ == "__main__":
    main()
