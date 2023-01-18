# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=logging-fstring-interpolation

from pathlib import Path

from knack.log import get_logger as knack_get_logger


def get_logger(name: str, file_path: Path = None):
    '''Get the logger for the extension'''
    _logger = knack_get_logger(name)

    # this must only happen in the builder, otherwise
    # the log file could be created on users machines
    if file_path is not None and file_path.is_file():
        import logging
        formatter = logging.Formatter('{asctime} [{name:^28}] {levelname:<8}: {message}',
                                      datefmt='%m/%d/%Y %I:%M:%S %p', style='{',)
        fh = logging.FileHandler(file_path)
        fh.setLevel(level=_logger.level)
        fh.setFormatter(formatter)
        _logger.addHandler(fh)

    return _logger
