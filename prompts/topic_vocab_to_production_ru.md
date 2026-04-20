# Topic Vocabulary To Russian-Led Production Cards

Use this prompt to turn a raw German-only topic vocabulary file into an Anki-ready TSV import for the note type described in [production.md](/mnt/data/german-study/anki/note-types/production.md).

For tagging, follow the repository conventions documented in [tagging.md](/mnt/data/german-study/docs/tagging.md).

Recommended raw source pattern:

- `anki/sources/vocabulary/<topic>/<filename>.txt`

Current example:

- `anki/sources/vocabulary/ice_skating/c1_c2_ice_skating_2026-03-20.txt`

New source files may use `.tsv`; the current `.txt` files remain valid.

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

- raw: `anki/sources/vocabulary/ice_skating/c1_c2_ice_skating_2026-03-20.txt`
- output: `anki/decks/vocabulary/ice_skating/c1_c2_ice_skating_production_DE_RU.tsv`

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
- First apply the common production rules below.
- After that, if a domain add-on is provided after the common rules, apply that add-on too.
- If a domain add-on conflicts with the common rules, follow the domain add-on only for topic-specific meaning choice, terminology, and preferred domain tagging. Keep the output format unchanged.

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
  - `domain::taktik`
  - `domain::mannschaft`
  - `domain::regelwerk`
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
- Prefer topic-relevant domain tags:
  - for figure skating style topics, `domain::technik`, `domain::wettkampf`, `domain::eissport`
  - for team sport topics such as ice hockey, `domain::taktik`, `domain::mannschaft`, `domain::regelwerk`, `domain::wettkampf`
  - for technical topics, prefer a small stable set of domain tags from the provided domain add-on instead of inventing new ones line by line

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
anki/sources/vocabulary/ice_skating/c1_c2_ice_skating_2026-03-20.txt

Example input lines:
die Kufe
die Landung stabil ausfahren
Die Kür war technisch stark und künstlerisch klar.

Example output if file-writing tools are not available:
OUTPUT: anki/decks/vocabulary/ice_skating/c1_c2_ice_skating_production_DE_RU.tsv
лезвие конька	die Kufe	Metallteil am Schuh	form::vokabel func::produktion level::c1_c2 topic::ice_skating source::raw::vocabulary::ice_skating card::wort domain::eissport
уверенно выйти из приземления	die Landung stabil ausfahren	nach dem Sprung sicher weitergleiten	form::vokabel func::produktion level::c1_c2 topic::ice_skating source::raw::vocabulary::ice_skating card::chunk domain::technik
Программа была технически сильной и художественно ясной.	Die Kür war technisch stark und künstlerisch klar.	Programm wirkt sportlich und gestalterisch überzeugend	form::vokabel func::produktion level::c1_c2 topic::ice_skating source::raw::vocabulary::ice_skating card::satz domain::wettkampf

When I send a raw file path and its raw lines, convert that file only.
After finishing one file, wait for the next raw file.
```

## Combined Prompt Use

This file is intended to serve as the common core of a combined prompt.

Recommended structure when using it with topic files:

1. paste the common prompt template from this file
2. append one domain add-on section if the topic needs domain-specific disambiguation
3. then provide the raw file path and raw lines

Use the domain add-on only to refine:

- meaning choice for ambiguous technical terms
- preferred Russian phrasing where precision matters
- preferred `domain::...` tags
- topic-specific distinctions that affect hints

Do not use a domain add-on to change:

- the TSV column order
- the one-line-per-input-line rule
- the note type
- the general tagging backbone
- the requirement to preserve `AnswerDE` exactly

## Domain Add-On Template

Append a short block like this after the common prompt when needed:

```text
Domain add-on for: <topic>

Meaning and prompt guidance:
- ...

Hint guidance:
- ...

Preferred domain tags:
- ...

Ambiguity notes:
- ...
```

## Domain Add-On: General CS / IT

Use this add-on for files such as:

- `anki/sources/vocabulary/general_cs_it/...`

```text
Domain add-on for: general_cs_it

Meaning and prompt guidance:
- Prefer mainstream software, systems, networking, database, and infrastructure meanings.
- For technical nouns, prefer precise Russian prompts over broad dictionary glosses.
- If a term has both everyday and technical meanings, choose the technical one unless the raw line clearly points elsewhere.
- For chunks, write prompts that sound like real engineering actions or system operations.
- For sentences, preserve the practical engineering context rather than making them abstract.

Hint guidance:
- Keep hints functional and plain, as if explaining the term to a teammate.
- Prefer usage cues such as architecture role, system behavior, or operational context.
- Avoid overly academic paraphrases if a simple practical cue is enough.

Preferred domain tags:
- `domain::technik`
- `domain::software`
- `domain::netzwerk`
- `domain::daten`
- `domain::infrastruktur`

Ambiguity notes:
- `die Anwendung` usually means software application, not abstract use.
- `das Deployment` / `die Bereitstellung` should be treated as release or rollout in a software context.
- `die Migration` should usually be read as system, database, or platform migration.
- `die Architektur` should usually mean software or system architecture.
- `die Schnittstelle` should usually mean API, interface, or system boundary.
- `der Cache` and `die Warteschlange` should be handled as technical runtime components.
- `die Sicherheit` in these files often means operational or system security, but use `domain::sicherheit` only if the item is clearly security-focused rather than general CS/IT.
```

## Domain Add-On: AI / ML

Use this add-on for files such as:

- `anki/sources/vocabulary/ai_ml/...`

```text
Domain add-on for: ai_ml

Meaning and prompt guidance:
- Prefer AI, machine learning, model evaluation, prompting, and deployment meanings.
- For Russian prompts, preserve distinctions between training, inference, evaluation, prompting, and safety.
- For model-related vocabulary, make the prompt specific enough that the learner can recover the exact technical term.
- For chunks, cue concrete model-development or model-usage situations.
- For sentences, keep the ML or LLM context explicit where needed.

Hint guidance:
- Prefer short conceptual paraphrases about model behavior, training dynamics, evaluation, or safe usage.
- Keep hints concrete and technical rather than philosophical.
- If the target is a known failure mode, the hint should point to the behavior, not restate the label.

Preferred domain tags:
- `domain::ki`
- `domain::ml`
- `domain::daten`
- `domain::modellierung`
- `domain::sicherheit`

Ambiguity notes:
- `das Modell` should usually mean an ML or AI model, not a generic model or example.
- `das Training` should usually mean model training, not general practice.
- `die Inferenz` should be treated as model inference at runtime.
- `die Einbettung` should be treated as embedding in the ML sense.
- `der Kontext` and `das Kontextfenster` should be handled in LLM or sequence-processing terms when relevant.
- `die Halluzination` should be treated as fabricated model output, not human imagination.
- `die Ausrichtung` should be treated as AI alignment when the surrounding vocabulary supports that reading.
- `die Sicherheit` may refer either to model safety or information security; prefer the AI-safety reading in AI/ML files unless the line clearly belongs to cybersecurity.
```

## Domain Add-On: Tennis

Use this add-on for files such as:

- `anki/sources/vocabulary/tennis/...`

```text
Domain add-on for: tennis

Meaning and prompt guidance:
- Prefer sport-specific tennis meanings over everyday meanings.
- For Russian prompts, sound like real match, coaching, or commentary language rather than dictionary glosses.
- Preserve distinctions between stroke names, tactical patterns, scoring terms, and tournament terms.
- For chunks, write prompts as natural tennis actions or match instructions.
- For sentences, keep the on-court or competition context explicit when needed.

Hint guidance:
- Prefer short cues about match situation, stroke function, tactical purpose, or competition context.
- Keep hints concrete and sport-specific.
- Avoid generic hints that could fit many sports if a tennis-specific cue is possible.

Preferred domain tags:
- `domain::sport`
- `domain::tennis`
- `domain::training`
- `domain::wettkampf`
- `domain::taktik`
- `domain::technik`

Ambiguity notes:
- `der Aufschlag` should usually mean tennis serve, not a generic beginning of play.
- `der Return` should be treated as the return of serve, not a general return or comeback.
- `der Slice` should be treated as the tennis stroke or spin type.
- `der Volley` and `der Halbvolley` should keep the tennis shot meaning.
- `das Break` should mean winning the opponent's service game.
- `der Vorteil` should be treated in the tennis scoring sense when the file context supports it.
- `die Challenge` should usually mean an electronic line-call challenge.
- `die Linie`, `cross`, and `longline` should be interpreted in tennis shot-placement terms.
```

## Domain Add-On: Medical

Use this add-on for files such as:

- `anki/sources/vocabulary/medical/...`

```text
Domain add-on for: medical

Meaning and prompt guidance:
- Prefer patient-facing medical and dental meanings over abstract or institutional meanings.
- For Russian prompts, use natural language a patient or doctor would realistically use in appointments, treatment discussions, and follow-up care.
- Preserve distinctions between symptoms, diagnoses, tests, treatment steps, medications, and insurance or paperwork terms.
- For dental lines, keep the dental context explicit when needed instead of collapsing everything into general medicine.
- For chunks, write prompts as realistic clinic, pharmacy, or dentist-office actions.
- For sentences, preserve the practical consultation context and symptom logic.

Hint guidance:
- Prefer short cues about symptom type, examination purpose, treatment function, recovery context, or dental procedure role.
- Keep hints concrete and practical rather than textbook-like.
- Avoid overly broad hints if a more specific medical or dental cue is possible.

Preferred domain tags:
- `domain::medizin`
- `domain::symptom`
- `domain::diagnostik`
- `domain::behandlung`
- `domain::zahnarzt`

Ambiguity notes:
- `die Praxis` should usually mean a medical or dental practice, not abstract practical experience.
- `die Beschwerden` should usually mean symptoms or patient complaints, not general dissatisfaction.
- `der Befund` should be treated as a medical finding or test result.
- `das Rezept` should usually mean a medical prescription, not a cooking recipe.
- `die Krone` in these files may be a dental crown rather than a generic crown.
- `die Brücke` in these files may be a dental bridge rather than a physical bridge.
- `die Schiene` may refer to a dental splint, bite guard, or support device depending on context.
- `die Reinigung` in dental context should often be read as professional tooth cleaning rather than general cleaning.
```

### Additional Example For Ice Hockey

Example input path:
anki/sources/vocabulary/ice_hockey/c1_c2_ice_hockey_2026-03-20.txt

Example input lines:
das Powerplay
die Passwege konsequent zustellen
Der Torwart hält den Winkel konsequent klein.

Example output if file-writing tools are not available:
OUTPUT: anki/decks/vocabulary/ice_hockey/c1_c2_ice_hockey_production_DE_RU.tsv
игра в большинстве	das Powerplay	Angriff mit einem Spieler mehr	form::vokabel func::produktion level::c1_c2 topic::ice_hockey source::raw::vocabulary::ice_hockey card::wort domain::taktik
последовательно перекрывать линии передач	die Passwege konsequent zustellen	Zuspielmöglichkeiten systematisch schließen	form::vokabel func::produktion level::c1_c2 topic::ice_hockey source::raw::vocabulary::ice_hockey card::chunk domain::taktik
Вратарь последовательно сокращает угол обстрела.	Der Torwart hält den Winkel konsequent klein.	nimmt dem Gegner gezielt freien Raum	form::vokabel func::produktion level::c1_c2 topic::ice_hockey source::raw::vocabulary::ice_hockey card::satz domain::technik

## Recommended Use

- Start with a small sample and check whether the Russian prompts are precise enough.
- Spot-check hints to ensure they do not reuse the target wording.
- For mixed files like topic vocabulary lists, keep the same tag backbone for all rows and vary only `card::...` and the most useful `domain::...` tag.
- If a raw item is too broad for a precise Russian prompt, rewrite the prompt as a short situational cue rather than a one-word gloss.
- For team-sport files, prefer tags that distinguish technique, tactics, team structure, and rules instead of using only generic sport tags.
