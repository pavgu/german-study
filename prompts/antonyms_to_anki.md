# Antonyms To Anki Prompt

Use this prompt to turn a raw TSV file of German antonym pairs into an Anki-ready TSV import for the note type described in [antonyms-production-ru.md](/mnt/data/german-study/anki/note-types/antonyms-production-ru.md).

For tagging, follow the repository conventions documented in [tagging.md](/mnt/data/german-study/docs/tagging.md).

The raw source file should live under `anki/imports/raw/antonyms/`.

Recommended source file:

- `anki/imports/raw/antonyms/c1_antonyms_2026-03-20.txt`

## Goal

Starting from one raw TSV file of German antonym pairs, create an Anki-ready TSV that supports both:

- direct recall of the pair
- Russian-led production of each antonym in a full German sentence

The output must match the custom note type with these fields:

1. `Antonym1DE`
2. `Antonym2DE`
3. `PromptAntonym1RU`
4. `PromptAntonym2RU`
5. `AnswerAntonym1DE`
6. `AnswerAntonym2DE`
7. `Tags`

## Recommended Raw Input Format

Each non-empty row should have exactly 2 tab-separated fields:

1. `Antonym1DE`
2. `Antonym2DE`

Example:

```tsv
explizit	implizit
präzise	vage
```

## Output Design

For each input row, generate exactly 1 output TSV row with 7 columns:

1. `Antonym1DE`
2. `Antonym2DE`
3. `PromptAntonym1RU`
4. `PromptAntonym2RU`
5. `AnswerAntonym1DE`
6. `AnswerAntonym2DE`
7. `Tags`

Each row should make both antonyms usable in context, not just recognizable as a dictionary pair.

## Output Path Recommendation

If tool access is available, write the output file under:

- `anki/decks/antonyms/`

Suggested filename pattern:

- raw: `anki/imports/raw/antonyms/c1_antonyms_2026-03-20.txt`
- output: `anki/decks/antonyms/c1_antonyms_production_DE_RU.txt`

If tool access is not available, return the exact TSV content and target path.

## Prompt Template

```text
You are helping create Anki cards for German antonym pairs.

We will work from one raw TSV file at a time.

The raw file has 2 tab-separated fields per non-empty row:
1. Antonym1DE
2. Antonym2DE

For each input row, create exactly 1 output TSV row with these columns:
1. Antonym1DE
2. Antonym2DE
3. PromptAntonym1RU
4. PromptAntonym2RU
5. AnswerAntonym1DE
6. AnswerAntonym2DE
7. Tags

Goal:
- Build cards for the custom note type "German Antonyms Production RU".
- The learner should be able to study the antonym pair itself and also produce each word from a short Russian prompt.

General rules:
- Keep the original German pair unchanged in columns 1 and 2.
- Treat both sides as equally important.
- Prefer natural, idiomatic, modern standard German.
- Prefer short, memorable, high-value sentences suitable for Anki review.
- Keep the Russian prompts concise and specific.
- Make the sentence context strongly support the intended antonym.
- Avoid prompts that are near-literal translations of the answer sentence.
- If a pair is conceptual rather than absolute, choose contexts where the contrast feels natural and useful.
- Preserve reflexive forms, separable prefixes, case government, adjective endings, and collocations correctly.

Rules for PromptAntonym1RU and PromptAntonym2RU:
- Write one short natural Russian sentence for each antonym.
- The prompt must strongly cue the intended German antonym.
- The prompt should make the opposite word feel wrong or much less natural in that context.
- Keep prompts learner-friendly and concrete whenever possible.
- Avoid simply inserting a Russian cognate that gives away the German answer.

Rules for AnswerAntonym1DE and AnswerAntonym2DE:
- Write one full natural German sentence for each antonym.
- The sentence must contain the exact antonym from the pair.
- Use each antonym in a realistic context.
- Do not use cloze format.
- Keep the answer sentence closely aligned with the meaning of its Russian prompt.
- Prefer one clear target word use per sentence.

Quality rules:
- Do not make the two prompts artificially parallel if natural German usage differs.
- If one antonym is stylistically marked or more abstract, choose a context where it sounds normal.
- Avoid awkward textbook phrasing.
- Avoid extremely similar answer sentences unless contrast is the learning goal.
- At C1 level, nuanced abstract examples are welcome, but they should still sound natural.

Tags rules:
- Use repo-style space-separated tags exactly in line with `docs/tagging.md`.
- Always add:
  - `antonym::pair`
  - `level::c1`
- Add one normalized pair tag:
  - `pair::<antonym1>_<antonym2>`
- Add 1 to 3 topic or usage tags when clearly helpful, for example:
  - `domain::abstract`
  - `domain::argumentation`
  - `domain::society`
  - `domain::behavior`
  - `domain::style`
- Use lowercase tags.
- Replace spaces inside pair items with hyphens when needed.
- Do not add card-direction tags, because one note already generates multiple card types.

Normalization rules for pair tags:
- Keep German spelling in lowercase.
- Replace spaces with hyphens.
- Keep umlauts and ß.
- Example:
  - `sich öffnen` + `sich verschließen` -> `pair::sich-öffnen_sich-verschließen`

Output rules:
- Return tab-separated rows only.
- Do not add headers.
- Do not add bullets, explanations, markdown, or code fences.
- Generate exactly 1 row per input row.

Example input row:
explizit	implizit

Example output row:
explizit	implizit	Он сформулировал это требование совершенно прямо.	Критика звучала не прямо, а только между строк.	Er formulierte diese Forderung ganz explizit.	Die Kritik blieb implizit und wurde nur zwischen den Zeilen deutlich.	antonym::pair level::c1 pair::explizit_implizit domain::abstract domain::argumentation

When I send a raw file path and its TSV rows, convert that file only.
If you have file-writing tools, write the output file and confirm with:
WROTE: <path>
If you do not have file-writing tools, return:
OUTPUT: <path>
followed by the TSV rows only.
```

## Recommended Tag Approach

Treat [tagging.md](/mnt/data/german-study/docs/tagging.md) as the source of truth for tag design.

For antonyms, prefer:

- `antonym::pair`
- `level::c1`
- `pair::<normalized_pair>`
- optional topical tags like `domain::abstract`

Do not invent a parallel tagging scheme for this deck. Keep antonym tags compatible with the namespace-based approach already documented for the repo.

## Recommended Use

- Start with a smaller batch and review sentence quality before generating the full file.
- Keep prompts specific enough to force lexical choice.
- If a pair feels too loose, rewrite the prompts to emphasize contrasting contexts rather than removing the pair immediately.
- After generation, spot-check difficult or abstract pairs for naturalness before import.
