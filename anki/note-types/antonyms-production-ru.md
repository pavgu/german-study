# Anki Note Type For Russian-Led Antonyms Production

Recommended note type name:

- `German Antonyms Production RU`

Recommended fields:

- `Antonym1DE`
- `Antonym2DE`
- `DefinitionAntonym1DE`
- `DefinitionAntonym2DE`
- `PromptAntonym1RU`
- `PromptAntonym2RU`
- `AnswerAntonym1DE`
- `AnswerAntonym2DE`
- `Tags`

## Why This Layout

This layout combines two useful study modes in one note:

- abstract antonym recall: `Antonym1DE` <-> `Antonym2DE`
- compact German-definition recall for each side
- active production: short Russian prompts that force a full German sentence with the right word

Using `Antonym1` and `Antonym2` keeps both sides of the pair equal. That works better than `Target` and `Antonym` because either word can be tested first.

## Suggested Import Mapping

Recommended TSV column order:

1. `Antonym1DE`
2. `Antonym2DE`
3. `DefinitionAntonym1DE`
4. `DefinitionAntonym2DE`
5. `PromptAntonym1RU`
6. `PromptAntonym2RU`
7. `AnswerAntonym1DE`
8. `AnswerAntonym2DE`
9. Anki tags

## Recommended Card Types

1. `Antonym1 -> Antonym2`
2. `Antonym2 -> Antonym1`
3. `DE Definition -> Antonym1`
4. `DE Definition -> Antonym2`
5. `RU Prompt -> Antonym1 Sentence`
6. `RU Prompt -> Antonym2 Sentence`

## Card Type 1: Antonym1 -> Antonym2

### Front Template

```html
<div class="label">Antonym 1</div>
<div class="sentence">{{Antonym1DE}}</div>
```

### Back Template

```html
<div class="label">Antonym 1</div>
<div class="help">{{Antonym1DE}}</div>

<hr>
<div class="label">Antonym 2</div>
<div class="sentence">{{Antonym2DE}}</div>
```

## Card Type 2: Antonym2 -> Antonym1

### Front Template

```html
<div class="label">Antonym 2</div>
<div class="sentence">{{Antonym2DE}}</div>
```

### Back Template

```html
<div class="label">Antonym 2</div>
<div class="help">{{Antonym2DE}}</div>

<hr>
<div class="label">Antonym 1</div>
<div class="sentence">{{Antonym1DE}}</div>
```

## Card Type 3: DE Definition -> Antonym1

### Front Template

```html
<div class="label">German Definition</div>
<div class="sentence">{{DefinitionAntonym1DE}}</div>
```

### Back Template

```html
<div class="label">German Definition</div>
<div class="help">{{DefinitionAntonym1DE}}</div>

<hr>
<div class="label">Target Word</div>
<div class="sentence">{{Antonym1DE}}</div>

<hr>
<div class="label">Pair</div>
<div class="value">{{Antonym1DE}} <span class="sep">↔</span> {{Antonym2DE}}</div>
```

## Card Type 4: DE Definition -> Antonym2

### Front Template

```html
<div class="label">German Definition</div>
<div class="sentence">{{DefinitionAntonym2DE}}</div>
```

### Back Template

```html
<div class="label">German Definition</div>
<div class="help">{{DefinitionAntonym2DE}}</div>

<hr>
<div class="label">Target Word</div>
<div class="sentence">{{Antonym2DE}}</div>

<hr>
<div class="label">Pair</div>
<div class="value">{{Antonym1DE}} <span class="sep">↔</span> {{Antonym2DE}}</div>
```

## Card Type 5: RU Prompt -> Antonym1 Sentence

### Front Template

```html
<div class="label">Russian Prompt</div>
<div class="sentence">{{PromptAntonym1RU}}</div>
```

### Back Template

```html
<div class="label">Russian Prompt</div>
<div class="help">{{PromptAntonym1RU}}</div>

<hr>
<div class="label">German Answer</div>
<div class="sentence">{{AnswerAntonym1DE}}</div>

<hr>
<div class="label">Pair</div>
<div class="value">{{Antonym1DE}} <span class="sep">↔</span> {{Antonym2DE}}</div>
```

## Card Type 6: RU Prompt -> Antonym2 Sentence

### Front Template

```html
<div class="label">Russian Prompt</div>
<div class="sentence">{{PromptAntonym2RU}}</div>
```

### Back Template

```html
<div class="label">Russian Prompt</div>
<div class="help">{{PromptAntonym2RU}}</div>

<hr>
<div class="label">German Answer</div>
<div class="sentence">{{AnswerAntonym2DE}}</div>

<hr>
<div class="label">Pair</div>
<div class="value">{{Antonym1DE}} <span class="sep">↔</span> {{Antonym2DE}}</div>
```

## Styling

```css
.card {
  font-family: "Noto Sans", "Segoe UI", sans-serif;
  font-size: 22px;
  line-height: 1.5;
  text-align: left;
  color: #1f2933;
  background: #fffdf8;
  max-width: 42rem;
  margin: 0 auto;
}

.sentence {
  font-size: 1.28em;
  margin-bottom: 0.8em;
}

.label {
  font-size: 0.72em;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #7a6f5a;
  margin-bottom: 0.35em;
}

.help {
  color: #8b5e34;
}

.value {
  color: #243b53;
}

.sep {
  color: #b45309;
  font-weight: 700;
  padding: 0 0.25em;
}

hr {
  border: 0;
  border-top: 1px solid #eadfce;
  margin: 0.9em 0;
}
```

## Notes

- The German-definition cards help test each word individually instead of only the pair contrast.
- The definition should describe meaning, not just negate the opposite word.
- Keep Russian prompts short but specific enough that only one of the pair fits naturally.
- The answer fields should contain full German sentences, not isolated words.
- The pair section on the production card backs helps reinforce the contrast after recall.
- `Tags` can be mapped on import even though it is not shown on the card.
- This layout works best for finished antonym decks under `anki/decks/antonyms/`, not for intermediate conversion output.
