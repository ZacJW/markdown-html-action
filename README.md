# markdown-html-action

Renders markdown files to HTML files using Python's markdown package.

- Supports third-party extensions such as [PyMdown](https://facelessuser.github.io/pymdown-extensions/)
- Supports finding input files with glob pattern matching and/or lists of files
- Files that match glob patterns are naturally sorted
  - `file*.md` will match in order: `file1.md`, `file2.md`, `file11.md`
  - See [natsort](https://github.com/SethMMorton/natsort) for more info
- Supports generating multiple output files, each with different inputs
- Supports building in a stylesheet to all output files as a `<style>` block

## Usage

```yaml
      - uses: ZacJW/markdown-html-action@1.1.0
        with:
          input_files: '[["wildcard*.md"], ["dir1/*.md", "dir2/*.md]]'
          output_files: '["out1.html", "out2.html"]'
          builtin_stylesheet: 'style.css'
          packages: 'pymdown-extensions'
          extensions: '["pymdownx.extra"]'
```

This example will create two output files, `out1.html` and `out2.html` in the root of the repo. `out1.html` will be build from all files that match `wildcard*.md` in the root of the repo.

`out2.html` will be built from all `.md` files immediately in `dir1` and `dir2`, with `dir1`'s files appearing first in the output.

All outputs will be built using the `pymdownx.extra` extension pack, and the `pymdown-extensions` package has been installed to facilitate this.

All outputs will include a `<style>` block with the contents of the `style.css` stylesheet inside.

## Inputs

### `input_files`

**Required**. A JSON list of lists of paths to markdown files to render in to HTML files. Each sublist corresponds to a path in `output files`, with each path in the sublist being rendered in the order they appear to produce the output.

If a path in a sublist is a glob pattern, all matching files will be rendered into the output, but they will be done in order according to [natsort](https://github.com/SethMMorton/natsort) on their path. `file*.md` will match in order: `file1.md`, `file2.md`, `file11.md`

### `output_files`

**Required**. A JSON list of paths to save the rendered HTML files to. Each path corresponds to a sublist in `input_files`, with each path in the sublist being rendered in the order they appear to produce the output.

### `exclude_duplicates`

*Optional*. (boolean) Whether or not a file should be automatically excluded from being included more than once in a given output file. If it is included more than once, only the first occurrence appears in the output file.

This does not exclude a file from being included in more than one output file.

**If not specified**, defaults to true

### `builtin_stylesheet`

*Optional*. A path to a stylesheet to be included as a `<style>` block at the end of every output file.

**If not specified**, no `<style>` block will be created.

### `packages`

*Optional*. A space separated list of Python packages to be installed before execution (useful for installing third-party markdown extensions) i.e. what you would write after `pip install`.

**If not specified**, no additional packages will be installed.

### `extensions`

*Optional*. A JSON list of extensions to be passed to Python markdown. See [Python-Markdown](https://python-markdown.github.io/extensions/) for details. Also supports third-party extensions so long as their packages have been installed using the `packages` input.

**If not specified**, the built-in `extra` extension pack will be enabled.

### `extension_configs`

*Optional*. A JSON object of extension configurations. See [Python-Markdown](https://python-markdown.github.io/reference/#extension_configs) for details.

**If not specified**, extensions will use default configurations.
