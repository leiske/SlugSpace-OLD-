from flask import Flask, render_template

app = Flask(__name__)

title = "Parking Counter"

@app.route('/')
def index():
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')