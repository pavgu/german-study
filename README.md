# German Study

## Overview

This repository is a broader workspace for German study, with Anki decks, source materials, note types, prompts, and small helper scripts in one place.

## Repository Structure

- `anki/decks/` -> finished Anki-ready decks grouped by study area
- `anki/sources/` -> raw TSV source files grouped by study area
- `anki/note-types/` -> Anki note type templates and import mapping docs
- `reference/` -> source PDFs and other reference material
- `docs/` -> lightweight repo documentation and conventions
- `prompts/` -> prompts used for AI-assisted conversion or study support
- `scripts/` -> small Python utilities for validation and TSV preparation
- `tests/` -> small test datasets

## Current Study Assets

- `anki/sources/b2/goethe` -> Goethe B2 raw TSV imports
- `anki/sources/c1/goethe` -> Goethe C1 raw TSV imports
- `anki/decks/goethe/b2` -> Goethe B2 deck files and merged imports
- `anki/decks/confusables` -> confusables decks and experiments
- `anki/decks/vocabulary` -> topic vocabulary decks
- `anki/decks/grammar/hin-und-her_cloze_DE_RU.txt` -> cloze deck for `hin` / `her`
- `anki/decks/grammar/hin-und-her_production_DE_RU.txt` -> production deck for `hin` / `her`
- `anki/note-types/cloze.md` -> note type for cloze-based cards
- `anki/note-types/production.md` -> note type for prompt-to-answer production cards
- `reference/goethe` -> Goethe source PDFs
- `docs/tagging.md` -> shared tag namespace guidance

## Naming Conventions

- Treat deck and source files as TSV by content.
- Prefer the `.tsv` extension for all new tab-separated files.
- Keep existing legacy `.txt` files in place unless there is a concrete reason to rename them.
- Prefer topic or deck folders named after content domains, not processing stages.

## Usage

```bash
uv venv
source .venv/bin/activate
uv run python scripts/validate_tsv.py anki/sources/b2/goethe/K1_RM_RU.txt
uv run python scripts/validate_all.py anki/sources/b2/goethe
uv run python scripts/merge_converted.py anki/decks/goethe/b2 anki/decks/goethe/b2/K1-K12_RM_DE_RU.txt
```

## Recommended Workflow

1. Keep raw study materials under `anki/sources/`.
2. Use the prompts in `prompts/` to convert or generate study material.
3. Save finished importable decks under `anki/decks/`.
4. Keep Goethe deck batches under `anki/decks/goethe/<level>/`.
5. Use the note type templates in `anki/note-types/` when importing into Anki.
6. Keep tag design aligned with `docs/tagging.md` instead of inventing deck-local tag systems.

## Notes

The repository started as a German learner dictionary project and now serves as a more general German study workspace. The main layout is `anki/sources/` -> `anki/decks/`, including permanent Goethe outputs under `anki/decks/goethe/`.
