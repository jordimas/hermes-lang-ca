# Hermes Catalan language pack · Català

Catalan (`ca`) UI translations for [Hermes Agent](https://github.com/NousResearch/hermes-agent):
CLI, gateway, TUI and Desktop.

## Install

Requires Hermes Agent **0.21.6 or later** with language-pack support.

```bash
hermes plugins install https://github.com/jordimas/hermes-lang-ca
hermes config set display.language ca
```

Restart Hermes to load the pack. If needed, check whether `HERMES_LANGUAGE` overrides the setting.
To switch back: `hermes config set display.language en`.

The pack translates UI text. To get replies in Catalan, ask the agent in your instructions.
Some built-in branding and non-text Desktop entries remain in English.

## Contributing

Edit values in `locales/`, preserving keys, placeholders, line breaks and command syntax.
Validate before submitting:

```bash
hermes plugins validate /path/to/hermes-lang-ca
```

## License

MIT. Derived from Hermes Agent's English UI catalogs. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
