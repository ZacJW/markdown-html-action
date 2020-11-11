#!/bin/bash -e

pip3 install markdown natsort

if [ -n "$INPUT_PACKAGES" ]; then
    pip3 install "$INPUT_PACKAGES"
fi

python3 /markdown-html.py
