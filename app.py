#!/usr/bin/env python3 m pip install --upgrade flask
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
app = Flask(__name__)
app.config["MYSQL_HOST"] = os.environ['MYSQLHOST']
app.config["MYSQL_USER"] = os.environ['MYSQLUSE']
app.config["MYSQL_PASSWORD"] = os.environ['MYSQLPASS']
app.config["MYSQL_DB"] = os.environ['MYSQLDB']
mysql= MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
         details = request.form
         FName = (details['Forename']).title()
         LName = (details['Surname']).title()
         Country = (details['Nationality']).title()
         Birthday = details['Date_of_Birth']
         BCAD = details['bcad']
         Notes = details['Notes']
         cur.execute("INSERT INTO commanderstable(firstname,lastname,nationality,date_of_birth,bcad,notes) VALUES(%s,%s,%s,%s,%s,%s)", (FName,LName,Country,Birthday,BCAD,Notes))
         mysql.connection.commit()

    cur.execute('''SELECT firstname,lastname,nationality,DATE_FORMAT(date_of_birth, '%D %M %Y'),bcad,notes FROM commanderstable''')
    rows = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    commanderinfo = []
    for row in rows:
        commanderinfo.append(row)
    return render_template('homepage.html', commanderinfo = commanderinfo)

@app.route('/battles', methods=['GET','POST'])
def battlespage():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
         details = request.form
         Location = (details['Location']).title()
         start = details['Start']
         end = details['End']
         BCAD = details['bcad']
         type = details['Type']
         result = details['Result']
         wCommand = details['wCommander']
         lCommand = details['lCommander']
         wStrength = details['wStrong']
         lStrength = details['lStrong']

         cur.execute("INSERT INTO armiestable(strength,commanderID) VALUES(%s,(SELECT ID FROM commanderstable WHERE lastname = %s))",(wStrength,wCommand))
         cur.execute("INSERT INTO armiestable(strength,commanderID) VALUES(%s,(SELECT ID FROM commanderstable WHERE lastname = %s))",(lStrength,lCommand))
         cur.execute("INSERT INTO battlestable(location,startdate,enddate,bcad,type,result,winner,loser) VALUES(%s,%s,%s,%s,%s,%s,(SELECT armyID FROM armiestable WHERE strength = %s),(SELECT armyID FROM armiestable WHERE strength = %s))", (Location,start,end,BCAD,type,result,wStrength,lStrength))
         mysql.connection.commit()
    cur.execute('''SELECT location,DATE_FORMAT(startdate, '%D %M %Y'),DATE_FORMAT(enddate, '%D %M %Y'),bcad,type,result,armiestable.strength,commanderstable.firstname,commanderstable.lastname,commanderstable.nationality FROM battlestable,armiestable,commanderstable WHERE battlestable.winner = armiestable.armyID AND armiestable.commanderID = commanderstable.ID''')
    rows = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    battleinfo = []
    for row in rows:
        battleinfo.append(row)
    return render_template('battlespage.html', battleinfo=battleinfo)


@app.route('/delete/commander', methods=['GET', 'POST'])
def delete_commander():
    remove_name = request.form["DeleteThis"]
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM commanderstable WHERE lastname LIKE %s',(remove_name,))
    cur.execute('''SELECT firstname,lastname,nationality,DATE_FORMAT(date_of_birth, '%D %M %Y'),bcad,notes FROM commanderstable''')
    rows = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    commanderinfo = []
    for row in rows:
        commanderinfo.append(row)
    return render_template('homepage.html', commanderinfo = commanderinfo)

@app.route('/delete/battle', methods=['GET', 'POST'])
def delete_battle():
    remove_name = request.form["RemoveThis"].title()
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM battlestable WHERE location LIKE %s',(remove_name,))
    cur.execute('''SELECT location,DATE_FORMAT(startdate, '%D %M %Y'),bcad,DATE_FORMAT(startdate, '%D %M %Y'),bcad,type FROM battlestable''')
    rows = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    battleinfo = []
    for row in rows:
        battleinfo.append(row)
    return render_template('battlespage.html', battleinfo=battleinfo)

@app.route('/update/battle', methods=['GET','POST'])
def update_battle():
    cur = mysql.connection.cursor()
    cur.execute('SELECT location FROM battlestable')
    rows = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    battleinfo = []
    for row in rows:
        battleinfo.append(row)
    if request.method == 'POST':
        details = request.form
        cur = mysql.connection.cursor()
        
        OLocation = details['OLocation'].title()
        ULocation = details['Location'].title()
        Ustart = details['Start']
        Uend = details['End']
        UBCAD = details['bcad']
        Utype = details['Type']
        cur.execute("UPDATE battlestable SET location = %s,startdate = %s,enddate = %s,bcad = %s,type = %s  WHERE location = %s;",(ULocation,Ustart,Uend,UBCAD,Utype,OLocation))
        cur.execute('''SELECT location,DATE_FORMAT(startdate, '%D %M %Y'),bcad,DATE_FORMAT(startdate, '%D %M %Y'),bcad,type FROM battlestable''')
        rows = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        battleinfo = []
        for row in rows:
            battleinfo.append(row)
        return render_template('battlespage.html', battleinfo=battleinfo)
    return render_template('updatebattle.html', battleinfo = battleinfo)

@app.route('/update/commander', methods=['GET','POST'])
def update_commander():
    cur = mysql.connection.cursor()
    cur.execute('SELECT lastname FROM commanderstable')
    rows = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    info = []
    for row in rows:
        info.append(row)
    if request.method == 'POST':
        details = request.form
        cur = mysql.connection.cursor()
        OLName = details['OSurname'].title()
        FName = details['UForename'].title()
        LName = details['USurname'].title()
        Country = details['UNationality'].title()
        Birthday = details['UDate_of_Birth']
        BCAD = details['Ubcad']
        Notes = details['UNotes']
        cur.execute("UPDATE commanderstable SET firstname = %s,lastname = %s,nationality = %s,date_of_birth = %s,bcad = %s,notes = %s  WHERE lastname = %s;",(FName,LName,Country,Birthday,BCAD,Notes,OLName))
        cur.execute('''SELECT firstname,lastname,nationality,DATE_FORMAT(date_of_birth, '%D %M %Y'),bcad,notes FROM commanderstable''')
        rows = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        commanderinfo = []
        for row in rows:
            commanderinfo.append(row)
        return render_template('homepage.html', commanderinfo = commanderinfo)
    return render_template('updategeneral.html', info = info)

@app.route('/event', methods=['GET','POST'])
def assign_to_event():
    eventinfo = []
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        details = request.form
        LName = details['Surname']
        Location = details['Location']
        cur.execute('INSERT INTO relations(generalID,battleID) VALUES((SELECT ID FROM commanderstable WHERE lastname = %s),(SELECT ID FROM battlestable WHERE location = %s))',(LName,Location))
        mysql.connection.commit()
        cur.execute('SELECT commanderstable.firstname, commanderstable.lastname, battlestable.location, relations.eventID FROM commanderstable, battlestable, relations WHERE commanderstable.ID = relations.generalID AND battlestable.ID = relations.battleID')
        rows = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        eventinfo = []
        for row in rows:
            eventinfo.append(row)
        return render_template('events.html', eventinfo = eventinfo)
    cur.execute('SELECT commanderstable.firstname, commanderstable.lastname, battlestable.location, relations.eventID FROM commanderstable, battlestable, relations WHERE commanderstable.ID = relations.generalID AND battlestable.ID = relations.battleID')
    rows = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    for row in rows:
        eventinfo.append(row)
    return render_template('events.html', eventinfo = eventinfo)

@app.route('/delete/event', methods=['GET', 'POST'])
def delete_relation():
    eventinfo = []
    remove_name = request.form["UnassignThis"]
    remove_location = request.form['UnassignThisToo']
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM relations WHERE (generalID = (SELECT ID FROM commanderstable WHERE lastname = %s)) AND (battleID = (SELECT ID FROM battlestable WHERE location = %s)) ',(remove_name,remove_location))
    cur.execute('SELECT commanderstable.firstname, commanderstable.lastname, battlestable.location, relations.eventID FROM commanderstable, battlestable, relations WHERE commanderstable.ID = relations.generalID AND battlestable.ID = relations.battleID')
    rows = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    for row in rows:
        eventinfo.append(row)
    return render_template('events.html', eventinfo = eventinfo)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)