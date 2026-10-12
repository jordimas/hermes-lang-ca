# Hermes Catalan language pack · Català

Catalan (`ca`) UI translations for [Hermes Agent](https://github.com/NousResearch/hermes-agent).
This is an **initial, partial translation**, covering core/CLI and gateway messages, the terminal UI
(TUI), and the Desktop app. Untranslated strings fall back to English.

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

## Coverage · version 0.1.4

| Surface | Translated keys | English reference keys | Coverage |
| --- | ---: | ---: | ---: |
| Core / CLI / gateway | 415 | 3,438 | 12.1% |
| TUI | 254 | 1,301 | 19.5% |
| Desktop | 699 | 5,065 | 13.8% |
| **Total** | **1,368** | **9,804** | **14.0%** |

Counts refer to Hermes revision `74f77ab9b04c502aa7ee0999346f05f027ea9b48`.
Version 0.1.1 adds all current slash-command descriptions, `/help` text and section headings,
and welcome/shutdown messages. Version 0.1.2 adds the first 48 startup tips and all 11 empty-input
example prompts; the remaining startup tips still fall back to English. Version 0.1.3 translates
the exit summary and session-resume hint. User-supplied session titles keep their original text.
Version 0.1.4 adds the `agent.max_turns` startup tip and translates the CLI's `Tip:` prefix.
The pack also covers approvals, common actions, session navigation,
status messages, voice controls and tool activity. A matching key means the translation is recognized; these counts
do not imply that a whole screen or workflow has been translated.

Hermes' built-in CLI skins currently override the translated `/help` title and welcome/goodbye
text with English branding. The startup banner also contains hardcoded English labels. A language
pack cannot override those; `/help` section headings and command descriptions use the translations.

## Layout

```text
plugin.yaml                Language declaration: ca / Català / left-to-right
locales/ca.yaml             Core, CLI and gateway
locales/ca.tui.yaml         Terminal UI
locales/ca.desktop.yaml     Desktop
reference/en.tui.json       English references for the translated TUI keys
reference/en.desktop.json   English references for the translated Desktop keys
scripts/check.py           Contributor validation utility
```

Hermes loads only the manifest and locale catalogs. There is no `__init__.py`, runtime Python plugin,
network access, model call, extra runtime dependency or automatic change to `display.language`.
The Python check script and English reference snapshots are contributor resources, not plugin code.

## Contributing

Translate values, keeping keys unchanged. Partial additions are welcome.

- Preserve Python placeholders such as `{count}` and positional TUI/Desktop placeholders such as
  `{0}` and `{1}`, including repeated occurrences.
- Preserve command names, flags, URLs, configuration keys and parser-sensitive tokens. Approval
  choice menus and accepted input lists currently use the English fallback deliberately.
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
  --hermes-source /path/to/hermes-agent
```

See [VALIDATION.md](VALIDATION.md) for release checks and the
[upstream language-pack guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/language-packs.md)
for the plugin format.

To audit every available key and export complete lists of missing translations, add
`--missing-dir /tmp/hermes-ca-missing` to the check command above. Validation checks translation
correctness; it does not require full coverage.

## Instal·lació en català

Aquest paquet afegeix **Català** a les llengües de la interfície de Hermes.
La versió inicial és parcial: les cadenes que encara no s’han traduït es mostren en anglès.

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
