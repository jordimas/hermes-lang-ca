# Validation · 0.1.2

Validated on 2026-10-11 against Hermes source revision
`74f77ab9b04c502aa7ee0999346f05f027ea9b48` (latest upstream snapshot at validation time).
Also checked against the installed Hermes revision `c0ef5af5205dbdc25e9e44acd66873b4bb3503c9`.

## Hermes plugin validation

```bash
HERMES_HOME=/tmp/hermes-ca-validation-home hermes plugins validate /tmp/hermes-lang-ca
```

Result: **Validation passed**.

- Manifest, version requirement and manifest-only language-pack loading accepted.
- Core: 408 keys; all recognized.
- TUI: 254 keys; all recognized.
- Desktop: 699 keys; all recognized.
- No Python runtime dependencies or registered tools.
- No runtime Python entry point; capability probe skipped as expected.
- Security scan cautions concern the literal word `sudo` in English UI reference strings.
  These are text references to password prompts, not executable commands.

## Catalog checks

```bash
python3 scripts/check.py --hermes-source /path/to/hermes-agent
```

Result: all catalogs contain text values, recognized keys, matching placeholder multisets and
matching newline counts. Coverage is partial; see README.md for the denominators.

## Runtime smoke check

A separate temporary Hermes home, containing a copy of this plugin and a config enabling it, was
loaded through the real `hermes_cli.plugins.PluginManager.discover_and_load()` path, with real
imports and no loader mocks. Verified:

- The manifest-only plugin loads and `ca` becomes selectable as **Català**.
- Loading the plugin alone leaves the display language in English.
- `approval.denied` renders as `      ✗ Denegat`.
- `gateway.model.switched` formats the supplied model name correctly in Catalan.
- An untranslated approval-choice menu falls back to the English catalog unchanged.
- The TUI catalog serves `status.ready: preparat`.
- The Desktop catalog serves `common.save: Desa`.
- Setting `display.language: ca` selects Catalan.
- Unloading the plugin removes the registered language.

For 0.1.1, an isolated temporary profile was used to load the updated pack and call the real
`CLIInfoMixin.show_help()` renderer against both the upstream snapshot and the installed checkout.
Verified all English `slash.*` and `cli.help.*` keys have Catalan translations, every registry
command resolves a translated description, and rendered help includes `Sessió`, `Configuració`,
`Inicia una sessió nova`, translated usage suffixes and hints. Parser-sensitive approval menus
still fall back to English. The built-in skin still overrides the help title with
`Available Commands`; this limitation is documented in README.md.

For 0.1.2, all three catalogs were audited against the latest snapshot using
`scripts/check.py --hermes-source /path/to/hermes-agent --missing-dir /tmp/hermes-ca-missing`.
Missing translations: core 3,030; TUI 1,047; Desktop 4,366 (8,443 total).
All translated keys are recognized. The package is partial, not a complete translation.
The first 48 startup tips and all 11 input examples are now translated, including
`tips.t027` (`/insights`) and `tips.placeholder.p08` (the to-do list example).

No interactive Desktop or TUI rendering was tested. The translation has not received an independent
linguistic review and is not a complete localization.
