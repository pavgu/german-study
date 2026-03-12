# German Learner Dictionary

## Overview

This project converts German→Russian source TSV files into German-focused Anki production cards suitable for B2 learners. The intended workflow is prompt-first: validate raw Anki-style rows locally, then use ChatGPT to convert each raw file directly into a 4-column DE-RU TSV.

## Features

- TSV dictionary processing
- Prompt-first conversion workflow
- German explanation generation for cloze targets
- Production-card rewriting for better active recall
- Validation pipeline
- Prompt-only DE-RU conversion from raw files
- Per-file DE-RU conversion output
- Merge step for single-file Anki import

## Repository Structure

- `data/raw/<level>/<source>` → original TSV files grouped by CEFR level and source
- `data/converted/<level>/<source>` → processed German→German dictionary files after ChatGPT-based conversion
- `data/samples` → small testing datasets
- `docs` → workflow notes and Anki setup documentation
- `scripts` → small Python utilities for validation and TSV preparation
- `prompts` → prompts used for production-card conversion and German explanation generation
- `tests` → small test datasets

Current source layout:

- `data/raw/b2/goethe` → Goethe B2 raw dictionary files
- `data/converted/b2/goethe` → converted outputs for the same source

## TSV Format

Example output schema:

```tsv
german_sentence	german_definition_or_synonym	russian_translation	anki_tags
```

Example row:

```tsv
Mein {{c1::wichtigster}} Gegenstand ist {{c2::…}}.	entscheidendster / am wichtigsten	Мой самый важный предмет — это …	form::satzmuster func::beschreibung topic::gegenstände level::b2_c1 source::goethe::b2::k1
```

## Usage

```bash
uv venv
source .venv/bin/activate
uv run python scripts/validate_tsv.py data/raw/b2/goethe/K1_RM_RU.txt
uv run python scripts/validate_all.py data/raw/b2/goethe
uv run python scripts/merge_converted.py data/converted/b2/goethe data/converted/b2/goethe/K1-K12_RM_DE_RU.txt
```

Recommended workflow:

1. Validate the source TSV.
2. Use ChatGPT with the rules in `prompts/definition_rules.md` and `prompts/fill_german_field.md` to convert one raw source file directly into a 4-column DE-RU production-card TSV, rewriting placeholder or weak clozes when necessary.
3. Save the completed file in the matching `data/converted/<level>/<source>/` folder.
4. Repeat the same prompt workflow for the next raw file in the directory.
5. Merge the converted chapter files into one TSV for faster Anki import.
6. Create an Anki note type using the templates in `docs/anki_note_type.md`.

## Development Notes

ChatGPT or another AI model can be used to generate German definitions and example sentences. The prompt guidance in `prompts/definition_rules.md` defines the expected style for learner-friendly output. The scripts in this repository are intentionally minimal and are only meant to support a manual AI-assisted workflow, not replace it.

This repository is set up to use `uv` with a local `.venv`. If you want development tools from `pyproject.toml`, run `uv sync --dev`.
