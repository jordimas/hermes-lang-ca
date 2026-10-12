# Hermes Catalan language pack · Català

Catalan (`ca`) UI translations for [Hermes Agent](https://github.com/NousResearch/hermes-agent).
The pack covers every text-overridable key in the validated core/CLI and gateway catalogs,
the terminal UI (TUI), and the Desktop app. See the coverage and runtime limitations below.

## Install

Requires Hermes Agent **0.21.6 or later** with language-pack support.

```bash
hermes plugins install https://github.com/jordimas/hermes-lang-ca
hermes config set display.language ca
```

Restart any running Hermes CLI, TUI, Desktop or gateway process to load the pack.
The language selector displays **Català**. If the configured language does not take effect, check
whether an existing `HERMES_LANGUAGE` setting overrides `display.language`.

To switch back:

```bash
hermes config set display.language en
```

This pack translates static UI text. To have the agent answer in Catalan, also ask it to do so in
your instructions. Tool output, logs and slash-command names are not translated by language packs.

## Coverage · version 0.2.0

| Surface | Translated keys | English reference keys | Coverage |
| --- | ---: | ---: | ---: |
| Core / CLI / gateway | 3,438 | 3,438 | 100% |
| TUI | 1,301 | 1,301 | 100% |
| Desktop | 5,061 | 5,065 | 99.92% |
| **Total** | **9,800** | **9,804** | **99.96%** |

Counts refer to the installed Hermes revision `c0ef5af5205dbdc25e9e44acd66873b4bb3503c9`.
Version 0.2.0 adds 8,432 catalog entries. All 9,800 text-overridable keys are supplied, including
all startup tips, approval labels, configuration labels, billing screens and exit summaries.
Command syntax, accepted input keywords, product names and technical symbols retain their original
spelling. User-supplied session titles and other dynamic content keep their original text.

Four Desktop keys cannot be represented by a text-only pack: `composer.followUpPlaceholders` and
`composer.newSessionPlaceholders` are lists, `intro.custom` returns a list, and
`sidebar.projects.branchOff` returns an object. They deliberately retain their bundled values;
overriding them with strings would change their types and break the interface. The full key export
currently counts these alongside text keys.

Hermes' built-in CLI skins currently override the translated `/help` title and welcome/goodbye
text with English branding. The startup banner also contains hardcoded English labels. A language
pack cannot override those; `/help` section headings and command descriptions use the translations.
CLI autocomplete can also retain descriptions rendered before the pack loads; see
[Hermes issue #136743](https://github.com/NousResearch/hermes-agent/issues/136743).

## Layout

```text
plugin.yaml                Language declaration: ca / Català / left-to-right
locales/ca.yaml             Core, CLI and gateway
locales/ca.tui.yaml         Terminal UI
locales/ca.desktop.yaml     Desktop
reference/en.core.json      English core reference snapshot
reference/en.tui.json       English TUI reference snapshot
reference/en.desktop.json   English Desktop text reference snapshot
scripts/check.py           Contributor validation utility
```

Hermes loads only the manifest and locale catalogs. There is no `__init__.py`, runtime Python plugin,
network access, model call, extra runtime dependency or automatic change to `display.language`.
The Python check script and English reference snapshots are contributor resources, not plugin code.

## Contributing

Translate values, keeping keys unchanged. New upstream keys and translation corrections are welcome.

- Preserve Python placeholders such as `{count}` and positional TUI/Desktop placeholders such as
  `{0}` and `{1}`, including repeated occurrences.
- Preserve command names, flags, URLs, configuration keys and parser-sensitive tokens. Approval
  menus translate their descriptions while retaining the accepted shortcut letters. Accepted input
  lists retain the English tokens that Hermes parses.
- Keep all YAML leaves as strings. Quote YAML reserved words and numeric-looking values.
- Keep line breaks used by the original message.
- When adding TUI/Desktop keys, update the corresponding English reference snapshot from the
  English source catalog. Function-valued strings use positional placeholders in parameter order;
  the snapshot represents their rendered string, using the plural form where needed.
- Validate against a current Hermes checkout before submitting changes.

```bash
hermes plugins validate /path/to/hermes-lang-ca
```

The additional check verifies known keys, text values, placeholder multiplicity and line breaks:

```bash
/path/to/hermes-agent/scripts/run-in-hermes-env python3 \
  /path/to/hermes-lang-ca/scripts/check.py \
  --hermes-source /path/to/hermes-agent --require-complete
```

See [VALIDATION.md](VALIDATION.md) for release checks and the
[upstream language-pack guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/language-packs.md)
for the plugin format.

To audit every available key and export complete lists of missing translations, add
`--missing-dir /tmp/hermes-ca-missing` to the check command above. `--require-complete` fails when
any supported text key is missing; the four non-text Desktop keys are reported separately.

## Instal·lació en català

Aquest paquet afegeix **Català** a les llengües de la interfície de Hermes.
La versió 0.2.0 cobreix totes les claus de text dels catàlegs validats. Quatre claus de Desktop
que contenen llistes o objectes es conserven sense substituir-les per text. Alguns textos imposats
pels temes de Hermes encara poden aparèixer en anglès; vegeu les limitacions descrites més amunt.

```bash
hermes plugins install https://github.com/jordimas/hermes-lang-ca
hermes config set display.language ca
```

Reinicia les interfícies de Hermes que tinguis obertes perquè carreguin el paquet.
Perquè l’agent també respongui en català, indica-ho a les seves instruccions.

Les aportacions són benvingudes. Conserva les claus, les ordres i els marcadors de substitució
quan tradueixis els textos.

## License

MIT. Derived from Hermes Agent's English UI catalogs. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
