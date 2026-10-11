# Validation · 0.1.0

Validated on 2026-10-11 against Hermes source revision
`c0ef5af5205dbdc25e9e44acd66873b4bb3503c9`.

## Hermes plugin validation

```bash
HERMES_HOME=/tmp/hermes-ca-validation-home hermes plugins validate /tmp/hermes-lang-ca
```

Result: **Validation passed**.

- Manifest, version requirement and manifest-only language-pack loading accepted.
- Core: 208 keys; all recognized.
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

No interactive Desktop or TUI rendering was tested. The translation has not received an independent
linguistic review and is not a complete localization.
