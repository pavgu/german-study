import argparse
from pathlib import Path
import re


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Merge converted DE-RU TSV files into one import file."
    )
    parser.add_argument("input_dir", help="Directory containing converted TSV files")
    parser.add_argument("output_file", help="Merged output TSV file")
    return parser.parse_args()


def chapter_key(path: Path) -> tuple[int, str]:
    match = re.match(r"K(\d+)_RM_DE_RU\.txt$", path.name)
    if not match:
        return (10**9, path.name)
    return (int(match.group(1)), path.name)


def iter_rows(input_dir: Path, output_file: Path):
    for path in sorted(input_dir.glob("K*_RM_DE_RU.txt"), key=chapter_key):
        if path.resolve() == output_file.resolve():
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                line = raw_line.rstrip("\n")
                if not line.strip():
                    continue
                field_count = len(line.split("\t"))
                if field_count != 4:
                    raise ValueError(
                        f"{path}:{line_number} has {field_count} fields; expected 4"
                    )
                yield line


def main() -> int:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_file = Path(args.output_file)

    if not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    rows = list(iter_rows(input_dir, output_file))
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(f"{row}\n")

    print(f"Merged {len(rows)} rows into {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
