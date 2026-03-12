import argparse
import csv


REQUIRED_COLUMNS = ("lemma", "pos", "russian_translation")


def validate_tsv(path: str) -> int:
    warning_count = 0

    with open(path, "r", encoding="utf-8", newline="") as input_file:
        reader = csv.DictReader(input_file, delimiter="\t")
        if reader.fieldnames is None:
            raise ValueError("TSV file has no header row.")

        missing_columns = [column for column in REQUIRED_COLUMNS if column not in reader.fieldnames]
        if missing_columns:
            raise ValueError(
                "Missing required columns: " + ", ".join(missing_columns)
            )

        row_count = 0
        for row_count, row in enumerate(reader, start=1):
            for column in reader.fieldnames:
                value = row.get(column, "")
                if value is None or value.strip() == "":
                    print(f"Warning: row {row_count} has empty field '{column}'.")
                    warning_count += 1

    print(f"Rows: {row_count}")
    print(f"Columns: {len(reader.fieldnames)}")
    print("Column names: " + ", ".join(reader.fieldnames))
    print(f"Warnings: {warning_count}")
    return warning_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate TSV dictionary input.")
    parser.add_argument("input_tsv", help="Path to the TSV file to validate.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    validate_tsv(args.input_tsv)


if __name__ == "__main__":
    main()
