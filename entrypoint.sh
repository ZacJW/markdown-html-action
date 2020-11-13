#!/bin/bash -e

pip3 install markdown natsort

if [ -n "$INPUT_PACKAGES" ]; then
    IFS=' ' read -ra packages_array <<< "$INPUT_PACKAGES"
    pip3 install "${packages_array[@]}"
fi

python3 /markdown-html.py
