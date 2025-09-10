#!/bin/bash

# Exit immediately if a command fails
set -e

# Define your GitHub repo name
REPO_NAME="staticsite"

# Run the generator with basepath set to /REPO_NAME/
echo "Building site with basepath: /$REPO_NAME/"
python3 src/main.py "/$REPO_NAME/"

echo "Build complete. Output is in the docs/ directory."
