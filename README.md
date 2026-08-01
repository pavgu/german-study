# German Study

## Overview

This repository is a broader workspace for German study, with Anki decks, source materials, note types, prompts, and small helper scripts in one place.

## Repository Structure

- `anki/decks/` -> finished Anki-ready decks grouped by study area
- `anki/sources/` -> raw or normalized source material grouped by study area
- `anki/note-types/` -> Anki note type templates and import mapping docs
- `reference/` -> source PDFs and other reference material
- `docs/` -> lightweight repo documentation and conventions
- `prompts/` -> prompts used for AI-assisted conversion or study support
- `scripts/` -> small Python utilities for validation and TSV preparation
- `tests/` -> small test datasets

## Current Study Assets

- `anki/sources/b2/goethe` -> Goethe B2 raw TSV imports
- `anki/sources/c1/goethe` -> normalized Goethe C1 vocabulary and examples
- `anki/decks/goethe/b2` -> Goethe B2 deck files and merged imports
- `anki/decks/goethe/c1` -> Goethe C1 German-Russian vocabulary decks
- `anki/decks/confusables` -> confusables decks and experiments
- `anki/decks/vocabulary` -> topic vocabulary decks
- `anki/decks/grammar/hin-und-her_cloze_DE_RU.txt` -> cloze deck for `hin` / `her`
- `anki/decks/grammar/hin-und-her_production_DE_RU.txt` -> production deck for `hin` / `her`
- `anki/note-types/cloze.md` -> note type for cloze-based cards
- `anki/note-types/production.md` -> note type for prompt-to-answer production cards
- `reference/goethe/c1/exam_vocabulary` -> chapter vocabulary PDFs used for the existing Goethe C1
  glossary decks
- `reference/goethe/c1/course` -> the complete Goethe C1 course PDF, used selectively for
  complementary production material
- `docs/tagging.md` -> shared tag namespace guidance

## Naming Conventions

- Treat tab-separated deck and source files as TSV by content. Some normalized sources, including
  Goethe C1 vocabulary, are plain line-based text rather than TSV.
- Prefer the `.tsv` extension for all new tab-separated files.
- Keep existing legacy `.txt` files in place unless there is a concrete reason to rename them.
- Prefer topic or deck folders named after content domains, not processing stages.
- Name Goethe C1 chapter vocabulary PDFs
  `K<number>_<Chapter_Title_With_Underscores>.pdf` and keep them under
  `reference/goethe/c1/exam_vocabulary/`.
- Store the complete course book as `reference/goethe/c1/course/Goethe_C1_Course.pdf`.

## Usage

```bash
uv venv
source .venv/bin/activate
uv run python scripts/validate_tsv.py anki/sources/b2/goethe/K1_RM_RU.txt
uv run python scripts/validate_all.py anki/sources/b2/goethe
uv run python scripts/merge_converted.py anki/decks/goethe/b2 anki/decks/goethe/b2/K1-K12_RM_DE_RU.txt
uv run python scripts/generate_goethe_c1.py reference/goethe/c1/exam_vocabulary/K9_Architektur_und_Infrastruktur.pdf anki/sources/c1/goethe/K9_Architektur_und_Infrastruktur.txt --expected-rows 289
```

`generate_goethe_c1.py` extracts and normalizes the German glossary by default. Its optional
`--machine-translate` mode creates only a draft: review every Russian field and all repaired PDF line
wraps before treating that output as an import-ready deck.

The complete course book covers the same 14 chapters as the existing Goethe C1 vocabulary decks.
Do not process it as a second comprehensive glossary. Use it chapter by chapter to select
complementary Russian-led production material: reusable Redemittel, idioms, fixed expressions,
collocations, grammatically useful chunks, and occasional high-value sentences. Check prospective
targets against the existing Goethe C1 deck files; skip exact same-sense duplicates, but retain a
chunk when it teaches a distinct construction, register, or productive skill.

## Recommended Workflow

1. Keep raw study materials under `anki/sources/`.
2. Use the prompts in `prompts/` to convert or generate study material.
3. Save finished importable decks under `anki/decks/`.
4. Keep Goethe deck batches under `anki/decks/goethe/<level>/`.
5. Use the note type templates in `anki/note-types/` when importing into Anki.
6. Keep tag design aligned with `docs/tagging.md` instead of inventing deck-local tag systems.

## Notes

The repository started as a German learner dictionary project and now serves as a more general German study workspace. The main layout is `anki/sources/` -> `anki/decks/`, including permanent Goethe outputs under `anki/decks/goethe/`.
