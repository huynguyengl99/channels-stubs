#!/usr/bin/env bash

if [ "$1" == "--fix" ]; then
  ruff check . --fix && black ./channels-stubs && toml-sort ./*.toml
else
  ruff check . && black ./channels-stubs --check && toml-sort ./*.toml --check
fi
