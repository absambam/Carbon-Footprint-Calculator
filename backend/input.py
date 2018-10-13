#!/usr/bin/env python
import os
import emission_calc

headers = ["Content-type: text/html"]
qs = os.environ['QUERY_STRING']

def sendHeaders():
    for h in headers:
        print h
    print "\n"

def sendForm():
    print '''
    <html>
      <body>
          <form action='backend/emission_calc.py' method='calculateFootprint'>
              <label for="mpg">Enter Your Vehicle's MPG</label>
              <input id="mpg" type="number" name="mpg" value="0" />
              <input type="submit">
          </form>
      </body>
    </html>
    '''

def sendPage(emission, in_month, in_year):
    print '''
    <html>
      <body>
        <h1>Your carbon emissions for this trip total to {0} pounds of CO2</h1>
        <h1>If you travelled to this place {1} times in a month, you would hit the average monthly CO2 emissions per person in the United States.</h1>
        <h1>If you travelled to this place {2} times in a year, you would the average annual CO2 emissions per person in the United States.</h1>
      </body>
    </html>
    '''.format(emission, in_month, in_year)

if not qs:
    sendHeaders()
    sendForm()
else:
    if 'mpg' in qs:
        mpg = qs.split('=')[1]
    else:
        mpg = 'No Name Provided'
    sendHeaders()
    emission = emission_calc.calcFootprint(mpg, mpg)
    in_year = emission_calc.numTravelsInYear(emission)
    in_month = emission_calc.numTravelsInMonth(emission)
    sendPage(emission, in_month, in_year)