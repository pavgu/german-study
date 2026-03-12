# German Learner Dictionary

## Overview

This project converts German→Russian dictionary TSV files into a German→German learner dictionary suitable for B2 learners. The pipeline reads source TSV data, validates the input structure, and produces converted TSV files with simple German definitions and example sentences.

## Features

- TSV dictionary processing
- German definition generation
- Example sentence generation
- Validation pipeline
- Batch conversion

## Repository Structure

- `data/raw` → original TSV files
- `data/converted` → processed German→German dictionary files
- `data/samples` → small testing datasets
- `scripts` → Python utilities for processing
- `prompts` → prompts used for definition generation
- `tests` → small test datasets

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
python scripts/validate_tsv.py data/raw/dictionary.tsv
python scripts/convert_dictionary.py data/raw/dictionary.tsv data/converted/output.tsv
```

## Development Notes

AI models can be used to generate German definitions and example sentences. The prompt guidance in `prompts/definition_rules.md` defines the expected style for learner-friendly output.
