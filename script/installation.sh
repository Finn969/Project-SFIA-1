#!/bin/bash
source venv/bin/activate
sudo python3 -m pip install flask
sudo python3 -m pip install flask_mysqldb

python3 app.py