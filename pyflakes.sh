#!/bin/bash

echo "============================================================"
echo "== pyflakes =="
pyflakes yaset | grep -v migration
