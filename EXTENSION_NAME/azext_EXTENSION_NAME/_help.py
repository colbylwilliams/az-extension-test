# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

from ._constants import EXT_DESCRIPTION, EXT_NAME

helps[f'{EXT_NAME}'] = f"""
type: group
short-summary: {EXT_DESCRIPTION}.
"""

# -----------------------
# EXTENSION_NAME version
# EXTENSION_NAME upgrade
# -----------------------

helps[f'{EXT_NAME} version'] = f"""
type: command
short-summary: Show the version of the {EXT_NAME} extension.
"""

helps[f'{EXT_NAME} upgrade'] = f"""
type: command
short-summary: Update {EXT_NAME} cli extension.
examples:
  - name: Update {EXT_NAME} cli extension to the latest stable release.
    text: az {EXT_NAME} upgrade
  - name: Update {EXT_NAME} cli extension to the latest pre-release.
    text: az {EXT_NAME} upgrade --pre
  - name: Update {EXT_NAME} cli extension a specific version.
    text: az {EXT_NAME} upgrade --version 0.1.0
"""
