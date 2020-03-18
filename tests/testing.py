#!/usr/bin/env python3 m pip install --upgrade flask
import urllib3
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
app = Flask(__name__)
app.config["MYSQL_HOST"] = #os.environ['MYSQLHOST']
app.config["MYSQL_USER"] = #os.environ['MYSQLUSE']
app.config["MYSQL_PASSWORD"] = #os.environ['MYSQLPASS']
app.config["MYSQL_DB"] =  #os.environ['MYSQLDB']
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
        cur.execute('SELECT notes FROM commanderstable WHERE firstname="Place" AND lastname="Holder"')
        placeholder_notes = cur.fetchall()
        assert placeholder_notes[0][0] == 'Placeholder'

def test_delete_ctable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO commanderstable (firstname,lastname,nationality,date_of_birth,bcad,notes) VALUES("Place","Holder","United States","2000-1-1","AD","Lorem Ipsum")')
        start_records = cur.execute('SELECT * FROM commanderstable')
        cur.execute('DELETE FROM commanderstable WHERE lastname = "Holder"')
        end_records = cur.execute('SELECT * FROM commanderstable')
        cur.close()
        assert end_records + 1 == start_records

def test_create_btable():
    with app.app_context():
        cur = mysql.connection.cursor()
        start_records = cur.execute('SELECT * FROM battlestable')
        cur.execute('INSERT INTO battlestable (location,startdate,enddate,bcad,type) VALUES("Placeholder","2000-1-1","2000-1-2","AD","Land")')
        end_records = cur.execute('SELECT * FROM battlestable')
        cur.close()
        assert end_records - 1 == start_records

def test_update_btable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO battlestable (location,startdate,enddate,bcad,type) VALUES("Placeholder","2000-1-1","2000-1-2","AD","Land")')
        cur.execute('SELECT location FROM battlestable')
        cur.execute('UPDATE battlestable SET type = "Siege"  WHERE location = "Placeholder"')    
        cur.execute('SELECT type FROM battlestable WHERE location="Placeholder"')
        placeholder_notes = cur.fetchall()
        assert placeholder_notes[0][0] == 'Siege'

def test_delete_btable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO battlestable (location,startdate,enddate,bcad,type) VALUES("Placeholder","2000-1-1","2000-1-2","AD","Land")')
        start_records = cur.execute('SELECT * FROM battlestable')
        cur.execute('DELETE FROM battlestable WHERE location = "Placeholder"')
        end_records = cur.execute('SELECT * FROM battlestable')
        cur.close()
        assert end_records + 1 == start_records

def test_create_rtable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO commanderstable (firstname,lastname,nationality,date_of_birth,bcad,notes) VALUES("Place","Holder","United States","2000-1-1","AD","Lorem Ipsum")')
        cur.execute('INSERT INTO battlestable (location,startdate,enddate,bcad,type) VALUES("Placeholder","2000-1-1","2000-1-2","AD","Land")')
        start_records = cur.execute('SELECT * FROM relations')
        cur.execute('INSERT INTO relations(generalID,battleID) VALUES((SELECT ID FROM commanderstable WHERE firstname = "Place" AND lastname = "Holder"),(SELECT ID FROM battlestable WHERE location = "Placeholder"))')
        end_records = cur.execute('SELECT * FROM relations')
        cur.close()
        assert end_records - 1 == start_records

def test_delete_rtable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO commanderstable (firstname,lastname,nationality,date_of_birth,bcad,notes) VALUES("Place","Holder","United States","2000-1-1","AD","Lorem Ipsum")')
        cur.execute('INSERT INTO battlestable (location,startdate,enddate,bcad,type) VALUES("Placeholder","2000-1-1","2000-1-2","AD","Land")')
        cur.execute('INSERT INTO relations(generalID,battleID) VALUES((SELECT ID FROM commanderstable WHERE firstname = "Place" AND lastname = "Holder"),(SELECT ID FROM battlestable WHERE location = "Placeholder"))')
        start_records = cur.execute('SELECT * FROM relations')
        cur.execute('DELETE FROM relations WHERE (generalID = (SELECT ID FROM commanderstable WHERE firstname = "Place" AND lastname = "Holder")) AND (battleID = (SELECT ID FROM battlestable WHERE location = "Placeholder"))')
        end_records = cur.execute('SELECT * FROM relations')
        cur.close()
        assert end_records + 1 == start_records