from flask import Flask
from flask import request
import distance
import emission_calc

app = Flask(__name__)

@app.route("/calculator", methods=['POST', 'GET'])
def calc():
    if request.method == 'POST':
        if request.form['starting-point'] != None and request.form['destination'] != None and request.form['mpg'] != None:
            dist = distance.getDistance(request.form['starting-point'], request.form['destination'])
            emission = emission_calc.calcFootprint(request.form['mpg'], dist)
            monthTravels = emission_calc.numTravelsInMonth(emission)
            yearTravels = emission_calc.numTravelsInYear(emission)

            data = [dist, emission, monthTravels, yearTravels]
            return data


@app.route("/hello")
def helo():
    return "hello me"

app.run()
#starting-point, destination, mpg
