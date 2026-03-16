# Anki Note Type For Russian-Led Confusables Production

Recommended note type name:

- `German Confusables Production RU`

Recommended fields:

- `PromptRU`
- `AnswerDE`
- `HintDE`

Import mapping for generated TSV:

- column 1 -> `PromptRU`
- column 2 -> `AnswerDE`
- column 3 -> `HintDE`
- column 4 -> Anki tags

## Why This Layout

This layout is optimized for active production:

- the front is in Russian, so you must retrieve the German item
- the front also shows a short hint, so you practice distinguishing confusables during recall
- the back gives the full German answer, not just the isolated word
- `HintDE` makes the contrast explicit without needing a second Russian field

This is better for confusables than a plain translation card because it forces you to choose between near-neighbors such as:

- `ermitteln` vs `vermitteln`
- `meiden` vs `vermeiden`
- `kennen` vs `wissen`

## Front Template

```html
<div class="label">Russian Prompt</div>
<div class="sentence">{{PromptRU}}</div>

{{#HintDE}}
<hr>
<div class="label">Hint</div>
<div class="help">{{hint:HintDE}}</div>
{{/HintDE}}
```

## Back Template

```html
<div class="label">Russian Prompt</div>
<div class="help">{{PromptRU}}</div>

{{#HintDE}}
<hr>
<div class="label">Hint</div>
<div class="value">{{HintDE}}</div>
{{/HintDE}}

<hr>
<div class="label">German Answer</div>
<div class="sentence">{{AnswerDE}}</div>
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

hr {
  border: 0;
  border-top: 1px solid #eadfce;
  margin: 0.9em 0;
}
```

## Field Guidance

- `PromptRU`: one natural Russian sentence that points clearly to the target item
- `AnswerDE`: one natural German sentence with the target item in full, not a cloze
- `HintDE`: a short German contrast hint shown on the front and back, for example `Polizei -> ermitteln; Nachricht -> vermitteln`

## Notes

- Keep `PromptRU` precise enough that only one of the pair should fit naturally.
- Avoid vague one-word Russian prompts whenever a short sentence gives cleaner disambiguation.
- Keep `HintDE` short enough to guide recall without simply naming the answer.
