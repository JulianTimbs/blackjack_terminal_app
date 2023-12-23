#!/bin/bash

python3 venv .venv
source .venv/bin/activate
pip3 install -U pytest &> /dev/null
pytest