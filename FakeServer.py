from flask import Flask, render_template, redirect

app = Flask(__name__)

title = "SlugSpace"

lots = [{'name':"West",'carsInLot':2,'remainingSpots':18},{'name':"East",'carsInLot':5,'remainingSpots':15},{'name':"North",'carsInLot':2,'remainingSpots':18}]

@app.route('/')
def parkingLot(): 
    return render_template('index.html', title=title,lots=lots)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')