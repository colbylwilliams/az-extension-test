# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=line-too-long

from datetime import datetime, timezone

timestamp = datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')

EXT_NAME = 'EXTENSION_NAME'
EXT_DESCRIPTION = 'EXTENSION_DESCRIPTION'

EXT_DIR_NAME = f'azext_{EXT_NAME.replace("-", "_")}'
EXT_REPO_NAME = f'az-{EXT_NAME}'
EXT_REPO_OWNER = 'colbylwilliams'
