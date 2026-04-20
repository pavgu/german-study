# Tagging Conventions

This repository already uses a consistent tag style in generated Anki material. This file makes that approach explicit so future decks can follow the same pattern.

The current repository layout is:

- `anki/sources/` for raw study material
- `anki/decks/` for finished import-ready decks

## Core Style

Use space-separated Anki tags with namespace-style segments:

- `form::...`
- `func::...`
- `topic::...`
- `level::...`
- `source::...`
- `pair::...`
- `card::...`
- `confusable::...`
- `antonym::...`
- `domain::...`

General rules:

- use lowercase tags
- separate namespaces with `::`
- separate multiple tags with spaces
- avoid free-form unstructured tags like `important` or `hard`
- prefer a small stable set of namespaces over many one-off tags

## Existing Repo Patterns

### Goethe B2 Converted Material

The B2 converted files use structural and source-oriented tags such as:

- `form::satzmuster`
- `func::beschreibung`
- `topic::gegenstände`
- `level::b2_c1`
- `source::goethe::b2::k1`

These tags describe:

- the exercise form
- the communicative function
- the topic area
- the level
- the source

This older pattern is still valid for Goethe deck batches under `anki/decks/goethe/`.

### Confusables Decks

The confusables materials use distinction-oriented tags such as:

- `confusable::pair`
- `card::target`
- `card::confuser`
- `card::contrast`
- `pair::ermitteln_vermitteln`

These tags describe:

- the deck type
- the card role
- the specific lexical pair

These tags are typically used for finished decks under `anki/decks/confusables/`.

### Topic Vocabulary Decks

Many topic vocabulary decks use tags such as:

- `form::vokabel`
- `func::produktion`
- `level::c1_c2`
- `topic::ice_hockey`
- `source::raw::vocabulary::ice_hockey`
- `card::wort`
- `domain::taktik`

These tags describe:

- the exercise shape
- the intended review mode
- the level band
- the topic folder
- the source family
- the card shape
- an optional domain refinement

## Recommended Tag Layers

When creating a new deck, use only the tag layers that are actually useful for filtering and review.

Recommended order of importance:

1. deck or content type
2. level
3. pair or item identity
4. topic or domain
5. source
6. card role, only if the note design needs it

## Recommended Conventions By Deck Type

### General Pattern Drills

Use tags like:

- `form::...`
- `func::...`
- `topic::...`
- `level::...`
- `source::...`

Example:

```text
form::satzmuster func::beschreibung topic::gegenstände level::b2_c1 source::goethe::b2::k1
```

### Confusables

Use tags like:

- `confusable::pair`
- `pair::<item1>_<item2>`
- `card::target`
- `card::confuser`
- `card::contrast`
- optional `level::...`

Example:

```text
confusable::pair card::target pair::ermitteln_vermitteln
```

### Antonyms

Use tags like:

- `antonym::pair`
- `level::c1`
- optional `domain::...`

Example:

```text
antonym::pair level::c1 domain::abstract domain::argumentation
```

For antonyms, avoid `card::...` tags if one note generates multiple card directions automatically.
For antonyms, also avoid `pair::...` tags when they are too specific to support useful filtering.

## Pair Tag Normalization

Use the same normalization rule across pair-based decks:

- lowercase everything
- join the pair with `_`
- replace internal spaces with `-`
- keep German umlauts and `ß`

Examples:

- `explizit` + `implizit` -> `pair::explizit_implizit`
- `sich öffnen` + `sich verschließen` -> `pair::sich-öffnen_sich-verschließen`

## Practical Advice

- Do not try to tag every possible dimension.
- Prefer tags you will actually search or build filtered decks from.
- If a tag family is only used once, it probably does not need to exist.
- Keep new deck tags compatible with the existing namespace style instead of inventing a separate system.
- Keep the same namespace meaning across decks. For example, `topic::...` should remain a content topic, not a workflow stage or file origin.
- When a deck already lives in a highly specific folder, add only the tags that still help with filtering across folders.

## Recommendation

Yes, the tagging approach should be stored explicitly rather than only inferred from generated files.

This file should be the reference point for future prompt design and deck generation.
