#!/bin/bash

source ~/.bashrc
python3 -m pytest ./tests/testing.py
python3 -m coverage run -m --source=. pytest ./tests/testing.py
python3 -m coverage report -m ./tests/testing.py