#!/bin/python3

import markdown, natsort, os, json, pathlib

md = markdown.Markdown(extensions=["tables", "toc"], output_format="html5")
os.environ['GITHUB_WORKSPACE'] = '.'
os.environ['INPUT_INPUT_FILES'] = '[["t/w*.md"]]'
os.environ['INPUT_OUTPUT_FILES'] = '["out.html"]'
os.environ['INPUT_EXCLUDE_DUPLICATES'] = 'true'

REPO_PATH = pathlib.Path(os.environ['GITHUB_WORKSPACE'])
INPUT_LIST = json.loads(os.environ['INPUT_INPUT_FILES'])
OUTPUT_LIST = json.loads(os.environ['INPUT_OUTPUT_FILES'])
EXCLUDE_DUPLICATES : bool = json.loads(os.environ['INPUT_EXCLUDE_DUPLICATES'])

if not isinstance(INPUT_LIST, list):
    raise ValueError()

for sublist in INPUT_LIST:
    if not isinstance(sublist, list):
        raise ValueError()

if not isinstance(OUTPUT_LIST, list):
    raise ValueError()

if len(OUTPUT_LIST) != len(INPUT_LIST):
    raise ValueError()

for input_sublist, output_path_str in zip(INPUT_LIST, OUTPUT_LIST):
    md.reset()
    md_str = ""
    input_path_included = set()
    for input_path_glob_str in input_sublist:
        input_path_list = natsort.natsorted([str(p) for p in REPO_PATH.glob(input_path_glob_str)])
        for input_path_str in input_path_list:
            if not EXCLUDE_DUPLICATES or input_path_str not in input_path_included:
                input_path_included.add(input_path_str)
                with open(input_path_str, 'r') as input_file:
                    md_str += input_file.read() + "\n"
    output_path = REPO_PATH.joinpath(output_path_str)
    html = md.convert(md_str)
    with open(output_path, 'w') as output_file:
        output_file.write(html)
