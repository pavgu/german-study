# Confusables To Russian-Led Production Cards

Use this prompt to turn a raw TSV file of German confusable pairs into production-focused Anki cards with precise Russian prompts.

Recommended raw source:

- `anki/imports/raw/confusables/confusables_curated.txt`

Recommended default workflow:

- keep your broad capture list in `anki/imports/raw/confusables/confusables.txt`
- move stronger pairs into `anki/imports/raw/confusables/confusables_curated.txt`
- generate cards from the curated file by default

Recommended note type:

- [confusables-production-ru.md](/mnt/data/german-study/anki/note-types/confusables-production-ru.md)

## Goal

Starting from one raw TSV file where each row contains exactly 2 confusing German items, create Anki-ready production cards that:

- show a precise Russian prompt on the front
- require active recall of the correct German item
- make the contrast with the confusable explicit
- use careful, exact Russian wording

## Raw Input Format

Each non-empty row has exactly 2 tab-separated fields:

1. `Target`
2. `Confuser`

Example:

```tsv
ermitteln	vermitteln
meiden	vermeiden
```

## Output Format

For each input row, generate exactly 3 TSV rows with these columns:

1. `PromptRU`
2. `AnswerDE`
3. `HintDE`
4. Tags

The 3 rows per pair should be:

1. `card::target` -> prompt leads to `Target`
2. `card::confuser` -> prompt leads to `Confuser`
3. `card::contrast` -> prompt plus hint make the difference especially clear

## Output Path Recommendation

If tool access is available, write output under:

- `anki/decks/confusables/`

Suggested filename:

- `anki/decks/confusables/confusables_production_DE_RU.txt`

If tool access is not available, return the target path and the exact TSV rows.

## Prompt Template

```text
You are helping create Russian-led production Anki cards for confusing German words and expressions.

We will work from one raw TSV file at a time.

The raw file has exactly 2 tab-separated fields per non-empty row:
1. Target
2. Confuser

For each input row, create exactly 3 output TSV rows.

Output columns:
1. PromptRU
2. AnswerDE
3. HintDE
4. Tags

Card goal:
- The learner sees Russian and must produce the correct German item in a natural German sentence.
- The Russian must be precise enough to support the intended German answer.
- The front-side hint must help distinguish the confusable without giving away the full answer.

Rules for row 1:
- Build a Russian prompt that clearly leads to Target, not Confuser.
- Write one natural German answer sentence that uses Target correctly.
- Add a short German contrast hint suitable for the front of the card.
- Tag with `card::target`.

Rules for row 2:
- Build a Russian prompt that clearly leads to Confuser, not Target.
- Write one natural German answer sentence that uses Confuser correctly.
- Add a short German contrast hint suitable for the front of the card.
- Tag with `card::confuser`.

Rules for row 3:
- Create a contrast-heavy production card.
- The Russian prompt should strongly narrow the meaning.
- The German answer should use either Target or Confuser, whichever makes the sharpest contrast.
- The German hint must mention both items explicitly.
- Tag with `card::contrast`.

Russian prompt rules:
- Write natural Russian, not translationese.
- Be precise and semantically narrow.
- Prefer a short sentence over a single word if a single word would be ambiguous.
- If Russian has several possible renderings, choose the one that best isolates the target meaning.
- Avoid vague prompts that could fit both items.

German answer rules:
- Write one short natural German sentence.
- Use the target item in its correct form.
- Do not use cloze markup.
- Prefer realistic everyday or B2-relevant contexts.
- Keep syntax natural and unforced.
- Make case government, reflexive forms, separable prefixes, and collocations correct.
- The sentence should make the target meaning obvious in context.

HintDE rules:
- Keep it short and contrastive because it appears on the front of the card.
- Mention both items when useful.
- Prefer patterns like:
  - `Polizei -> ermitteln; Nachricht / Kontakt -> vermitteln`
  - `Person / Ort meiden; Risiko / Fehler vermeiden`
  - `kennen = familiar sein; wissen = Information haben`
- Avoid hints that simply restate the answer word by itself.

Tag rules:
- Add `confusable::pair`
- Add one of:
  - `card::target`
  - `card::confuser`
  - `card::contrast`

Quality rules:
- Do not guess sloppy Russian wording.
- If one Russian gloss is imprecise, rewrite the whole prompt more concretely.
- The Russian and German must match exactly in meaning.
- Prefer precision over stylistic variation.
- Do not use dictionary fragments as the main prompt when a sentence is clearer.
- Avoid prompts where both German items would be defensible.

Output rules:
- Return TSV rows only.
- Do not add headers.
- Do not add markdown, bullets, explanations, or code fences.
- Generate exactly 3 rows per input row.

Example input row:
ermitteln	vermitteln

Example output rows:
Полиция смогла быстро установить личность преступника.	Die Polizei konnte den Täter schnell ermitteln.	Polizei -> ermitteln; Nachricht / Kontakt -> vermitteln	confusable::pair card::target
Агентство помогло ему найти новую квартиру.	Die Agentur hat ihm eine neue Wohnung vermittelt.	Kontakt / Angebot -> vermitteln	confusable::pair card::confuser
Эту новость сразу передали по радио.	Im Radio wurde die Nachricht sofort vermittelt.	Polizei -> ermitteln; Nachricht -> vermitteln	confusable::pair card::contrast

When I send a raw file path and its TSV rows, convert that file only.
If you have file-writing tools, write the file and confirm with:
WROTE: <path>
If you do not have file-writing tools, return:
OUTPUT: <path>
followed by the TSV rows only.
```

## Recommended Use

- Use this prompt when your main review direction is `RU -> DE`.
- Review a small batch first to verify that the Russian prompts are precise enough.
- If a pair has more than one important sense, split it into separate rows later rather than forcing too much onto one card.
