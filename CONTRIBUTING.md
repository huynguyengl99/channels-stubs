# Contributing to Channels Stubs

Contributions are welcome! Here are some pointers to help you install the library for development and validate your changes before submitting a pull request.

## Install the library for development

First install [uv](https://docs.astral.sh/uv/getting-started/installation/), create your own `.venv`
and activate it:

```bash
uv venv # or pythin -m venv .venv
source .venv/bin/activate
```

Then use uv install all dev package:
```bash
uv sync
```

## Validate the changes before creating a pull request

1. Make sure the existing stub tests are still passing:

```bash
scripts/stubtest.sh
```

2. Reformat and validate the code with the following tools:

```bash
bash scripts/lint.sh [--fix]
```

3. For committing code, use the [Commitizen](https://commitizen-tools.github.io/commitizen/) tool to follow
commit best practices.

```bash
cz commit
```

These steps are also run automatically in the CI when you open the pull request.
