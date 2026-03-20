# Topic Vocabulary To Russian-Led Production Cards

Use this prompt to turn a raw German-only topic vocabulary file into an Anki-ready TSV import for the note type described in [production.md](/mnt/data/german-study/anki/note-types/production.md).

For tagging, follow the repository conventions documented in [tagging.md](/mnt/data/german-study/docs/tagging.md).

Recommended raw source pattern:

- `anki/imports/raw/vocabulary/<topic>/<filename>.txt`

Current example:

- `anki/imports/raw/vocabulary/ice_skating/c1_c2_ice_skating_2026-03-20.txt`

## Goal

Starting from one raw file where each non-empty line contains exactly one German item, create an Anki-ready TSV for `German Production Prompt` notes.

The raw lines may contain:

- single words
- short chunks or collocations
- short full sentences

The output must have exactly 4 tab-separated columns:

1. `PromptRU`
2. `AnswerDE`
3. `HintDE`
4. `Tags`

## Recommended Output Path

If tool access is available, write the output file under:

- `anki/decks/vocabulary/<topic>/`

Suggested example output:

- raw: `anki/imports/raw/vocabulary/ice_skating/c1_c2_ice_skating_2026-03-20.txt`
- output: `anki/decks/vocabulary/ice_skating/c1_c2_ice_skating_production_DE_RU.txt`

If tool access is not available, return the target path and the exact TSV rows.

## Prompt Template

```text
You are helping create Russian-led Anki production cards from a raw German topic vocabulary file.

We will work from one raw file at a time.

Each non-empty input line contains exactly 1 German item.
The item may be:
- a single word
- a short chunk or collocation
- a short full sentence

For each non-empty line, create exactly 1 TSV output row with these columns:
1. PromptRU
2. AnswerDE
3. HintDE
4. Tags

Goal:
- The learner sees a Russian prompt and must actively produce the exact German item from the raw file.
- The hint must help recall the target in German without reusing the same wording.
- The output should be suitable for the note type "German Production Prompt".

Core rules:
- Preserve the German item exactly in column 2 unless there is an obvious typo in the raw line.
- Generate exactly 1 output row per non-empty input line.
- Keep the content useful for active recall, not for passive recognition only.
- Prefer precise, natural, modern standard German and natural Russian.
- Keep the rows concise and import-ready.

Rules for PromptRU:
- Write natural Russian.
- Make the prompt specific enough that the intended German answer is clear.
- For single words, prefer a short Russian phrase or sentence rather than a bare dictionary gloss when needed for precision.
- For chunks, write a Russian prompt that cues the expression as a usable phrase.
- For full sentences, write a natural Russian sentence that closely matches the German meaning.
- Avoid overly vague prompts that could fit many different German answers.
- Avoid adding extra information that is not present in the German target.

Rules for AnswerDE:
- Copy the German item from the raw line exactly.
- Do not add cloze markup.
- Do not rewrite correct wording just for style.

Rules for HintDE:
- Write in German only.
- The hint must not repeat the target wording and must not use the same key words as the answer.
- The hint should describe the meaning, usage, function, or context in a learner-friendly way.
- Prefer a short paraphrase, semantic cue, or situational explanation.
- Usually keep the hint to about 2 to 8 words.
- For a single word, prefer a near-synonym, plain-German explanation, or usage cue.
- For a chunk, describe when or why one would say it.
- For a full sentence, summarize the communicative intent in different words.
- Do not simply translate the answer into German again.
- Do not include the answer word inside the hint in inflected or base form.

Rules for Tags:
- Use repo-style space-separated tags exactly in line with docs/tagging.md.
- Use lowercase tags only.
- Always add:
  - `form::vokabel`
  - `func::produktion`
  - `level::<level-from-filename-or-path>`
  - `topic::<normalized-topic>`
  - `source::raw::vocabulary::<normalized-topic>`
- Add one card-shape tag based on the line type:
  - `card::wort`
  - `card::chunk`
  - `card::satz`
- Add one helpful domain tag when clearly appropriate, for example:
  - `domain::sport`
  - `domain::eissport`
  - `domain::technik`
  - `domain::wettkampf`
- Infer the topic from the folder name when possible.
- Infer the level from the filename when possible, such as:
  - `c1_c2`
  - `c1`
  - `b2_c1`
- Normalize topic tags like this:
  - lowercase
  - keep underscores if the folder name uses them
  - example: `ice_skating` -> `topic::ice_skating`
- Do not invent unnecessary extra tags.
- Keep the tag set stable across the file.

Line type classification:
- `card::wort` for a single lexical item such as `die Kufe`
- `card::chunk` for a phrase, collocation, or sentence fragment such as `die Landung sicher ausfahren`
- `card::satz` for a full sentence ending in sentence punctuation or clearly functioning as a complete sentence

Quality rules:
- The Russian prompt and the German answer must match in meaning exactly.
- The hint must be genuinely helpful for recall.
- The hint must not give away the answer by repeating its wording.
- Prefer memorable prompts over dictionary-style labels.
- Keep answer sentences short if the raw item is a sentence.
- Do not add headers.
- Do not add markdown, bullets, numbering, or code fences.
- Return tab-separated rows only.
- Skip empty lines.

Output behavior:
- If you have file-writing tools:
  - write the file
  - then confirm with one line starting with `WROTE: `
- If you do not have file-writing tools:
  - return the output path on a single line starting with `OUTPUT: `
  - then return the TSV rows only

Example input path:
anki/imports/raw/vocabulary/ice_skating/c1_c2_ice_skating_2026-03-20.txt

Example input lines:
die Kufe
die Landung stabil ausfahren
Die Kür war technisch stark und künstlerisch klar.

Example output if file-writing tools are not available:
OUTPUT: anki/decks/vocabulary/ice_skating/c1_c2_ice_skating_production_DE_RU.txt
лезвие конька	die Kufe	Metallteil am Schuh	form::vokabel func::produktion level::c1_c2 topic::ice_skating source::raw::vocabulary::ice_skating card::wort domain::eissport
уверенно выйти из приземления	die Landung stabil ausfahren	nach dem Sprung sicher weitergleiten	form::vokabel func::produktion level::c1_c2 topic::ice_skating source::raw::vocabulary::ice_skating card::chunk domain::technik
Программа была технически сильной и художественно ясной.	Die Kür war technisch stark und künstlerisch klar.	Programm wirkt sportlich und gestalterisch überzeugend	form::vokabel func::produktion level::c1_c2 topic::ice_skating source::raw::vocabulary::ice_skating card::satz domain::wettkampf

When I send a raw file path and its raw lines, convert that file only.
After finishing one file, wait for the next raw file.
```

## Recommended Use

- Start with a small sample and check whether the Russian prompts are precise enough.
- Spot-check hints to ensure they do not reuse the target wording.
- For mixed files like topic vocabulary lists, keep the same tag backbone for all rows and vary only `card::...` and the most useful `domain::...` tag.
- If a raw item is too broad for a precise Russian prompt, rewrite the prompt as a short situational cue rather than a one-word gloss.
