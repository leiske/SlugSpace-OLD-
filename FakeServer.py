from flask import Flask, render_template, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'slugspace'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
cursor = mysql.connect().cursor()

@app.route('/')
def parkingLot():
    return render_template('index.html', title="SlugSpace", lots=getParkingLots())

def getParkingLots():
    cursor.execute("SELECT * from PARKING_LOTS")
    data = cursor.fetchall()
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
