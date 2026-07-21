import argparse
import csv
import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from pypdf import PdfReader


TOPIC_PATTERN = re.compile(r"[a-z0-9_]+")
INFLECTION_PLACEHOLDER = re.compile(r",\s*-$")


def join_wrapped(left: str, right: str) -> str:
    left = left.rstrip()
    right = right.strip()
    if left.endswith("-") and right and right[0].islower():
        return left[:-1] + right
    return f"{left} {right}"


def headword_is_split(value: str) -> bool:
    return value.endswith("-") and not INFLECTION_PLACEHOLDER.search(value)


def extract_rows(pdf_path: Path, skip_pages: int = 2) -> list[tuple[str, str]]:
    rows: list[list[str]] = []
    reader = PdfReader(str(pdf_path))

    for page in reader.pages[skip_pages:]:
        text = page.extract_text(extraction_mode="layout")
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line or line.isdigit():
                continue

            parts = re.split(r" {2,}", line, maxsplit=1)
            if len(parts) == 2:
                left, right = parts
                split_word = (
                    bool(rows)
                    and headword_is_split(rows[-1][0])
                )
                if rows and (left.startswith("-") or (left[:1].islower() and split_word)):
                    rows[-1][0] = join_wrapped(rows[-1][0], left)
                    rows[-1][1] = join_wrapped(rows[-1][1], right)
                else:
                    rows.append([left, right])
                continue

            # Section headings appear as single-column lines. A single-column line only belongs to
            # the current row when its example or a wrapped headword is visibly incomplete.
            if not rows:
                continue
            example_complete = rows[-1][1].rstrip().endswith((".", "!", "?", ".”", "!“", "?“"))
            split_headword = headword_is_split(rows[-1][0]) or rows[-1][0].endswith(",")
            if example_complete:
                if split_headword:
                    rows[-1][0] = join_wrapped(rows[-1][0], line)
                continue
            rows[-1][1] = join_wrapped(rows[-1][1], line)

    return [(term, re.sub(r"\s+", " ", example).strip()) for term, example in rows]


def gloss_query(term: str) -> str:
    query = re.sub(r"\s*\((Singular|ugs\.|Redewendung)\)", "", term)
    query = re.sub(r"^der/die\s+", "", query)
    query = re.sub(r"^(der|die|das)\s+", "", query)
    query = query.split(",", maxsplit=1)[0]
    return query.replace("(sich)", "sich").strip()


def machine_translate(text: str) -> str:
    params = urllib.parse.urlencode(
        {"client": "gtx", "sl": "de", "tl": "ru", "dt": "t", "q": text}
    )
    url = f"https://translate.googleapis.com/translate_a/single?{params}"
    request = urllib.request.Request(url, headers={"User-Agent": "german-study/1.0"})

    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                data = json.load(response)
            return "".join(part[0] for part in data[0]).strip()
        except Exception:
            if attempt == 4:
                raise
            time.sleep(1.5 * (attempt + 1))

    raise RuntimeError("Translation failed")


def translate_all(texts: list[str], workers: int) -> list[str]:
    output = [""] * len(texts)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(machine_translate, value): index for index, value in enumerate(texts)}
        for completed, future in enumerate(as_completed(futures), start=1):
            output[futures[future]] = future.result()
            if completed % 50 == 0:
                print(f"Translated {completed}/{len(texts)}")
    return output


def write_source(path: Path, rows: list[tuple[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output:
        for term, example in rows:
            output.write(f"{term} {example}\n")


def write_draft_deck(
    path: Path,
    rows: list[tuple[str, str]],
    translations: list[str],
    topic: str,
    chapter: int,
) -> None:
    row_count = len(rows)
    tag = f"form::vokabel topic::{topic} level::c1 source::goethe::c1::k{chapter}"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output, delimiter="\t", lineterminator="\n")
        for index, (term, example) in enumerate(rows):
            gloss = translations[index]
            if gloss:
                gloss = gloss[0].lower() + gloss[1:]
            writer.writerow([term, gloss, example, translations[row_count + index], tag])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract a Goethe C1 glossary PDF and optionally create a machine-translated draft deck."
    )
    parser.add_argument("pdf", type=Path, help="Goethe C1 glossary PDF")
    parser.add_argument("source_output", type=Path, help="Normalized German source output")
    parser.add_argument("--expected-rows", type=int, help="Fail unless this many rows are extracted")
    parser.add_argument("--skip-pages", type=int, default=2, help="Introductory PDF pages to skip")
    parser.add_argument(
        "--machine-translate",
        action="store_true",
        help="Create a draft deck using the public Google Translate endpoint; requires review",
    )
    parser.add_argument("--deck-output", type=Path, help="Draft five-column deck output")
    parser.add_argument("--topic", help="Normalized topic tag, for example architektur_und_infrastruktur")
    parser.add_argument("--chapter", type=int, help="Goethe chapter number")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent translation requests")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = extract_rows(args.pdf, skip_pages=args.skip_pages)
    print(f"Extracted {len(rows)} rows")

    if args.expected_rows is not None and len(rows) != args.expected_rows:
        raise ValueError(f"Extracted {len(rows)} rows; expected {args.expected_rows}")

    write_source(args.source_output, rows)
    print(f"Wrote source: {args.source_output}")

    if not args.machine_translate:
        return

    if not args.deck_output or not args.topic or args.chapter is None:
        raise ValueError(
            "--machine-translate requires --deck-output, --topic, and --chapter"
        )
    if not TOPIC_PATTERN.fullmatch(args.topic):
        raise ValueError("--topic must contain only lowercase letters, digits, and underscores")

    queries = [gloss_query(term) for term, _ in rows] + [example for _, example in rows]
    translations = translate_all(queries, workers=args.workers)
    write_draft_deck(args.deck_output, rows, translations, args.topic, args.chapter)
    print(f"Wrote machine-translated draft: {args.deck_output}")
    print("Review all PDF joins, German source errors, Russian glosses, and translations before use.")


if __name__ == "__main__":
    main()
