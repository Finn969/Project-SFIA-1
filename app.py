from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
app = Flask(__name__)
app.config["MYSQL_HOST"] = '35.234.149.105' #os.environ['MYSQLHOST']
app.config["MYSQL_USER"] = 'root' #os.environ['MYSQLUSE']
app.config["MYSQL_PASSWORD"] = 'Pr0metheus' #os.environ['MYSQLPASS']
app.config["MYSQL_DB"] = 'battlesdb'#os.environ['MYSQLDB']
mysql= MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
         details = request.form
         FName = details['Forename']
         LName = details['Surname']
         Country = details['Nationality']
         Birthday = details['Date_of_Birth']
         Notes = details['Notes']
         cur.execute("INSERT INTO commanderstable(firstname,lastname,nationality,date_of_birth,notes) VALUES(%s,%s,%s,%s,%s)", (FName,LName,Country,Birthday,Notes))
         mysql.connection.commit()

    cur.execute('SELECT * FROM commanderstable')
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
         Location = details['Location']
         start = details['Start']
         end = details['End']
         type = details['Type']
         cur.execute("INSERT INTO battlestable(location,startdate,enddate,type) VALUES(%s,%s,%s,%s)", (Location,start,end,type))
         mysql.connection.commit()

    cur.execute('SELECT * FROM battlestable')
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
    cur.execute('SELECT * FROM commanderstable')
    rows = cur.fetchall()
    mysql.connection.commit()
    commanderinfo = []
    for row in rows:
        commanderinfo.append(row)
    return render_template('homepage.html', commanderinfo = commanderinfo)

@app.route('/delete/battle', methods=['GET', 'POST'])
def delete_battle():
    remove_name = request.form["RemoveThis"]
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM battlestable WHERE location LIKE %s',(remove_name,))
    cur.execute('SELECT * FROM battlestable')
    rows = cur.fetchall()
    mysql.connection.commit()
    battleinfo = []
    for row in rows:
        battleinfo.append(row)
    return render_template('homepage.html', battleinfo=battleinfo)




if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)