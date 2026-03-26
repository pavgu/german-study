# Antonyms To Anki Prompt

Use this prompt to turn a raw TSV file of German antonym pairs into an Anki-ready TSV import for the note type described in [antonyms-production-ru.md](/mnt/data/german-study/anki/note-types/antonyms-production-ru.md).

For tagging, follow the repository conventions documented in [tagging.md](/mnt/data/german-study/docs/tagging.md).

The raw source file should live under `anki/imports/raw/antonyms/`.

Recommended source file:

- `anki/imports/raw/antonyms/c1_antonyms_2026-03-20.txt`

## Goal

Starting from one raw TSV file of German antonym pairs, create an Anki-ready TSV that supports all of the following:

- direct recall of the pair
- short German-definition recall for each individual word
- Russian-led production of each antonym in a full German sentence

The output must match the custom note type with these fields:

1. `Antonym1DE`
2. `Antonym2DE`
3. `DefinitionAntonym1DE`
4. `DefinitionAntonym2DE`
5. `PromptAntonym1RU`
6. `PromptAntonym2RU`
7. `AnswerAntonym1DE`
8. `AnswerAntonym2DE`
9. `Tags`

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

For each input row, generate exactly 1 output TSV row with 9 columns:

1. `Antonym1DE`
2. `Antonym2DE`
3. `DefinitionAntonym1DE`
4. `DefinitionAntonym2DE`
5. `PromptAntonym1RU`
6. `PromptAntonym2RU`
7. `AnswerAntonym1DE`
8. `AnswerAntonym2DE`
9. `Tags`

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
3. DefinitionAntonym1DE
4. DefinitionAntonym2DE
5. PromptAntonym1RU
6. PromptAntonym2RU
7. AnswerAntonym1DE
8. AnswerAntonym2DE
9. Tags

Goal:
- Build cards for the custom note type "German Antonyms Production RU".
- The learner should be able to study the antonym pair itself, recall each word from a short German definition, and produce each word from a short Russian prompt.

General rules:
- Keep the original German pair unchanged in columns 1 and 2.
- Fields 1 and 2 must use the dictionary headword or lemma, not an inflected form from the answer sentence.
- Treat both sides as equally important.
- Prefer natural, idiomatic, modern standard German.
- Prefer colloquial everyday wording when it sounds natural for the meaning; do not make the German sound literary, bureaucratic, translated, or textbook-like unless the target word itself belongs to that register.
- Prefer compact German definitions that isolate the meaning of each word.
- Prefer short, memorable, high-value sentences suitable for Anki review.
- Keep the Russian prompts concise and specific.
- Make the sentence context strongly support the intended antonym.
- Avoid prompts that are near-literal translations of the answer sentence.
- If a pair is conceptual rather than absolute, choose contexts where the contrast feels natural and useful.
- Preserve reflexive forms, separable prefixes, case government, adjective endings, and collocations correctly.

Rules for DefinitionAntonym1DE and DefinitionAntonym2DE:
- Field 3 must be a short German paraphrase or description of the word in field 1.
- Field 4 must be a short German paraphrase or description of the word in field 2.
- Write one short German paraphrase for each antonym.
- Use simple, idiomatic German that a native speaker would actually say when explaining the word.
- The definition should strongly point to the intended word, not to both words equally.
- Do not define one word only as the negation of the other.
- Prefer meaning-based cues over register labels alone.
- Keep the definition compact enough to work as an Anki front side.
- Avoid stiff dictionary wording if a more colloquial paraphrase is possible.
- Do not turn the definition field into a sentence with the target word blanked out.
- Do not reuse the answer sentence with one word removed.
- Do not write mini-cloze prompts in these fields.
- These fields are lexical descriptions, not contextual gap-fill cues.
- Good:
  - `explizit` -> `klar und direkt ausgedrückt`
  - `implizit` -> `nicht direkt gesagt, aber gemeint`
- Also good:
  - `zulässig` -> `nach den Regeln erlaubt`
  - `stichhaltig` -> `gut begründet und überzeugend`
- Bad:
  - `implizit` -> `nicht explizit`
- Bad:
  - `Das Auswahlverfahren muss ... sein.`
  - `Die Mehrheit ... diese Reform.`
  - `Gegenteil von unflexibel`

Rules for PromptAntonym1RU and PromptAntonym2RU:
- Write one short natural Russian sentence for each antonym.
- Prefer idiomatic modern Russian over formal or dictionary-like wording.
- The prompt must strongly cue the intended German antonym.
- The prompt should make the opposite word feel wrong or much less natural in that context.
- Keep prompts learner-friendly and concrete whenever possible.
- Avoid simply inserting a Russian cognate that gives away the German answer.
- Avoid vague prompts that describe only a broad semantic area instead of the exact lexical choice.
- Prefer prompts that suggest the target word through situation, collocation, tone, or implication rather than by direct translation.
- Keep the same actor, situation, and sentence type as the German answer whenever possible; do not turn a statement into an instruction or shift to a different event.

Rules for AnswerAntonym1DE and AnswerAntonym2DE:
- Write one full natural German sentence for each antonym.
- The sentence must contain the exact antonym from the pair.
- Use each antonym in a realistic context.
- Do not use cloze format.
- Keep the answer sentence closely aligned with the meaning of its Russian prompt.
- Prefer one clear target word use per sentence.
- Prefer German collocations that are common and idiomatic.
- If two grammatically correct options exist, choose the one a native speaker is more likely to say in everyday educated usage.
- Avoid overengineered written-style syntax when a simpler colloquial sentence would sound better.
- Make sure the target word fits naturally with the noun, verb, or subject it modifies.
- Do not force a formally possible but unusual collocation if a more idiomatic sentence is available.
- If a sentence sounds merely acceptable but not like something a native speaker would normally say, rewrite it.

Quality rules:
- Do not make the two prompts artificially parallel if natural German usage differs.
- If one antonym is stylistically marked or more abstract, choose a context where it sounds normal.
- Avoid awkward textbook phrasing.
- Avoid translations that are semantically correct but lexically off.
- Check that the German sentence sounds like an original German sentence, not a translation from Russian.
- Check that the Russian prompt sounds like an original Russian cue, not a gloss of the German answer.
- Check that the Russian cue and the German answer match not only in general meaning but also in perspective, for example `wirkt` versus `fühlt sich`, person versus thing, process versus result.
- Check that the Russian prompt also sounds natural in Russian and not just semantically serviceable.
- Avoid extremely similar answer sentences unless contrast is the learning goal.
- At C1 level, nuanced abstract examples are welcome, but they should still sound natural.

Lexical precision check for every row:
- Ask whether the Russian prompt points to this exact word, not just to the general idea.
- Ask whether the German definition excludes the opposite word clearly enough.
- Ask whether the German answer uses a natural collocation for this word.
- Ask whether fields 3 and 4 are genuine paraphrases, not gap sentences.
- Ask whether fields 1 and 2 are lemmas rather than inflected sentence forms.
- If the sentence feels correct but slightly stiff, rewrite it in more idiomatic German.
- If the Russian feels like a translation prompt rather than a real cue, rewrite it.

Preference hierarchy:
- 1. precise meaning
- 2. idiomatic and colloquial German
- 3. natural Russian cueing
- 4. brevity
- 5. symmetry between the two sides

Tags rules:
- Use repo-style space-separated tags exactly in line with `docs/tagging.md`.
- Always add:
  - `antonym::pair`
  - `level::c1`
- Add 1 to 3 topic or usage tags when clearly helpful, for example:
  - `domain::abstract`
  - `domain::argumentation`
  - `domain::society`
  - `domain::behavior`
  - `domain::style`
- Use lowercase tags.
- Do not add card-direction tags, because one note already generates multiple card types.
- Do not add `pair::...` tags for antonyms, because they are usually too specific to help with filtering or review.

Output rules:
- Return tab-separated rows only.
- Do not add headers.
- Do not add bullets, explanations, markdown, or code fences.
- Generate exactly 1 row per input row.

Example input row:
explizit	implizit

Example output row:
explizit	implizit	klar und direkt ausgedrückt	nicht direkt gesagt, aber gemeint	Он сформулировал это требование совершенно прямо.	Критика звучала не прямо, а только между строк.	Er formulierte diese Forderung ganz explizit.	Die Kritik blieb implizit und wurde nur zwischen den Zeilen deutlich.	antonym::pair level::c1 domain::abstract domain::argumentation

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
- optional topical tags like `domain::abstract`

Do not invent a parallel tagging scheme for this deck. Keep antonym tags compatible with the namespace-based approach already documented for the repo.

## Recommended Use

- Start with a smaller batch and review sentence quality before generating the full file.
- Review the German definitions first. If both words could fit, rewrite the definition.
- Keep prompts specific enough to force lexical choice.
- If a pair feels too loose, rewrite the prompts to emphasize contrasting contexts rather than removing the pair immediately.
- After generation, spot-check difficult or abstract pairs for naturalness before import.
