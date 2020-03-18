#!/usr/bin/env python3 m pip install --upgrade flask
import urllib3
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
app = Flask(__name__)
app.config["MYSQL_HOST"] = '35.234.149.105' #os.environ['MYSQLHOST']
app.config["MYSQL_USER"] = 'root' #os.environ['MYSQLUSE']
app.config["MYSQL_PASSWORD"] = 'Pr0metheus'# os.environ['MYSQLPASS']
app.config["MYSQL_DB"] = 'battlesdb'# os.environ['MYSQLDB']
mysql= MySQL(app)

def test_homepage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/')
    assert 200 == r.status

def test_battlespage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/battles')
    assert 200 == r.status

def test_updateGpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/update/commander')
    assert 200 == r.status

def test_updateBpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/update/battle')
    assert 200 == r.status

def test_relationspage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/event')
    assert 200 == r.status

def test_select_ctable():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_records = cur.execute('SELECT * FROM commanderstable')
        mysql.connection.commit()
        cur.close()
        assert 6 == num_records

def test_create_ctable():
    with app.app_context():
        cur = mysql.connection.cursor()
        start_records = cur.execute('SELECT * FROM commanderstable')
        cur.execute('INSERT INTO commanderstable (firstname,lastname,nationality,date_of_birth,bcad,notes) VALUES("Place","Holder","United States","2000-1-1","AD","Lorem Ipsum")')
        end_records = cur.execute('SELECT * FROM commanderstable')
        cur.close()
        assert end_records - 1 == start_records

def test_update_ctable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO commanderstable (firstname,lastname,nationality,date_of_birth,bcad,notes) VALUES("Place","Holder","United States","2000-1-1","AD","Lorem Ipsum")')
        cur.execute('SELECT firstname,lastname FROM commanderstable')
        cur.execute('UPDATE commanderstable SET notes = "Placeholder"  WHERE firstname = "Place" AND lastname = "Holder"')    
        placeholder_notes = cur.execute('SELECT notes FROM commanderstable WHERE firstname="Place" AND lastname="Holder"')
        assert placeholder_notes == 'Placeholder'

def test_delete_ctable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO commanderstable (firstname,lastname,nationality,date_of_birth,bcad,notes) VALUES("Place","Holder","United States","2000-1-1","AD","Lorem Ipsum")')
        start_records = cur.execute('SELECT * FROM commanderstable')
        cur.execute('DELETE FROM commanderstable WHERE lastname = "Holder"')
        end_records = cur.execute('SELECT * FROM commanderstable')
        cur.close()
        assert end_records + 1 == start_records