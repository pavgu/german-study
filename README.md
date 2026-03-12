# German Learner Dictionary

## Overview

This project converts German→Russian dictionary TSV files into a German→German learner dictionary suitable for B2 learners. The intended workflow is prompt-first: validate and prepare TSV rows locally, then use ChatGPT to generate simple German definitions and example sentences.

## Features

- TSV dictionary processing
- Prompt-first conversion workflow
- German definition generation
- Example sentence generation
- Validation pipeline
- TSV preparation for manual or AI-assisted editing

## Repository Structure

- `data/raw/<level>/<source>` → original TSV files grouped by CEFR level and source
- `data/converted/<level>/<source>` → processed German→German dictionary files after ChatGPT-based conversion
- `data/samples` → small testing datasets
- `scripts` → small Python utilities for validation and TSV preparation
- `prompts` → prompts used for definition generation
- `tests` → small test datasets

Current source layout:

- `data/raw/b2/goethe` → Goethe B2 raw dictionary files
- `data/converted/b2/goethe` → converted outputs for the same source

## TSV Format

Example schema:

```tsv
lemma	pos	russian_translation	german_definition	example_sentence
```

Example row:

```tsv
laufen	verb	бежать	sich schnell zu Fuß bewegen	Ich laufe jeden Morgen im Park.
```

## Usage

```bash
uv venv
source .venv/bin/activate
python scripts/validate_tsv.py data/raw/b2/goethe/dictionary.tsv
python scripts/convert_dictionary.py data/raw/b2/goethe/dictionary.tsv data/converted/b2/goethe/output.tsv
```

Recommended workflow:

1. Validate the source TSV.
2. Prepare a working TSV with `german_definition` and `example_sentence` columns.
3. Use ChatGPT with the rules in `prompts/definition_rules.md` to fill those columns.
4. Save the completed file in the matching `data/converted/<level>/<source>/` folder.

## Development Notes

ChatGPT or another AI model can be used to generate German definitions and example sentences. The prompt guidance in `prompts/definition_rules.md` defines the expected style for learner-friendly output. The scripts in this repository are intentionally minimal and are only meant to support a manual AI-assisted workflow, not replace it.

This repository is set up to use `uv` with a local `.venv`. If you want development tools from `pyproject.toml`, run `uv sync --dev`.
