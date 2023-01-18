# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=inconsistent-return-statements, unused-argument

# import requests

from azure.cli.core.commands.parameters import get_resources_in_resource_group, get_resources_in_subscription
from azure.cli.core.decorators import Completer

# from ._client_factory import cf_network, cf_resources
from ._github import get_github_releases
from ._logging import get_logger

log = get_logger(__name__)


# @Completer
# def subnet_completion_list(cmd, prefix, ns, **kwargs):
#     client = network_client_factory(cmd.cli_ctx)
#     if ns.resource_group_name and ns.vnet_name:
#         rg = ns.resource_group_name
#         vnet = ns.vnet_name
#         return [r.name for r in client.subnets.list(resource_group_name=rg, virtual_network_name=vnet)]


@Completer
def get_version_completion_list(cmd, prefix, ns, **kwargs):
    return [r['tag_name'] for r in get_github_releases()]


def get_resource_name_completion_list(group_option='resource_group_name', resource_type=None):

    @Completer
    def completer(cmd, prefix, ns, **kwargs):
        rg = getattr(ns, group_option, None)
        if rg:
            return [r.name for r in get_resources_in_resource_group(cmd.cli_ctx, rg, resource_type=resource_type)]
        return [r.name for r in get_resources_in_subscription(cmd.cli_ctx, resource_type)]

    return completer
