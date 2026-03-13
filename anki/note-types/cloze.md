# Anki Note Type

Recommended note type name:

- `German Production Cloze`

Recommended fields:

- `Text`
- `Cue`
- `Translation`

Import mapping for the merged TSV:

- column 1 -> `Text`
- column 2 -> `Cue`
- column 3 -> `Translation`
- column 4 -> Anki tags

## Front Template

```html
<div class="sentence">{{cloze:Text}}</div>

{{#Cue}}
<hr>
<div class="label">Cue</div>
<div class="help">{{hint:Cue}}</div>
{{/Cue}}

{{#Translation}}
<hr>
<div class="label">Translation</div>
<div class="help">{{hint:Translation}}</div>
{{/Translation}}
```

## Back Template

```html
<div class="sentence">{{cloze:Text}}</div>

{{#Cue}}
<hr>
<div class="label">Cue</div>
<div class="value">{{Cue}}</div>
{{/Cue}}

{{#Translation}}
<hr>
<div class="label">Translation</div>
<div class="value">{{Translation}}</div>
{{/Translation}}
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
  font-size: 1.35em;
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
  font-style: italic;
}

.value {
  color: #243b53;
}

.cloze {
  font-weight: 700;
  color: #b45309;
}

hr {
  border: 0;
  border-top: 1px solid #eadfce;
  margin: 0.9em 0;
}
```

## Notes

- `Cue` and `Translation` use Anki conditional blocks, so they only show when the field is not empty.
- `Translation` is shown on both the front and the back by design.
- This note type is intended for merged imports such as `anki/imports/converted/b2/goethe/K1-K12_RM_DE_RU.txt`.
