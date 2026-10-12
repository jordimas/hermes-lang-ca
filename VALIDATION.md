# Validation · 0.2.0

Validated on 2026-10-12 against the installed Hermes source revision
`c0ef5af5205dbdc25e9e44acd66873b4bb3503c9`. The English core catalog and exported key sets also
match the previously downloaded upstream snapshot `74f77ab9b04c502aa7ee0999346f05f027ea9b48`.

## Coverage

| Surface | Supplied text keys | Available text keys | Non-text keys omitted |
| --- | ---: | ---: | ---: |
| Core / CLI / gateway | 3,438 | 3,438 | 0 |
| TUI | 1,301 | 1,301 | 0 |
| Desktop | 5,061 | 5,061 | 4 |
| Total | 9,800 | 9,800 | 4 |

No supported text keys are missing. Accepted input lists, executable snippets, product names and
technical symbols keep their original spelling; having an entry does not mean those tokens change.

The Desktop export also lists these values, which its text-only override adapter cannot preserve:

- `composer.followUpPlaceholders`: array of example prompts.
- `composer.newSessionPlaceholders`: array of example prompts.
- `intro.custom`: function returning an array.
- `sidebar.projects.branchOff`: function returning `{before, after}`.

They deliberately retain their bundled values. A string override would break their callers.

## Catalog validation

```bash
python3 scripts/check.py --hermes-source /path/to/hermes-agent --require-complete
hermes plugins validate /path/to/hermes-lang-ca
```

Both checks pass. All catalogs parse as text-only mappings with recognized keys and matching
placeholder multisets, including format specifiers and repeated arguments. Newline counts match.
The coverage gate rejects missing text entries and rejects overrides of the four non-text keys.
Full English references are included for reproducible translation maintenance.

The newly added translations were generated and proofread with a language model, followed by
manual corrections and representative spot checks. Commands, flags, URLs, code in backticks,
environment variables, shortcut letters and leading/trailing whitespace were checked separately.
Existing translations were retained. This is not an independent human linguistic review.

## Runtime checks

A temporary Hermes profile loads the manifest-only plugin through real plugin discovery. Checks
cover language selection, core translation formatting, all slash-command descriptions, `/help`,
startup tips, approval menus, exit summaries and both frontend catalogs.

The real shared frontend adapter (`unflattenMessages`, `adaptStringOverrides`, `mergeTranslations`) merges
the complete TUI and Desktop catalogs. Supplied static entries retain string values and supplied
function entries remain callable with positional arguments. The four non-text Desktop entries
retain their original types and values.

No interactive Desktop or TUI rendering was tested. Hermes' built-in CLI skin branding can still
override translated welcome/help/goodbye strings; startup banner labels also include hardcoded
English. CLI autocomplete can retain an early English snapshot (upstream issue
[#136743](https://github.com/NousResearch/hermes-agent/issues/136743)). These require changes in
Hermes itself and cannot be fixed by adding catalog entries.

The plugin registers no Python code, runtime dependencies or tools. Security-scan cautions about
`sudo` or command examples concern UI text, not executable plugin code. All translation/export/
proofreading scripts and batch results stayed in `/tmp` and are not published with the pack.
