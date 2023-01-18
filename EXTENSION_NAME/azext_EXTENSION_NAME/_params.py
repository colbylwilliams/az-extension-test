# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=line-too-long, too-many-statements

# from argcomplete.completers import DirectoriesCompleter, FilesCompleter
# from azure.cli.core.commands.parameters import (file_type, get_enum_type, get_location_type,
#                                                 get_resource_group_completion_list, tags_type)
# from knack.arguments import CLIArgumentType

from ._completers import get_version_completion_list
from ._constants import EXT_NAME
from ._validators import out_validator, source_version_validator

# get_resource_group_completion_list,)


def load_arguments(self, _):

    # outfile_type validator also validates outdir_type and stdout_type
    # outfile_type = CLIArgumentType(options_list=['--outfile'], completer=FilesCompleter(), validator=out_validator, help='When set, saves the output as the specified file path.')
    # outdir_type = CLIArgumentType(options_list=['--outdir'], completer=DirectoriesCompleter(), help='When set, saves the output at the specified directory.')
    # stdout_type = CLIArgumentType(options_list=['--stdout'], action='store_true', help='When set, prints all output to stdout instead of corresponding files.')

    with self.argument_context(f'{EXT_NAME} upgrade') as c:
        c.argument('version', options_list=['--version', '-v'], help='Version (tag). Default: latest stable.',
                   validator=source_version_validator, completer=get_version_completion_list)
        c.argument('prerelease', options_list=['--pre'], action='store_true',
                   help='Update to the latest prerelease version.')
