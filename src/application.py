from flask import Flask, url_for
from flask import request
from flask import render_template
import distance
import emission_calc

app = Flask(__name__)

# open the main screen
@app.route("/")
def start():
    url_for('static', filename='main.css')
    return render_template('index.html')

# open the search screen
@app.route("/app.html")
def lookup():
    url_for('static', filename='app.css')
    return render_template('app.html')

# run through and calculate everything
@app.route("/app", methods=['POST', 'GET'])
def calc():
    error=None
    if request.method == 'POST':
        if request.form['starting-point'] != None and request.form['destination'] != None and request.form['mpg'] != '0':
            dist = distance.getDistance(request.form['starting-point'], request.form['destination'])
            print (dist)
            if dist == -1:
                return render_template('app.html', error=error)
            emission = emission_calc.calcFootprint(request.form['mpg'], dist)
            # monthTravels = emission_calc.numTravelsInMonth(emission)
            yearTravels = emission_calc.numTravelsInYear(emission)
            trees = emission_calc.numTrees(emission)
            homes = emission_calc.numPerHomePerYear(emission)

            data = (emission, homes, trees, yearTravels)
            return render_template('test.html', data=data)
    return render_template('app.html', error=error)

app.run()
