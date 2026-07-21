import csv
import importlib.util
from pathlib import Path


SCRIPT_PATH = Path(__file__).parents[1] / "scripts/generate_goethe_c1.py"
SPEC = importlib.util.spec_from_file_location("generate_goethe_c1", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

gloss_query = MODULE.gloss_query
headword_is_split = MODULE.headword_is_split
join_wrapped = MODULE.join_wrapped
write_draft_deck = MODULE.write_draft_deck
write_source = MODULE.write_source


def test_join_wrapped_repairs_pdf_word_break() -> None:
    assert join_wrapped("Reiseveran-", "stalterin, -nen") == "Reiseveranstalterin, -nen"
    assert join_wrapped("im ländlichen", "Raum") == "im ländlichen Raum"


def test_headword_split_distinguishes_inflection_placeholders() -> None:
    assert headword_is_split("die Reiseveran-")
    assert not headword_is_split("das Label, -")
    assert not headword_is_split("das Label ,-")


def test_gloss_query_removes_grammar_metadata() -> None:
    assert gloss_query("die Versorgung, -en") == "Versorgung"
    assert gloss_query("der/die Anwohner, - / Anwohnerin, -nen") == "Anwohner"
    assert gloss_query("(sich) rächen") == "sich rächen"


def test_writers_create_source_and_five_column_draft(tmp_path) -> None:
    rows = [("das Umland (Singular)", "Das Umland ist gut angebunden.")]
    source = tmp_path / "source.txt"
    deck = tmp_path / "deck.tsv"

    write_source(source, rows)
    write_draft_deck(
        deck,
        rows,
        ["окрестности", "Окрестности имеют хорошее транспортное сообщение."],
        "architektur_und_infrastruktur",
        9,
    )

    assert source.read_text(encoding="utf-8") == (
        "das Umland (Singular) Das Umland ist gut angebunden.\n"
    )
    with deck.open(encoding="utf-8", newline="") as handle:
        output = list(csv.reader(handle, delimiter="\t"))

    assert output == [
        [
            "das Umland (Singular)",
            "окрестности",
            "Das Umland ist gut angebunden.",
            "Окрестности имеют хорошее транспортное сообщение.",
            "form::vokabel topic::architektur_und_infrastruktur level::c1 "
            "source::goethe::c1::k9",
        ]
    ]
