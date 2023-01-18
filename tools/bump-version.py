# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import argparse

from pathlib import Path
from re import search

from packaging.version import parse as parse_version  # pylint: disable=unresolved-import

EXT_NAME = 'EXTENSION_NAME'

parser = argparse.ArgumentParser()
parser.add_argument('--major', action='store_true', help='bump major version')
parser.add_argument('--minor', action='store_true', help='bump minor version')
parser.add_argument('--notes', nargs='*', default=['Bug fixes and minor improvements'], help='space seperated strings with release notes')

args = parser.parse_args()

major = args.major
minor = args.minor
notes = '* {}'.format('\n* '.join(args.notes))

if major and minor:
    raise ValueError('usage error: --major | --minor')

patch = not minor and not major

version = None

path_root = Path(__file__).resolve().parent.parent
path_src = path_root / EXT_NAME
path_ext = path_src / 'azext_' + EXT_NAME.replace('-', '_')

with open(path_src / 'setup.py', 'r') as f:
    for line in f:
        if line.startswith('VERSION'):
            txt = str(line).rstrip()
            match = search(r'VERSION = [\'\"](.*)[\'\"]$', txt)
            if match:
                version = match.group(1)

if not version:
    raise ValueError('no version found in setup.py')

version_old = parse_version(version)

n_major = version_old.major + 1 if major else version_old.major
n_minor = 0 if major else version_old.minor + 1 if minor else version_old.minor
n_patch = 0 if major or minor else version_old.micro + 1

version_new = parse_version(f'{n_major}.{n_minor}.{n_patch}')


print(f'bumping version: {version_old.public} -> {version_new.public}')

fmt_setup = 'VERSION = \'{}\''
fmt_release = f'https://github.com/colbylwilliams/az-{EXT_NAME}/releases/latest/download/{EXT_NAME.replace("-", "_")}-{{}}-py3-none-any.whl'
fmt_history = '{}\n++++++\n{}\n\n{}'


print('..updating setup.py')

with open(path_src / 'setup.py', 'r') as f:
    setup = f.read()

if fmt_setup.format(version_old.public) not in setup:
    raise ValueError('version string not found in setup.py')

setup = setup.replace(fmt_setup.format(version_old.public), fmt_setup.format(version_new.public))

with open(path_src / 'setup.py', 'w') as f:
    f.write(setup)


print('..updating HISTORY.rst')

with open(path_src / 'HISTORY.rst', 'r') as f:
    history = f.read()

if version_old.public not in history:
    raise ValueError('version string not found in HISTORY.rst')

history = history.replace(version_old.public, fmt_history.format(version_new.public, notes, version_old.public))

with open(path_src / 'HISTORY.rst', 'w') as f:
    f.write(history)


# print('..updating Dockerfile')

# with open(path_builder / 'Dockerfile', 'r') as f:
#     docker = f.read()

# if fmt_release.format(version_old.public) not in docker:
#     raise ValueError('version string not found in Dockerfile')

# docker = docker.replace(fmt_release.format(version_old.public), fmt_release.format(version_new.public))

# with open(path_builder / 'Dockerfile', 'w') as f:
#     f.write(docker)


print('..updating README.md')

with open(path_root / 'README.md', 'r') as f:
    readme = f.read()

if fmt_release.format(version_old.public) not in readme:
    raise ValueError('version string not found in README.md')

readme = readme.replace(fmt_release.format(version_old.public), fmt_release.format(version_new.public))

with open(path_root / 'README.md', 'w') as f:
    f.write(readme)


# print('..updating _constants.py')

# with open(path_ext / '_constants.py', 'r') as f:
#     constants = f.read()

# if fmt_release.format(version_old.public) not in constants:
#     raise ValueError('version string not found in _constants.py')

# constants = constants.replace(fmt_release.format(version_old.public), fmt_release.format(version_new.public))

# with open(path_ext / '_constants.py', 'w') as f:
#     f.write(constants)
