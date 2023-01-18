import json
import os

from pathlib import Path
from re import search

EXT_NAME = 'EXTENSION_NAME'
EXT_DESCRIPTION = 'EXTENSION_DESCRIPTION'

ci = os.environ.get('CI', False)

path_root = Path(__file__).resolve().parent.parent
path_src = path_root / EXT_NAME
path_assets = path_root / 'release_assets' if ci else path_root / '.local/release_assets'

# Get CLI version
with open(path_src / 'setup.py', 'r') as f:
    for line in f:
        if line.startswith('VERSION'):
            txt = str(line).rstrip()
            match = search(r'VERSION = [\'\"](.*)[\'\"]$', txt)
            if match:
                cli_version = match.group(1)
                cli_name = '{}-{}-py3-none-any.whl'.format(EXT_NAME.replace('-', '_'), cli_version)

version = f'v{cli_version}'
download_url = f'https://github.com/colbylwilliams/az-{EXT_NAME}/releases/download/{version}' if ci else path_assets

index = {}
index['extensions'] = {
    f'{EXT_NAME}': [
        {
            'downloadUrl': f'{download_url}/{cli_name}',
            'filename': f'{cli_name}',
            'metadata': {
                'azext.isPreview': True,
                'azext.isExperimental': True,
                'azext.minCliCoreVersion': '2.40.0',
                'azext.maxCliCoreVersion': '3.0.0',
                'classifiers': [
                    'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'Intended Audience :: System Administrators',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3.8',
                    'Programming Language :: Python :: 3.9',
                    'Programming Language :: Python :: 3.10',
                    'License :: OSI Approved :: MIT License',
                ],
                'extensions': {
                    'python.details': {
                        'contacts': [
                            {
                                'email': 'colbyw@microsoft.com',
                                'name': 'Microsoft Corporation',
                                'role': 'author'
                            }
                        ],
                        'document_names': {
                            'description': 'DESCRIPTION.rst'
                        },
                        'project_urls': {
                            'Home': f'https://github.com/colbylwilliams/az-{EXT_NAME}'
                        }
                    }
                },
                'generator': 'bdist_wheel (0.30.0)',
                'license': 'MIT',
                'metadata_version': '2.0',
                'name': f'{EXT_NAME}',
                'summary': f'Microsoft Azure Command-Line Tools {EXT_DESCRIPTION} Extension',
                'version': f'{cli_version}'
            }
        }
    ]
}

# save index.json to assets folder
with open(f'{path_assets}/index.json', 'w') as f:
    json.dump(index, f, ensure_ascii=False, indent=4, sort_keys=True)

assets = []

# add all the files in the root of the assets folder to the assets list
with os.scandir(path_assets) as s:
    for f in s:
        if f.is_file():
            print(f.path)
            assets.append({'name': f.name, 'path': f.path})


if not ci:  # if working locally, print the assets.json to a file
    with open(f'{path_assets}/assets.json', 'w') as f:
        json.dump(assets, f, ensure_ascii=False, indent=4, sort_keys=True)


github_output = os.environ.get('GITHUB_OUTPUT', None)
if github_output:
    with open(github_output, 'a+') as f:
        f.write(f'assets={json.dumps(assets)}')
