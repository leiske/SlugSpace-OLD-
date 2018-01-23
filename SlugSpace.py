from flask import Flask, render_template, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'oops_I_had_to_change_the_password'
app.config['MYSQL_DATABASE_DB'] = 'oops_I_had_to_change_the_db'
app.config['MYSQL_DATABASE_HOST'] = 'oops_had_to_move_our_db'

mysql.init_app(app)
conn = mysql.connect()
conn.autocommit(True)
cursor = conn.cursor()

lots = {"1","2","3"}

@app.route('/')
def parkingLot():
    return render_template('index.html', title="SlugSpace", lots=getParkingLots())

@app.route('/<lotId>')
def moreInfo(lotId):
    if(lotId not in lots):
        return render_template('404.html')
    return render_template('moreInfo.html',title="SlugSpace", lot=getParkingLot(lotId), events=getParkingEvents(lotId))

def getParkingLots():
    cursor.execute("SELECT * from parking_lots")
    data = cursor.fetchall()
    print(data)
    return data

def getParkingLot(lotId):
    cursor.execute("SELECT * from parking_lots where id="+lotId)
    data = cursor.fetchall()
    return data


def getParkingEvents(lotId):
    cursor.execute("SELECT * from parking_events where lot_id="+lotId+" order by created_at desc limit 20")
    data = cursor.fetchall()
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

