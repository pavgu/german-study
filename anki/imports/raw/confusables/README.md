# Confusables Raw Sources

Store raw TSV source files for confusing German words and expressions here.

Recommended pattern:

- one master file for all confusable pairs
- 2 columns per row

Columns:

1. `Target`
2. `Confuser`

Example:

```tsv
ermitteln	vermitteln
meiden	vermeiden
```

Suggested filenames:

- `confusables.txt`

Recommended default:

- [confusables.txt](/mnt/data/german-study/anki/imports/raw/confusables/confusables.txt)

The contrast meaning, example sentences, translations, and tags are generated later by the prompt.

Use [confusables_to_anki.md](/mnt/data/german-study/prompts/confusables_to_anki.md) to convert these raw rows into Anki-ready TSV output.
