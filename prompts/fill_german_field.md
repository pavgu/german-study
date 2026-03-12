# Raw To DE-RU Production Prompt

Use this prompt with ChatGPT to convert raw source files directly, without using a script to insert the new TSV field first.

If the ChatGPT session has file-writing or agent tools, it should write the converted file directly.
If it does not have file-writing tools, it should return the exact TSV content intended for the converted file so it can be saved without further editing.

## Goal

Starting from raw 3-column TSV files in a source directory such as `data/raw/b2/goethe/`, create one converted 4-column TSV file for each raw file.

The converted file should:

- keep the same folder structure under `data/converted/`
- keep the same filename pattern, but change `_RU` to `_DE_RU`
- contain 4 TSV fields per row

Output columns:

1. German sentence with one useful production-focused cloze deletion
2. German synonym or short German explanation for that one cloze target
3. Russian translation aligned with the final German sentence
4. original Anki tags

## Step-By-Step Workflow

Use the prompt below at the start of a ChatGPT session.

Then work file by file:

1. Give ChatGPT the raw file path and paste the raw TSV rows from that file.
2. Let ChatGPT write the converted file directly if tool access is available.
3. If tool access is not available, let ChatGPT return the target converted path and the full converted TSV content for that file.
4. Continue with the next raw file in the same directory.

## Prompt Template

```text
You are helping convert raw Anki-style German learning files into DE-RU Anki production cards.

We will work through all files in one raw source directory step by step.

Source directory example:
data/raw/b2/goethe/

For each raw file I send, do the following:

1. Derive the output path by mirroring the raw folder structure under `data/converted/`.
2. Change the filename from `*_RU.txt` to `*_DE_RU.txt`.
3. Convert every non-empty input row from 3 TSV fields to 4 TSV fields.
4. If you have file-writing tools, write the converted TSV directly to the target path.
5. If you do not have file-writing tools, return the exact converted TSV content for that target path.

Raw input columns:
1. German sentence with cloze deletions
2. Russian translation
3. Anki tags

Output columns:
1. German sentence, revised when needed for better production practice
2. New German synonym or short German explanation for the one cloze target
3. Russian translation, revised if needed
4. Same original Anki tags

Rules for rewriting the German sentence:
- Each output row must contain exactly one cloze deletion.
- Keep one primary production-relevant cloze only.
- If the input sentence has multiple cloze deletions, choose the best one and remove cloze markup from all other words or phrases.
- Prefer `Redemittel` first: sentence starters, discourse markers, reporting phrases, opinion phrases, request phrases, summary phrases, and other reusable B2 chunks.
- Choose a single word only when there is no strong phrase-level target.
- If the sentence already has a useful learner-relevant cloze, keep it.
- If the sentence contains an empty or placeholder cloze such as `{{c1::…}}` or `{{c1::...}}`, rewrite the sentence.
- Remove the placeholder cloze.
- Choose another useful word or short part of the sentence and mark it as the cloze.
- The new cloze should be valuable for active B2 production: especially reusable phrases and `Redemittel`, and secondarily useful vocabulary or collocations.
- Keep the sentence as close to the original as possible.
- Keep the sentence natural German.
- Field 2 must explain that one cloze target only.
- Prefer a concrete, usable sentence over an abstract pattern with `...`.
- If the sentence contains slash alternatives, rewrite it into one clear natural sentence unless the alternatives are essential.
- Avoid low-value cloze targets by default, especially isolated function words such as `dass`, `diesem`, `würde`, or bare numbers, unless they are part of a larger reusable phrase.
- Prefer lexical or phrase-level targets over grammar-only targets.
- Avoid overly long cloze spans when a shorter useful target is possible.
- Good cloze targets include expressions such as `In diesem Text geht es um`, `Ich würde mich freuen`, `Zusammenfassend kann man sagen, dass`, `Für mich ist es wichtig, dass`, `Ich habe mir vorgenommen`.

Rules for field 2:
- Write in German only.
- Use a synonym or a short explanation in simple German.
- Prefer B1-B2 wording.
- Keep it short, usually 1-5 words.
- Focus on the one final chosen cloze item.
- If the best choice is a phrase, keep it short.
- Do not copy the Russian translation into field 2.
- Field 2 must match the surviving cloze exactly.
- Do not explain a removed cloze.
- Prefer one consistent style: either a close synonym or a short plain-German explanation.
- Avoid mixed note style such as `X = Y` unless truly necessary.
- Do not add comments, markdown, bullets, numbering, or code fences.

Rules for field 3:
- If the Russian translation is still correct after the cloze rewrite, keep it.
- If the original translation depended on `...` or a placeholder cloze, rewrite the Russian translation so it matches the revised German sentence.
- Keep the translation natural and concise.
- Make sure the translation reflects the final concrete sentence, not the old pattern.

Rules for the full output:
- If you have file-writing tools:
  - write the file
  - then confirm with one line starting with `WROTE: `
- If you do not have file-writing tools:
  - return the output path on a single line starting with `OUTPUT: `
  - then return the converted TSV rows only
- Keep tab-separated formatting.
- Do not add a header row.
- Skip empty lines from the input.
- Preserve field 4 exactly.
- Make sure every output sentence has exactly one `{{c...::...}}` cloze.
- Optimize for Anki production practice, not for a monolingual dictionary entry.

Example raw input path:
data/raw/b2/goethe/K1_RM_RU.txt

Example expected output path:
data/converted/b2/goethe/K1_RM_DE_RU.txt

Example raw input rows:
Mein {{c1::wichtigster}} Gegenstand ist {{c2::…}}.	Мой самый важный предмет — это …	form::satzmuster func::beschreibung topic::gegenstände level::b2_c1 source::goethe::b2::k1
… war ein {{c1::Geschenk}} von {{c2::…}}.	… был подарком от …	form::satzmuster func::beschreibung topic::gegenstände level::b2_c1 source::goethe::b2::k1

Example output if file-writing tools are not available:
OUTPUT: data/converted/b2/goethe/K1_RM_DE_RU.txt
Mein {{c1::wichtigster}} Gegenstand ist mein Laptop.	entscheidendster / am wichtigsten	Мой самый важный предмет - это мой ноутбук.	form::satzmuster func::beschreibung topic::gegenstände level::b2_c1 source::goethe::b2::k1
Mein Fahrrad war ein {{c1::Geschenk}} von meiner Schwester.	etwas, das man geschenkt bekommt	Мой велосипед был подарком от моей сестры.	form::satzmuster func::beschreibung topic::gegenstände level::b2_c1 source::goethe::b2::k1
{{c1::Ich würde mich freuen}}, wenn du morgen kommst.	wäre froh	Я был(а) бы рад(а), если бы ты завтра пришёл / пришла.	form::satzmuster func::wünsche_ausdrücken topic::gefühle source::goethe::b2::k1
{{c1::In diesem Text geht es um}} den Einfluss von Erinnerungen auf unser Leben.	das Thema nennen	В этом тексте речь идёт о влиянии воспоминаний на нашу жизнь.	form::satzmuster func::zusammenfassen topic::texte source::goethe::b2::k1

Example output if file-writing tools are available:
WROTE: data/converted/b2/goethe/K1_RM_DE_RU.txt

When I send a raw file path and its TSV rows, convert that file only.
After finishing one file, wait for the next raw file.
```

## Recommended Use

- Process one raw file at a time.
- Paste the exact raw file path before the TSV rows.
- If the model cannot write files, save each ChatGPT result immediately into the mirrored `data/converted/...` path.
- Pay special attention to rows where the original cloze is only `…` or `...`; those rows must be rewritten, not copied.
- After conversion, quickly check that:
  - every row has exactly one cloze
  - field 2 explains that cloze
  - the sentence is concrete enough for production practice
  - the Russian translation matches the final sentence
