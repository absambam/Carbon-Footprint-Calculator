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
    error=None # for error returns
    # if there's some sort of input from the website
    if request.method == 'POST':
        # check if any of the necessary variables are uninitialized
        if request.form['starting-point'] != None and request.form['destination'] != None and request.form['mpg'] != '0':

            # get the distance from the starting point to destination
            info = distance.getDistance(request.form['starting-point'], request.form['destination'])
            # make sure a valid distance was given before running calculations
            if info[2] == -1:
                return render_template('app.html', error=error)

            base_url = 'https://www.google.com/maps/dir/'
            url = base_url + info[0] + '/' + info[1]
            
            # calculate the necessary variables
            emission = emission_calc.calcFootprint(request.form['mpg'], info[2])
            yearTravels = emission_calc.numTravelsInYear(emission)
            trees = emission_calc.numTrees(emission)
            homes = emission_calc.numPerHomePerYear(emission)

            # store the calculated data in a tuple and return it to the end html file
            data = (emission, homes, trees, yearTravels, url)
            return render_template('test.html', data=data)

    # return error if there was an issue with any of the inputted values
    return render_template('app.html', error=error)

app.run() # this is pretty self-explanatory...
