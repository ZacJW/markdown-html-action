#!/bin/bash -e

pip3 install markdown natsort

if [ -n "$INPUT_PACKAGES" ]; then
    IFS=' ' read -ra packages <<< "$INPUT_PACKAGES"
    for p in "$packages[@]"; do
        printf "%s\n" "$p" >> packages.txt
    done
    pip3 install -r packages.txt
fi

python3 /markdown-html.py
