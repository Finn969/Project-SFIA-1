#!/bin/bash
source venv/bin/activate
sudo python3 -m pip3 install flask
sudo python3 -m pip3 install flask_mysqldb

python3 app.py