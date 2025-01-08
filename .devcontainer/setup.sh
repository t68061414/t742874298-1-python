#!/bin/bash

# Install the speakeasy CLI
curl -fsSL https://raw.githubusercontent.com/speakeasy-api/speakeasy/main/install.sh | sh

# Setup samples directory
rmdir samples || true
mkdir samples

python -m pip install --upgrade pip
pip install -e .

# Generate starter usage sample with speakeasy
speakeasy generate usage -s https://example.com/OVERWRITE_WHEN_SAMPLE_SPEC_IS_WRITTEN -l python -o samples/root.py