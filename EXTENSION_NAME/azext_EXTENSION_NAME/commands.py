# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from ._constants import EXT_NAME


def load_command_table(self, _):  # pylint: disable=too-many-statements

    with self.command_group(EXT_NAME, is_preview=True):
        pass

    with self.command_group(EXT_NAME) as g:
        # g.custom_command('test', f'{EXT_NAME.replace("-", "_")}_tests')
        g.custom_command('version', f'{EXT_NAME.replace("-", "_")}_version')
        g.custom_command('upgrade', f'{EXT_NAME.replace("-", "_")}_upgrade')
