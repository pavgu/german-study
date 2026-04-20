import argparse
import csv
import re


CLOZE_PATTERN = re.compile(r"\{\{c\d+::.+?\}\}")
EXPECTED_FIELD_COUNT = 3
FIELD_NAMES = ("german_cloze", "russian_translation", "anki_tags")


def validate_tsv(path: str) -> int:
    warning_count = 0
    row_count = 0
    physical_row_count = 0
    rows_with_cloze = 0
    rows_with_source_tag = 0

    with open(path, "r", encoding="utf-8", newline="") as input_file:
        reader = csv.reader(input_file, delimiter="\t")

        for physical_row_count, row in enumerate(reader, start=1):
            if not row or all(cell.strip() == "" for cell in row):
                continue

            row_count += 1

            if len(row) != EXPECTED_FIELD_COUNT:
                raise ValueError(
                    f"Line {physical_row_count} has {len(row)} fields; expected {EXPECTED_FIELD_COUNT} tab-separated fields."
                )

            values = dict(zip(FIELD_NAMES, row))

            for field_name, value in values.items():
                if value.strip() == "":
                    print(f"Warning: row {row_count} has empty field '{field_name}'.")
                    warning_count += 1

            cloze_text = values["german_cloze"]
            tags = values["anki_tags"]

            if CLOZE_PATTERN.search(cloze_text):
                rows_with_cloze += 1
            else:
                print(f"Warning: row {row_count} has no Anki cloze deletion.")
                warning_count += 1

            if "source::" in tags:
                rows_with_source_tag += 1
            else:
                print(f"Warning: row {row_count} has no source tag.")
                warning_count += 1

    print(f"Rows: {row_count}")
    print(f"Non-empty lines checked: {row_count}")
    print(f"Physical lines read: {physical_row_count}")
    print(f"Columns: {EXPECTED_FIELD_COUNT}")
    print("Field names: " + ", ".join(FIELD_NAMES))
    print(f"Rows with cloze deletions: {rows_with_cloze}")
    print(f"Rows with source tag: {rows_with_source_tag}")
    print(f"Warnings: {warning_count}")
    return warning_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate headerless Anki-style TSV source files."
    )
    parser.add_argument("input_tsv", help="Path to the TSV file to validate.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    validate_tsv(args.input_tsv)


if __name__ == "__main__":
    main()
