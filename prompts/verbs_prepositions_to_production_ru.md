# Verb + Preposition To Russian-Led Production Cards

Use this prompt to turn a raw German file of `Verb + Präposition` combinations into an Anki-ready TSV import for the note type described in [production.md](/mnt/data/german-study/anki/note-types/production.md).

For tagging, follow the repository conventions documented in [tagging.md](/mnt/data/german-study/docs/tagging.md).

Recommended raw source pattern:

- `anki/imports/raw/grammar/<level>_verbs_prepositions_<date>.txt`

Current examples:

- `anki/imports/raw/grammar/b2_verbs_prepositions_2026-03-25.txt`
- `anki/imports/raw/grammar/c1_verbs_prepositions_2026-03-25.txt`
- `anki/imports/raw/grammar/c2_verbs_prepositions_2026-03-25.txt`

## Goal

Starting from one raw file where each non-empty line contains exactly one German `Verb + Präposition` combination, create an Anki-ready TSV for `German Production Prompt` notes.

The output must have exactly 4 tab-separated columns:

1. `PromptRU`
2. `AnswerDE`
3. `HintDE`
4. `Tags`

The learner should see a full Russian sentence, then produce a full German sentence that contains the exact target combination from the raw file.

## Recommended Output Path

If tool access is available, write the output file under:

- `anki/decks/grammar/`

Suggested filename pattern:

- raw: `anki/imports/raw/grammar/c1_verbs_prepositions_2026-03-25.txt`
- output: `anki/decks/grammar/c1_verbs_prepositions_production_DE_RU.txt`

If tool access is not available, return the target path and the exact TSV rows.

## Prompt Template

```text
You are helping create Russian-led Anki production cards for German Verb + Präposition combinations.

We will work from one raw file at a time.

Each non-empty input line contains exactly 1 German target combination.

Examples:
- bestehen auf
- sich interessieren für
- absehen von

For each non-empty input line, create exactly 1 TSV output row with these columns:
1. PromptRU
2. AnswerDE
3. HintDE
4. Tags

Goal:
- The learner sees a natural Russian sentence and must actively produce a natural full German sentence.
- The German answer sentence must contain the exact target Verb + Präposition combination from the raw file.
- The card should train productive command of the target combination, not just dictionary recognition.
- The output should be suitable for the note type "German Production Prompt".

Core rules:
- Preserve the target combination exactly as written in the raw line.
- Generate exactly 1 output row per non-empty input line.
- Prefer natural, modern, standard German and natural Russian.
- Prefer broadly standard German over regional variants unless the raw item itself is intentionally regional.
- If a raw target is clearly incomplete for standard use, for example because a required reflexive marker is missing, flag it for curation instead of silently generating around the problem.
- If a raw target is strongly regional and there is a clearly more standard equivalent, flag it for curation before generation.
- If a raw target is unusually marked, archaic, literary, or much less useful than a near-synonymous standard alternative already present in the same file, flag it for curation before generation instead of forcing a weak card.
- For advanced files, verify that the raw target is still genuinely a `Verb + Präposition` item, not a different pattern such as a genitive construction or a competing reflexive target already covered elsewhere in the file.
- Prefer short to medium-length sentences suitable for Anki review.
- Make the sentence specific enough that the target combination is clearly the intended answer.
- Avoid prompts that allow many equally natural German alternatives.
- Preserve reflexive forms exactly, for example:
  - `sich interessieren für`
  - `sich konzentrieren auf`
- Do not silently drop or add `sich` unless the raw file has first been curated.
- Preserve separable and non-separable verb behavior correctly in the final sentence.

Rules for PromptRU:
- Write one full natural Russian sentence.
- The prompt must cue the intended German combination strongly and specifically.
- The Russian should sound normal, not like a dictionary gloss.
- Prefer a context where the target Verb + Präposition is the clearest natural German solution.
- Make the Russian prompt precise enough to distinguish nearby alternatives such as:
  - `reden mit`
  - `sprechen mit`
  - `sich unterhalten mit`
- Keep the prompt concise and learner-friendly.
- Avoid making the Russian prompt so literal that it mechanically gives away the German structure.
- Make sure person, number, and gender match the German answer exactly.
- Make sure modal meaning also matches exactly, for example:
  - `пришлось`
  - `должен`
  - `может`
  should not disappear in the German answer.
- At C2 level, keep the Russian nuance exact:
  - `правота` is not the same as `невиновность`
  - `клясться чем-то` is not the same as `считать что-то особенно действенным`

Rules for AnswerDE:
- Write one full natural German sentence.
- The sentence must contain the exact target Verb + Präposition combination from the raw line.
- The target combination should appear in normal sentence form, with correct inflection and word order.
- Keep the sentence realistic and idiomatic.
- Usually use exactly one clear instance of the target combination.
- Do not use cloze markup.
- Do not hide the target preposition inside pronominal adverbs such as:
  - `davon`
  - `darauf`
  - `damit`
  when the learning goal is to reinforce the explicit `Verb + Präposition` combination.
- Prefer an explicit noun phrase after the preposition whenever possible, for example:
  - `von dieser Idee überzeugen`
  instead of
  - `davon überzeugen`
- If the target combination normally requires an object in natural German, include that object explicitly.
  Example:
  - prefer `einen Brief an jemanden schreiben`
  over an incomplete sentence like `an jemanden schreiben`
- Check agreement carefully in quantitative constructions such as:
  - `ein Drittel`
  - `die Hälfte`
  - `eine Reihe`
  because these often trigger avoidable verb-form mistakes.

Rules for HintDE:
- Write in German only.
- Usually keep the hint minimal.
- By default, use the target combination itself as the hint.
- Do not add case labels such as `+ Akk.` or `+ Dat.` in the hint.
- Do not add translation-like hint text unless the item would otherwise be too ambiguous.
- If an item is unusually ambiguous, you may add a very short disambiguating cue after the target combination, but keep it compact.

Rules for Tags:
- Use repo-style space-separated tags exactly in line with docs/tagging.md.
- Use lowercase tags only.
- Always add:
  - `form::grammar`
  - `func::produktion`
  - `topic::verbs_prepositions`
  - `level::<level-from-filename>`
- Keep the tag set lean with 3 to 4 tags total.
- Do not add `pair::...` tags for this deck type.
- Do not add `card::satz`, because all cards in this deck already share the same shape.
- Do not add `source::...` unless a later workflow specifically needs source filtering.

Level inference:
- Infer the level from the filename when possible:
  - `b2_verbs_prepositions_...` -> `level::b2`
  - `c1_verbs_prepositions_...` -> `level::c1`
  - `c2_verbs_prepositions_...` -> `level::c2`

Quality rules:
- The Russian prompt and the German answer sentence must match in meaning.
- The Russian prompt and the German answer must also match in grammatical details that matter for meaning, such as speaker reference and gender.
- Avoid near-duplicate cards where two different targets end up training almost the same meaning with only a register difference.
- If the raw file already contains a more standard target for a meaning, do not generate a second weaker row that teaches nearly the same thing less naturally.
- Do not let a non-reflexive target drift into a reflexive construction that is already represented elsewhere in the same deck.
- The sentence must clearly support the target combination rather than a generic synonym.
- Prefer contexts that make the preposition choice feel necessary.
- Avoid awkward textbook phrasing.
- Avoid sentences that are too abstract if a more concrete natural sentence is available.
- At higher levels, nuanced abstract contexts are welcome, but they should still sound like real German.
- If several German formulations are possible, choose the one that best reinforces the target combination.
- If a raw item is regionally marked or not ideal for broadly standard German, flag it mentally and prefer a more standard alternative only if the raw file has not fixed the wording already.
- Prefer idiomatic German syntax over literal Russian mirroring, even when preserving the same meaning.
- For C2 items, prefer fewer but cleaner cards over preserving every questionable raw target unchanged.

Output rules:
- Return tab-separated rows only.
- Do not add headers.
- Do not add markdown, bullets, numbering, or code fences.
- Generate exactly 1 row per non-empty input line.

Output behavior:
- If you have file-writing tools:
  - write the file
  - then confirm with one line starting with `WROTE: `
- If you do not have file-writing tools:
  - return the output path on a single line starting with `OUTPUT: `
  - then return the TSV rows only

Example input path:
anki/imports/raw/grammar/c1_verbs_prepositions_2026-03-25.txt

Example input lines:
bestehen auf
sich interessieren für
absehen von

Example output if file-writing tools are not available:
OUTPUT: anki/decks/grammar/c1_verbs_prepositions_production_DE_RU.txt
Он настаивает на немедленном решении.	Er besteht auf einer sofortigen Entscheidung.	bestehen auf	form::grammar func::produktion topic::verbs_prepositions level::c1
Она давно интересуется современной немецкой литературой.	Sie interessiert sich seit Langem für moderne deutsche Literatur.	sich interessieren für	form::grammar func::produktion topic::verbs_prepositions level::c1
В этой ситуации нам придется отказаться от первоначального плана.	In dieser Situation müssen wir von dem ursprünglichen Plan absehen.	absehen von	form::grammar func::produktion topic::verbs_prepositions level::c1

When I send a raw file path and its raw lines, convert that file only.
After finishing one file, wait for the next raw file.
```

## Recommended Use

- Start with a small batch and spot-check sentence quality before generating a full file.
- Prefer prompts that force the target combination naturally instead of relying on grammar labels.
- If a target remains too ambiguous even with a full sentence, rewrite the prompt rather than making the hint heavy.
- Keep the hint minimal so the main recall work still happens through the Russian sentence.
- For borderline C2 items, prefer especially natural register-appropriate contexts before accepting the generated card.
