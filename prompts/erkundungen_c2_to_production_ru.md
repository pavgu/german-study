# Erkundungen C2 To Russian-Led Production Cards

Use this workflow to extract important expressions and selected sentences from the chapter PDF ranges
in `reference/erkundungen/c2/Erkundungen_C2.pdf`.

Follow `docs/tagging.md` and import the finished deck with the note type documented in
`anki/note-types/production.md`.

## Normalized Source

Write one headerless TSV row per selected item under `anki/sources/c2/erkundungen/`:

1. exact or minimally normalized German target;
2. printed book page;
3. exercise or section identifier;
4. content type: `redewendung` or `satz`.

Use chapter filenames such as `K1_Sprache_und_Kommunikation.tsv`.

## Selection

Extract the shortest self-contained unit that preserves natural usage and meaning.

Prefer:

- idioms and fixed expressions;
- useful collocations and formal Redemittel;
- independently usable extracts;
- occasional complete sentences whose meaning or learning value depends on their context.

Exclude:

- exercise instructions and task boilerplate;
- elementary combinations that are not useful at C2;
- isolated words unless they belong to a fixed expression;
- repetitive grammatical examples;
- abstract sentence patterns with placeholders such as `X` and `Y`;
- long sentences whose main challenge is memorizing incidental wording.

Preserve articles, reflexive pronouns, prepositions, cases, and required complements. Convert an
inflected occurrence to a standard citation form only when needed to make an expression independently
learnable. Do not otherwise rewrite correct source wording.

## Finished Deck

Write one headerless TSV row per normalized source row under `anki/decks/erkundungen/c2/`:

1. Russian production prompt;
2. German answer;
3. short German hint;
4. Anki tags.

Use filenames such as `c2_erkundungen_k1_sprache_und_kommunikation_DE_RU.tsv`.

The German answer must match source column 1 exactly and remain in source order. The Russian prompt
must naturally and precisely cue that answer. The German hint should clarify meaning or usage without
repeating the target expression or an inflected form of its key words.

Use these tags:

- extracts: `form::redewendung func::produktion topic::<chapter_topic> level::c2 source::erkundungen::c2::k<chapter> card::chunk`
- sentences: `form::satz func::produktion topic::<chapter_topic> level::c2 source::erkundungen::c2::k<chapter> card::satz`

Do not use `form::satzmuster`.

## Validation

Check:

- exactly four non-empty fields in every source and deck row;
- one deck row for every source row;
- unique German targets unless repetition is intentional;
- exact source-to-deck German alignment and order;
- valid printed page and section references;
- consistent chapter tags and type-specific `form::`/`card::` tags;
- UTF-8, Unix newlines, and a final newline.
