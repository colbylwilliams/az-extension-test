# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType

from ._constants import EXT_DIR_NAME
from ._help import helps  # pylint: disable=unused-import
from ._params import load_arguments
from .commands import load_command_table


class EXTENSION_NAMECommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        custom_command_type = CliCommandType(operations_tmpl=f'{EXT_DIR_NAME}.custom#{{}}')
        super().__init__(cli_ctx=cli_ctx, custom_command_type=custom_command_type)

    def load_command_table(self, args):
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        load_arguments(self, command)


COMMAND_LOADER_CLS = EXTENSION_NAMECommandsLoader
