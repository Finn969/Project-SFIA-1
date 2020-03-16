#!/bin/bash
source venv/bin/activate
python3 -m pip install flask
python3 -m pip install flask_mysqldb

python3 app.py