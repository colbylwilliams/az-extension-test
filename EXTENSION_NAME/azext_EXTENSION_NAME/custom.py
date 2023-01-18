# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=line-too-long, logging-fstring-interpolation, too-many-locals, too-many-statements, unused-argument

from azure.cli.core.azclierror import CLIError
from azure.cli.core.extension.operations import show_extension, update_extension
from packaging.version import parse as parse_version

from ._constants import EXT_NAME
from ._github import get_github_latest_release_version, get_github_release
from ._logging import get_logger

log = get_logger(__name__)


# def EXTENSION_NAME_tests(cmd):


# -----------------------
# EXTENSION_NAME version
# EXTENSION_NAME upgrade
# -----------------------

def EXTENSION_NAME_version(cmd):
    ext = show_extension(EXT_NAME)
    current_version = 'v' + ext['version']
    is_dev = 'extensionType' in ext and ext['extensionType'] == 'dev'
    log.info(f'Current version: {current_version}')
    current_version_parsed = parse_version(current_version)
    print(f'az {EXT_NAME} version: {current_version}{" (dev)" if is_dev else ""}')

    # TODO: this throws if there's no releases yet
    latest_version = get_github_latest_release_version()
    log.info(f'Latest version: {latest_version}')
    latest_version_parsed = parse_version(latest_version)

    if current_version_parsed < latest_version_parsed:
        log.warning(f'There is a new version of az {EXT_NAME} {latest_version}. '
                    f'Please update using: az {EXT_NAME} upgrade')


def EXTENSION_NAME_upgrade(cmd, version=None, prerelease=False):
    ext = show_extension(EXT_NAME)
    current_version = 'v' + ext['version']
    log.info(f'Current version: {current_version}')
    current_version_parsed = parse_version(current_version)

    release = get_github_release(version=version, prerelease=prerelease)

    new_version = release['tag_name']
    log.info(f'Latest{" prerelease" if prerelease else ""} version: {new_version}')
    new_version_parsed = parse_version(new_version)

    is_dev = 'extensionType' in ext and ext['extensionType'] == 'dev'

    if not is_dev and new_version_parsed == current_version_parsed:
        print(f'Already on latest{" prerelease" if prerelease else ""} version: {new_version}')
        return

    if not is_dev and new_version_parsed < current_version_parsed:
        print(f'Current version is newer than latest{" prerelease" if prerelease else ""} version: {new_version}')
        return

    log.info(f'Upgrading to latest{" prerelease" if prerelease else ""} version: {new_version}')
    index = next((a for a in release['assets'] if 'index.json' in a['browser_download_url']), None)

    index_url = index['browser_download_url'] if index else None
    if not index_url:
        raise CLIError(f'Could not find index.json asset on release {new_version}. '
                       'Specify a specific prerelease version with --version/-v or use latest prerelease with --pre')

    if is_dev:
        log.warning('Skipping upgrade of dev extension.')
        return

    update_extension(cmd, extension_name=EXT_NAME, index_url=index_url)
