import argparse
import csv


DEFAULT_DEFINITION = "Definition fehlt"
DEFAULT_EXAMPLE = "Beispielsatz fehlt."


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
            row["german_definition"] = row.get("german_definition") or DEFAULT_DEFINITION
            row["example_sentence"] = row.get("example_sentence") or DEFAULT_EXAMPLE
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
        description="Convert a German-Russian TSV into a learner dictionary scaffold."
    )
    parser.add_argument("input_tsv", help="Path to the source TSV file.")
    parser.add_argument("output_tsv", help="Path to the converted TSV file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    convert_dictionary(args.input_tsv, args.output_tsv)


if __name__ == "__main__":
    main()
