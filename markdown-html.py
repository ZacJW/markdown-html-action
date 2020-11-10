#!/bin/python3

print("- Markdown-HTML -")

import markdown, natsort, os, json, pathlib

md = markdown.Markdown(extensions=["extra", "toc"], output_format="html5")

REPO_PATH = pathlib.Path(os.environ['GITHUB_WORKSPACE'])
INPUT_LIST = json.loads(os.environ['INPUT_INPUT_FILES'])
OUTPUT_LIST = json.loads(os.environ['INPUT_OUTPUT_FILES'])
EXCLUDE_DUPLICATES : bool = json.loads(os.environ['INPUT_EXCLUDE_DUPLICATES'])
BUILTIN_STYLESHEET : str = os.environ['INPUT_BUILTIN_STYLESHEET']

if not isinstance(INPUT_LIST, list) or not all([isinstance(sublist, list) for sublist in INPUT_LIST]):
    raise ValueError("input_files must be a JSON list of lists")

if not isinstance(OUTPUT_LIST, list):
    raise ValueError("output_files must be a JSON list")

if len(OUTPUT_LIST) != len(INPUT_LIST):
    raise ValueError(f"input_files (length: {len(INPUT_LIST)}) must be the same length as output_files (length: {len(OUTPUT_LIST)})")

if BUILTIN_STYLESHEET != "":
    with open(REPO_PATH.joinpath(BUILTIN_STYLESHEET), 'r') as stylesheet_file:
        style = "<style>\n" + stylesheet_file.read() + "</style>\n"
else:
    style = ""

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
    print("Generating", output_path_str)
    output_path = REPO_PATH.joinpath(output_path_str)
    html = md.convert(md_str) + "\n" + style
    with open(output_path, 'w') as output_file:
        output_file.write(html)
print("Markdown-HTML complete")
