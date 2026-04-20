# Confusables To Anki Prompt

Use this prompt to turn a raw TSV file of confusing German words into Anki-ready study rows.

This workflow is for cases like:

- `ermitteln` vs `vermitteln`
- `meiden` vs `vermeiden`
- `erinnern` vs `sich erinnern`

The raw source file should live under `anki/sources/confusables/`.

The simplest setup is to keep one master raw file for everything:

- `anki/sources/confusables/confusables.txt`

New source files may use `.tsv` if you want to follow the repo's preferred extension.

## Goal

Starting from one raw TSV file of confusable words or short expressions, create one or more Anki-ready TSV outputs that help distinguish the items in active use.

Prefer cards that force discrimination between similar items, not just dictionary recall.

## Recommended Raw Input Format

Each non-empty row should have exactly 2 tab-separated fields:

1. `Target` -> the main word or expression
2. `Confuser` -> the similar word or expression

Example:

```tsv
ermitteln	vermitteln
meiden	vermeiden
```

## Output Design

For each input row, generate 3 output rows for a production-oriented cloze note type with these columns:

1. German sentence with exactly one cloze deletion
2. Cue
3. Translation
4. Tags

The 3 rows per pair should be:

1. A sentence where `Target` is the correct answer
2. A sentence where `Confuser` is the correct answer
3. A contrast card whose cue explicitly compares the two items

The model should infer the meaning contrast from the pair itself.

## Output Path Recommendation

If tool access is available, write the output file under:

- `anki/decks/confusables/`

Suggested filename pattern:

- raw: `anki/sources/confusables/confusables.txt`
- output: `anki/decks/confusables/confusables_cloze.tsv`

If tool access is not available, return the exact TSV content and target path.

## Prompt Template

```text
You are helping create Anki cards for confusing German words and expressions.

We will work from one raw TSV file at a time.

The raw file has 2 tab-separated fields per non-empty row:
1. Target
2. Confuser

For each input row, create exactly 3 output TSV rows for Anki.

Output columns:
1. German sentence with exactly one cloze deletion
2. Cue
3. English or Russian translation that matches the sentence
4. Tags

Card design rules:
- The cards must help the learner distinguish Target from Confuser.
- Infer the semantic contrast from the pair itself.
- Prefer concrete, natural, high-frequency sentences.
- Avoid abstract dictionary-style wording when a concrete sentence is possible.
- Make the contrast obvious from context.
- Test one distinction at a time.
- Keep the sentence short enough for Anki review.

Rules for row 1:
- Use Target as the cloze answer.
- The sentence should strongly support Target, not Confuser.
- The cue should briefly explain why Target fits.

Rules for row 2:
- Use Confuser as the cloze answer.
- The sentence should strongly support Confuser, not Target.
- The cue should briefly explain why Confuser fits.

Rules for row 3:
- Make a contrast-focused card.
- Use either Target or Confuser as the cloze answer, whichever makes the clearest sentence.
- The cue must explicitly mention both items, for example:
  - `Polizei -> ermitteln; Kontakt / Nachricht -> vermitteln`
  - `Person / Ort meiden; Risiko / Fehler vermeiden`
- The translation must match the final German sentence.

Sentence rules:
- Every output sentence must contain exactly one cloze deletion.
- Use Anki cloze format like `{{c1::ermitteln}}`.
- Keep grammar fully natural.
- Preserve separable verbs, reflexive forms, and case government correctly.
- If one item is much rarer or stylistically marked, prefer a sentence that reflects normal usage.
- If the pair is not truly interchangeable, make the difference clear in the cue.

Cue rules:
- Keep cues short, usually 3 to 10 words.
- Use simple learner-facing wording.
- Prefer contrastive hints over dictionary definitions.
- Do not just repeat the translation.

Translation rules:
- Keep the translation concise and natural.
- It must match the final sentence exactly.

Tags rules:
- Add one of these tags:
  - `card::target`
  - `card::confuser`
  - `card::contrast`
- Add normalized pair tags when useful, for example:
  - `pair::ermitteln_vermitteln`
- Add a general topic tag such as `confusable::pair`

Output rules:
- Return tab-separated rows only.
- Do not add headers.
- Do not add bullets, explanations, markdown, or code fences.
- Generate exactly 3 rows per input row.

Example input row:
ermitteln	vermitteln

Example output rows:
Die Polizei konnte den Täter schnell {{c1::ermitteln}}.	Polizei / Täter finden	to identify the perpetrator quickly	confusable::pair card::target pair::ermitteln_vermitteln
Die Agentur hat ihm eine neue Wohnung {{c1::vermittelt}}.	Kontakt / Angebot organisieren	to arrange a new apartment for him	confusable::pair card::confuser pair::ermitteln_vermitteln
Im Radio wurde die Nachricht sofort {{c1::vermittelt}}.	Polizei -> ermitteln; Nachricht -> vermitteln	The message was conveyed immediately on the radio.	confusable::pair card::contrast pair::ermitteln_vermitteln

When I send a raw file path and its TSV rows, convert that file only.
If you have file-writing tools, write the output file and confirm with:
WROTE: <path>
If you do not have file-writing tools, return:
OUTPUT: <path>
followed by the TSV rows only.
```

## Recommended Use

- A single master file such as `anki/sources/confusables/confusables.txt` is recommended unless you later want to split by topic.
- Start small and review quality before generating very large batches.
- If a row contains more than 2 confusable items, split it into multiple pair rows.
- Prefer pairs that you genuinely confuse in production or reading.
