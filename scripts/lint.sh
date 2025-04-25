#!/usr/bin/env bash

if [ "$1" == "--fix" ]; then
  ruff check . --fix && black ./channels_stubs && toml-sort ./*.toml
else
  ruff check . && black ./channels_stubs --check && toml-sort ./*.toml --check
fi
