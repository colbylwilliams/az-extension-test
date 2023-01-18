# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os

from pathlib import Path
from re import search

EXT_NAME = 'EXTENSION_NAME'

path_root = Path(__file__).resolve().parent.parent
path_src = path_root / EXT_NAME

is_ci = os.environ.get('CI', False)
github_output = os.environ.get('GITHUB_OUTPUT', None)

version = None

with open(path_src / 'setup.py', 'r') as f:
    for line in f:
        if line.startswith('VERSION'):
            txt = str(line).rstrip()
            match = search(r'VERSION = [\'\"](.*)[\'\"]$', txt)
            if match:
                version = match.group(1)

if version:
    if github_output and is_ci:
        with open(github_output, 'a+') as f:
            f.write(f'version={version}\n')
    else:
        print(version)

fallback_counter = 0

changes = []

with open(path_src / 'HISTORY.rst', 'r') as f:
    for line in f:
        if line.startswith(version):
            sep = next(f, '').rstrip()  # skip the '++++++' separator
            change = next(f, '')

            while change and len(change) > 1 and not change.isspace():
                changes.append(change.rstrip())
                change = next(f, '')

                fallback_counter += 1
                if fallback_counter > 30:
                    break
            break

if changes:
    if github_output and is_ci:
        with open(github_output, 'a+') as f:
            f.write(f'changes={",".join(changes)}\n')
    else:
        print('\n'.join(changes))
        print(f'changes={",".join(changes)}\n')
