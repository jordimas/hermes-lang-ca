# Hermes Catalan language pack · Català

Catalan (`ca`) UI translations for [Hermes Agent](https://github.com/NousResearch/hermes-agent),
covering the CLI, gateway, terminal UI and Desktop app.

## Install

Requires Hermes Agent **0.21.6 or later** with language-pack support.

```bash
hermes plugins install https://github.com/jordimas/hermes-lang-ca
hermes config set display.language ca
```

Restart any running Hermes interface to load the pack. The language selector displays **Català**.
If the language does not change, check whether `HERMES_LANGUAGE` overrides the configuration.
To switch back, run `hermes config set display.language en`.

El paquet tradueix la interfície. Perquè l’agent també respongui en català, indica-ho a les seves
instruccions. Reinicia les interfícies obertes després d’instal·lar-lo.

## Coverage

Version **0.2.0** supplies all **9,800 supported text keys** in the validated catalogs.
Four Desktop entries containing lists or objects retain their bundled values. Some built-in
CLI branding and autocomplete descriptions can still appear in English. Tool output, logs,
slash-command names and user content keep their original text.

See [VALIDATION.md](VALIDATION.md) for coverage counts, the validated Hermes revision and runtime
limitations.

## Contributing

Translations live in `locales/ca.yaml`, `locales/ca.tui.yaml` and `locales/ca.desktop.yaml`;
English reference snapshots are in `reference/`.

Keep keys unchanged and values as strings. Preserve placeholders (including repeated occurrences),
line breaks, commands, flags, URLs, configuration keys and accepted input tokens.
When adding TUI/Desktop keys, update the corresponding English reference snapshot.

```bash
hermes plugins validate /path/to/hermes-lang-ca
/path/to/hermes-agent/scripts/run-in-hermes-env python3 \
  /path/to/hermes-lang-ca/scripts/check.py \
  --hermes-source /path/to/hermes-agent --require-complete
```

Add `--missing-dir /tmp/hermes-ca-missing` to export missing-key lists.
See the [upstream language-pack guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/language-packs.md)
for the plugin format.

## License

MIT. Derived from Hermes Agent's English UI catalogs. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
