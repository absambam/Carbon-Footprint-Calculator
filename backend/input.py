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

def sendPage(emission):
    print '''
    <html>
      <body>
        <h1>Your carbon emissions for this trip total to {0} pounds of CO2</h1>
        <h1></h1>
        <h1></h1>
      </body>
    </html>
    '''.format(emission)

if not qs:
    sendHeaders()
    sendForm()
else:
    if 'mpg' in qs:
        mpg = qs.split('=')[1]
    else:
        mpg = 'No Name Provided'
    sendHeaders()
    sendPage(mpg)