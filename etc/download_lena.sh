#!/bin/sh
# Example script demonstrating data prep for package distribution
# This doesn't have to be included for the package to work, but is useful for developers
# So it goes in etc

LENA_URL="https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"

curl -o src/packagename/data/images/lena.png "$LENA_URL"