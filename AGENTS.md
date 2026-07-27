# Repository Instructions

This repository stores German study material, primarily headerless TSV files for Anki.
Preserve the established source-to-deck workflow and the schema of the deck family being edited.

## Sources of Truth

- Read `README.md` for the repository layout and common commands.
- Follow `docs/tagging.md` for tag namespaces and normalization.
- Use the matching file in `anki/note-types/` for Anki fields and import mappings.
- Use the matching file in `prompts/` for content-generation rules. Those detailed rules take
  precedence over summaries in this file for their deck family.
- Inspect neighboring files in the same deck family before creating or changing data.

## Repository Layout

- `anki/sources/`: raw or normalized study material.
- `anki/decks/`: finished, import-ready Anki data.
- `anki/note-types/`: note templates and TSV-to-Anki field mappings.
- `prompts/`: generation and conversion instructions.
- `reference/`: source PDFs and other reference material.
- `docs/`: shared conventions.
- `scripts/`: validation, conversion, and merge utilities.
- `tests/`: test data and Python tests.

Keep raw material under `anki/sources/` and finished imports under `anki/decks/`. Organize folders
by content domain or source, not by temporary processing stage.

## File Conventions

- All Anki data files are UTF-8, headerless, and tab-separated unless a raw source format clearly
  establishes otherwise.
- Prefer `.tsv` for new tab-separated files. Do not rename legacy `.txt` files without a concrete
  reason; they are also TSV by content.
- Write one logical note per physical line. Do not place tabs or line breaks inside fields.
- Do not add Markdown, code fences, bullets, numbering, commentary, or a header row to deck data.
- Skip empty source lines and avoid empty output fields unless the relevant schema explicitly permits
  them.
- Preserve source order and the required row ratio. For example, topic vocabulary creates one output
  row per non-empty source line, while confusables production creates three rows per source pair.
- Preserve correct German source wording exactly. Correct only clear extraction, spelling, or grammar
  errors, and keep the source and finished deck consistent when doing so.
- Name Goethe chapter PDFs `K<number>_<Chapter_Title_With_Underscores>.pdf`, preserving German
  spelling such as `K7_Zeit_und_Lebensqualität.pdf`.

## Active Deck Schemas

Determine the schema from the deck family, its note-type document, and neighboring files. Do not use
one global column count for the repository.

### Goethe B2 Cloze

Raw files under `anki/sources/b2/goethe/` have three columns:

1. German cloze text
2. Russian translation
3. Anki tags

Converted files under `anki/decks/goethe/b2/` have four columns:

1. German cloze text
2. German cue
3. Russian translation
4. Anki tags

Use `anki/note-types/cloze.md` and `prompts/fill_german_field.md`. Preserve the tag field exactly
during conversion. The merged `K1-K12_RM_DE_RU.txt` file is generated from the per-chapter files and
must not be treated as an independent source.

### Goethe C1 Vocabulary

Normalized sources under `anki/sources/c1/goethe/` contain one German vocabulary item and its German
example per line. Finished files under `anki/decks/goethe/c1/` have five columns:

1. German headword or expression
2. Russian gloss
3. German example
4. Russian example translation
5. Anki tags

Keep the headword and German example aligned with the normalized source. Russian glosses should be
concise and context-appropriate; example translations should be natural Russian and preserve the
German meaning. Follow neighboring chapter naming such as
`c1_goethe_k8_reisen_und_tourismus_DE_RU.txt`.

Use stable chapter tags in this form:

```text
form::vokabel topic::<normalized_topic> level::c1 source::goethe::c1::k<chapter>
```

### Erkundungen C2 Expressions

The complete reference book is stored at
`reference/erkundungen/c2/Erkundungen_C2.pdf`. Work chapter by chapter using its PDF bookmarks and
printed page numbers. Current chapter boundaries are:

- K1, `Sprache und Kommunikation`: printed pages 5-32, PDF pages 6-33;
- K2, `Vergangenheit und Gegenwart`: printed pages 33-62, PDF pages 34-63;
- K3, `Stärken und Schwächen`: printed pages 63-88, PDF pages 64-89.

Normalized sources under `anki/sources/c2/erkundungen/` have four columns:

1. exact or minimally normalized German target;
2. printed book page;
3. exercise or section identifier;
4. content type: `redewendung` or `satz`.

Finished files under `anki/decks/erkundungen/c2/` use the four-column Russian-led production schema:

1. Russian prompt;
2. German answer;
3. German hint;
4. Anki tags.

Extract the shortest self-contained unit that preserves natural meaning and usage. Favor idioms,
fixed expressions, useful collocations, and formal Redemittel. Keep a complete sentence only when its
context is essential to its learning value. Do not create abstract `satzmuster` with placeholders.
Follow `prompts/erkundungen_c2_to_production_ru.md` and `anki/note-types/production.md`.

Use stable chapter tags in this form:

```text
form::redewendung func::produktion topic::<normalized_chapter_topic> level::c2 source::erkundungen::c2::k<chapter> card::chunk
```

For the occasional complete sentence, use `form::satz` and `card::satz` instead.

### Russian-Led Production

General topic vocabulary, grammar, and confusable production decks normally use four columns:

1. Russian prompt
2. German answer
3. German hint
4. Anki tags

Use `anki/note-types/production.md` or `anki/note-types/confusables-production-ru.md` as applicable.
For topic vocabulary, apply `prompts/topic_vocab_to_production_ru.md`. For verb-preposition decks,
apply `prompts/verbs_prepositions_to_production_ru.md`.

The Russian prompt must cue the intended German answer precisely. The German hint must be short and
helpful without repeating the target word, an inflected form of it, or merely translating it. Do not
add cloze markup to production answers.

### Antonyms

Antonym production notes have nine columns in the order documented by
`anki/note-types/antonyms-production-ru.md` and `prompts/antonyms_to_anki.md`. Generate one note per
input pair. Keep both German pair members unchanged, write independent German definitions, and use
natural Russian prompts with idiomatic German answer sentences.

### Confusables

Raw confusable rows contain two tab-separated German items. Follow the selected prompt exactly:
`prompts/confusables_to_anki.md` produces cloze-oriented rows, while
`prompts/confusables_to_production_ru.md` produces Russian-led production rows. Both workflows create
three output rows per input pair. Preserve reflexive forms, separable verbs, and case government.

## Tagging

- Use lowercase, space-separated, namespace-style tags.
- Reuse the namespaces in `docs/tagging.md`, including `form::`, `func::`, `topic::`, `level::`,
  `source::`, `card::`, `domain::`, `pair::`, `confusable::`, and `antonym::`.
- Keep tag sets small and useful for filtering. Do not invent deck-local namespaces or free-form tags.
- Normalize topic and pair values using the rules in `docs/tagging.md`.
- Preserve existing tags when a conversion prompt requires it.
- Do not add `pair::` or card-direction tags to antonym notes; one note already generates several card
  directions.

## Language Quality

- Use natural, modern standard German and natural Russian.
- Preserve German articles, reflexive pronouns, separable prefixes, prepositions, governed cases,
  register labels, and plural information.
- Match the Russian meaning to the sense demonstrated by the German example, especially for
  polysemous words and technical vocabulary.
- Prefer precise prompts and glosses over literal machine translation.
- Definitions and hints must not contain the answer word and must not be disguised cloze exercises.
- Avoid vague dictionary fragments when a short phrase or sentence disambiguates the target better.

## Validation

Use the project environment when available:

```bash
uv run pytest
uv run ruff check .
```

The current `scripts/validate_tsv.py` is specifically a three-column cloze-source validator. Use it
only for files with that schema:

```bash
uv run python scripts/validate_tsv.py anki/sources/b2/goethe/K1_RM_RU.txt
uv run python scripts/validate_all.py anki/sources/b2/goethe
```

For other deck families, validate their documented column count with a TSV-aware parser. At minimum,
check:

- the expected number of fields on every non-empty row;
- required fields are non-empty;
- expected row count and source-to-output ratio;
- unique headwords or note identities where duplicates are not intended;
- exact, consistent tags;
- source order and source-to-deck German-field consistency;
- UTF-8 output, Unix newlines, and a final newline.

Use the existing conversion and merge tools only for their documented formats:

```bash
uv run python scripts/convert_dictionary.py <input> [output]
uv run python scripts/merge_converted.py anki/decks/goethe/b2 anki/decks/goethe/b2/K1-K12_RM_DE_RU.txt
```

For Goethe C1 PDFs, use `scripts/generate_goethe_c1.py` to produce the normalized German source.
The script's optional `--machine-translate` output is a draft only. Review extraction joins, obvious
German source errors, every Russian gloss, and every example translation before declaring the deck
finished.

After editing Python, run the focused tests plus Ruff. After editing deck data, report the schema and
row-count checks that were actually run; do not claim the generic validator passed a schema it does
not support.
