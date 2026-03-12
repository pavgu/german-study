import argparse
from pathlib import Path

from validate_tsv import validate_tsv


def validate_all(input_dir: str) -> int:
    base_path = Path(input_dir)
    files = sorted(path for path in base_path.glob("*.txt") if path.is_file())

    if not files:
        raise ValueError(f"No .txt files found in {base_path}")

    files_with_issues = 0

    for path in files:
        print(f"Checking {path}")
        try:
            warning_count = validate_tsv(str(path))
        except Exception as exc:
            files_with_issues += 1
            print(f"ERROR: {path} failed validation: {exc}")
            continue

        if warning_count > 0:
            files_with_issues += 1
            print(f"RESULT: {path} has {warning_count} warnings.")
        else:
            print(f"RESULT: {path} passed.")

    print(f"Files checked: {len(files)}")
    print(f"Files with issues: {files_with_issues}")
    return files_with_issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate all headerless Anki-style TSV source files in a directory."
    )
    parser.add_argument("input_dir", help="Directory containing source .txt files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    issue_count = validate_all(args.input_dir)
    raise SystemExit(1 if issue_count else 0)


if __name__ == "__main__":
    main()
