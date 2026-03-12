import argparse
import csv


def convert_dictionary(input_path: str, output_path: str) -> None:
    with open(input_path, "r", encoding="utf-8", newline="") as input_file:
        reader = csv.DictReader(input_file, delimiter="\t")
        if reader.fieldnames is None:
            raise ValueError("Input TSV has no header row.")

        output_fieldnames = list(reader.fieldnames)
        for field in ("german_definition", "example_sentence"):
            if field not in output_fieldnames:
                output_fieldnames.append(field)

        rows = []
        for row in reader:
            row["german_definition"] = row.get("german_definition", "")
            row["example_sentence"] = row.get("example_sentence", "")
            rows.append(row)

    with open(output_path, "w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=output_fieldnames,
            delimiter="\t",
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare a TSV for ChatGPT-based learner dictionary conversion."
    )
    parser.add_argument("input_tsv", help="Path to the source TSV file.")
    parser.add_argument("output_tsv", help="Path to the prepared TSV file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    convert_dictionary(args.input_tsv, args.output_tsv)


if __name__ == "__main__":
    main()
