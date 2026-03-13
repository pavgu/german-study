# German Study

## Overview

This repository is a broader workspace for German study, with Anki decks, note types, raw import materials, prompts, and small helper scripts in one place.

## Repository Structure

- `anki/decks/` -> finished Anki-ready decks grouped by study area
- `anki/imports/raw/` -> raw TSV input files before conversion
- `anki/imports/converted/` -> converted TSV imports for larger deck builds
- `anki/note-types/` -> Anki note type templates and import mapping docs
- `grammar/` -> grammar notes and future topic-specific material
- `vocabulary/` -> vocabulary notes and future topic-specific material
- `writing/`, `speaking/`, `reading/`, `listening/` -> space for skill-specific study assets
- `prompts/` -> prompts used for AI-assisted conversion or study support
- `scripts/` -> small Python utilities for validation and TSV preparation
- `tests/` -> small test datasets
- `data/` -> auxiliary samples and legacy scratch data

## Current Study Assets

- `anki/imports/raw/b2/goethe` -> Goethe B2 raw TSV imports
- `anki/imports/converted/b2/goethe` -> converted Goethe B2 TSV imports
- `anki/decks/grammar/hin-und-her_cloze_DE_RU.txt` -> cloze deck for `hin` / `her`
- `anki/decks/grammar/hin-und-her_production_DE_RU.txt` -> production deck for `hin` / `her`
- `anki/note-types/cloze.md` -> note type for cloze-based cards
- `anki/note-types/production.md` -> note type for prompt-to-answer production cards

## Usage

```bash
uv venv
source .venv/bin/activate
uv run python scripts/validate_tsv.py anki/imports/raw/b2/goethe/K1_RM_RU.txt
uv run python scripts/validate_all.py anki/imports/raw/b2/goethe
uv run python scripts/merge_converted.py anki/imports/converted/b2/goethe anki/imports/converted/b2/goethe/K1-K12_RM_DE_RU.txt
```

## Recommended Workflow

1. Validate a raw TSV when you are working with the legacy import flow.
2. Use the prompts in `prompts/` to convert or generate study material.
3. Save finished importable decks under `anki/decks/`.
4. Keep larger intermediate conversion batches under `anki/imports/converted/`.
5. Use the note type templates in `anki/note-types/` when importing into Anki.

## Notes

The repository started as a German learner dictionary project and now serves as a more general German study workspace. Some helper scripts still support the older raw-to-converted import flow, which is why `anki/imports/` remains part of the structure.
