# Anki Note Type For Production Cards

Recommended note type name:

- `German Production Prompt`

Recommended fields:

- `Prompt`
- `Answer`
- `Hint`

Import mapping for a 4-column production TSV such as `anki/decks/grammar/hin-und-her_production_DE_RU.txt`:

- column 1 -> `Prompt`
- column 2 -> `Answer`
- column 3 -> `Hint`
- column 4 -> Anki tags

## Front Template

```html
<div class="label">Prompt</div>
<div class="sentence">{{Prompt}}</div>

{{#Hint}}
<hr>
<div class="label">Hint</div>
<div class="help">{{hint:Hint}}</div>
{{/Hint}}
```

## Back Template

```html
<div class="label">Prompt</div>
<div class="help">{{Prompt}}</div>

<hr>
<div class="label">Answer</div>
<div class="sentence">{{Answer}}</div>

{{#Hint}}
<hr>
<div class="label">Hint</div>
<div class="value">{{Hint}}</div>
{{/Hint}}
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
  font-size: 1.3em;
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

## Notes

- This note type is meant for full-sentence production, not cloze recognition.
- If the `Hint` field feels too helpful, leave it unmapped during import or hide it on the front.
- This layout is used by several finished deck families under `anki/decks/`, especially grammar and topic vocabulary production decks.
