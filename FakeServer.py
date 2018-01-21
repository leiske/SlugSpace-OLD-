from flask import Flask, render_template, redirect
from flaskext.mysql import MySQL
import pusher

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'slugspace'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
cursor = mysql.connect().cursor()

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
    cursor.execute("SELECT * from PARKING_LOTS")
    data = cursor.fetchall()
    return data

def getParkingLot(lotId):
    cursor.execute("SELECT * from PARKING_LOTS where id="+lotId)
    data = cursor.fetchall()
    return data


def getParkingEvents(lotId):
    cursor.execute("SELECT * from PARKING_EVENTS where lot_id="+lotId+" order by created_at desc")
    data = cursor.fetchall()
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

