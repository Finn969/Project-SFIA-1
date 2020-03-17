#!/bin/bash
source venv/bin/activate
python3 -m pip install flask
python3 -m pip install flask_mysqldb
python3 -m pip3 install urllib3
python3 -m pip3 install pytest
python3 -m pip3 install coverage
source ~/.bashrc
python3 app.py