#!/bin/bash -e

ruff format src tests
ruff src tests --fix
pyright src tests
