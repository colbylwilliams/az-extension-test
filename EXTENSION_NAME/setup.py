#!/usr/bin/env python

# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------


from codecs import open

from setuptools import find_packages, setup

try:
    from azure_bdist_wheel import cmdclass
except ImportError:
    from distutils import log as logger
    logger.warn("Wheel is not available, disabling bdist_wheel hook")

EXT_NAME = 'EXTENSION_NAME'

# Must match a HISTORY.rst entry.
VERSION = '0.0.1'

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
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
]

DEPENDENCIES = [
    'azure-cli-core'
]

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name=EXT_NAME,
    version=VERSION,
    description='Microsoft Azure Command-Line Tools EXTENSION_DESCRIPTION Extension',
    license='MIT',
    author='Microsoft Corporation',
    author_email='colbyw@microsoft.com',
    url=f'https://github.com/colbylwilliams/az-{EXT_NAME}',
    long_description=README + '\n\n' + HISTORY,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={f'azext_{EXT_NAME.replace("-", "_")}': ['azext_metadata.json']},
)
