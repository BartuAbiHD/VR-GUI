#!/bin/bash

# Get the path of the script's directory
scriptDir="$(dirname "$0")"

# Set the path to the Python runtime folder
runtimeFolder="${scriptDir}/runtime"

# Check if the runtime folder exists
if [ -f "${runtimeFolder}/python" ]; then
    # Runtime folder exists, so run the file using the runtime Python
    echo "Running with the runtime Python, Please wait."
    "${runtimeFolder}/python" vrgui.py --pycmd "${runtimeFolder}/python"
else
    # Runtime folder does not exist, so run the file using the system Python
    echo "Running with the system Python."
    python vrgui.py --pycmd python
fi