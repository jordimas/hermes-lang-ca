#!/usr/bin/env python3
"""Check catalogs against a Hermes checkout and the English reference snapshots.

Run in a Python environment with Hermes' dependencies available.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


# The Desktop key export includes arrays and object-returning functions. The
# text-only pack adapter would replace their shapes with strings and break UI.
NON_TEXT_KEYS = {
    'desktop': {
        'composer.followUpPlaceholders',
        'composer.newSessionPlaceholders',
        'intro.custom',
        'sidebar.projects.branchOff',
    },
}
PLACEHOLDERS = re.compile(
    r'\{(?:[A-Za-z_][A-Za-z_0-9]*|[0-9]+)(?:![ars])?(?::[^{}]*)?\}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hermes-source', type=Path, required=True)
    parser.add_argument('--missing-dir', type=Path,
                        help='Write complete missing-key lists for all three surfaces to this directory')
    parser.add_argument('--require-complete', action='store_true',
                        help='Fail if any text-overridable key lacks a translation')
    args = parser.parse_args()
    source = args.hermes_source.resolve()
    sys.path.insert(0, str(source))
    import hermes_yaml as yaml
    from agent.i18n_layers import flatten, non_text_leaves

    root = Path(__file__).resolve().parents[1]
    failures = []
    for surface in ('core', 'tui', 'desktop'):
        suffix = '' if surface == 'core' else '.' + surface
        file = root / f'locales/ca{suffix}.yaml'
        document = yaml.safe_load(file.read_text(encoding='utf-8'))
        if not isinstance(document, dict) or non_text_leaves(document):
            failures.append(f'{file.name}: expected a text-only mapping')
            continue
        catalog = flatten(document)
        if surface == 'core':
            english = flatten(yaml.safe_load((source / 'locales/en.yaml').read_text(encoding='utf-8')))
            known = set(english)
        else:
            english = json.loads((root / f'reference/en.{surface}.json').read_text(encoding='utf-8'))
            exported = json.loads((source / f'locales/_keys.{surface}.json').read_text(encoding='utf-8'))
            known = set(exported['keys'] if isinstance(exported, dict) else exported)
        for key, text in catalog.items():
            if key not in known:
                failures.append(f'{file.name}: unknown key {key}')
            if key not in english:
                failures.append(f'{file.name}: missing English reference for {key}')
                continue
            # A multiset also detects accidental duplicated or dropped arguments.
            placeholders = lambda s: Counter(PLACEHOLDERS.findall(s))
            if placeholders(text) != placeholders(english[key]):
                failures.append(f'{file.name}: placeholder mismatch at {key}')
            if text.count('\n') != english[key].count('\n'):
                failures.append(f'{file.name}: newline mismatch at {key}')
            if key in NON_TEXT_KEYS.get(surface, set()):
                failures.append(f'{file.name}: {key} cannot safely be overridden with text')
        missing = sorted(known - set(catalog))
        unsupported = set(missing) & NON_TEXT_KEYS.get(surface, set())
        untranslated = set(missing) - unsupported
        print(f'{surface}: {len(set(catalog) & known)} / {len(known)} keys; '
              f'{len(untranslated)} untranslated; {len(unsupported)} non-text keys')
        if args.require_complete and untranslated:
            failures.append(f'{file.name}: {len(untranslated)} text keys have no translation')
        if args.missing_dir:
            args.missing_dir.mkdir(parents=True, exist_ok=True)
            (args.missing_dir / f'missing.{surface}.json').write_text(
                json.dumps(missing, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        return 1
    print('Catalog keys, text values, placeholders and newlines: OK')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
