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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hermes-source', type=Path, required=True)
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
            placeholders = lambda s: Counter(re.findall(r'\{[A-Za-z_][A-Za-z_0-9]*\}|\{[0-9]+\}', s))
            if placeholders(text) != placeholders(english[key]):
                failures.append(f'{file.name}: placeholder mismatch at {key}')
            if '\n' in english[key] and text.count('\n') != english[key].count('\n'):
                failures.append(f'{file.name}: newline mismatch at {key}')
        print(f'{surface}: {len(catalog)} / {len(known)} keys')
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        return 1
    print('Catalog keys, text values, placeholders and newlines: OK')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
