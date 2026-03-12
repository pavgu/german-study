import argparse
import csv
from pathlib import Path


def default_output_path(input_path: str) -> str:
    path = Path(input_path)
    if "_RU" not in path.stem:
        raise ValueError("Input filename must contain '_RU' to build the output name.")
    output_name = path.stem.replace("_RU", "_DE_RU", 1) + path.suffix

    path_parts = list(path.parts)
    try:
        raw_index = path_parts.index("raw")
    except ValueError as exc:
        raise ValueError("Input path must contain '/raw/' so the converted path can mirror it.") from exc

    path_parts[raw_index] = "converted"
    mirrored_dir = Path(*path_parts[:-1])
    return str(mirrored_dir / output_name)


def convert_dictionary(input_path: str, output_path: str) -> int:
    row_count = 0
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8", newline="") as input_file, open(
        output, "w", encoding="utf-8", newline=""
    ) as output_file:
        reader = csv.reader(input_file, delimiter="\t")
        writer = csv.writer(output_file, delimiter="\t")

        for row in reader:
            if not row or all(cell.strip() == "" for cell in row):
                continue

            if len(row) != 3:
                raise ValueError(
                    f"Expected 3 tab-separated fields in {input_path}, got {len(row)}."
                )

            german_sentence, russian_translation, anki_tags = row
            writer.writerow([german_sentence, "", russian_translation, anki_tags])
            row_count += 1

    return row_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a raw Goethe source file into a 4-column DE-RU TSV."
    )
    parser.add_argument("input_tsv", help="Path to the source TSV file.")
    parser.add_argument(
        "output_tsv",
        nargs="?",
        help="Optional output path. Defaults to the mirrored converted path with '_DE' inserted before '_RU'.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = args.output_tsv or default_output_path(args.input_tsv)
    row_count = convert_dictionary(args.input_tsv, output_path)
    print(f"Wrote {row_count} rows to {output_path}")


if __name__ == "__main__":
    main()
