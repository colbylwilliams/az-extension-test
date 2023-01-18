#!/bin/bash

set -e

cdir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
extdir=${cdir%/*}

EXT_NAME = "EXTENSION_NAME"

echo "Azure CLI Build Utility"
echo ""

pushd $extdir > /dev/null

    echo "Creating a virtual environment"
    python -m venv .venv
    echo ""

    echo "Activating virtual environment"
    source .venv/bin/activate
    echo ""

    echo "Installing Azure CLI Dev Tools (azdev)"
    pip install azdev
    echo ""

    echo "Setting up Azure CLI Dev Tools (azdev)"
    azdev setup -r $PWD -e $EXT_NAME
    echo ""

    echo "Running Linter on $EXT_NAME extension source"
    azdev linter $EXT_NAME
    echo ""

    echo "Running Style Checks on $EXT_NAME extension source"
    azdev style $EXT_NAME
    echo ""

    echo "Building $EXT_NAME extension"
    azdev extension build $EXT_NAME --dist-dir ./release_assets
    echo ""

    echo "Deactivating virtual environment"
    deactivate
    echo ""

popd > /dev/null

echo "Done."
echo ""
