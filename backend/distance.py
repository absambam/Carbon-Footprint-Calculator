import json
import urllib
import urllib2
import time

def getDistance(startLoc, endLoc):
    # startLoc and endloc can only take in full addresses

    # https://maps.googleapis.com/maps/api/distancematrix/json?origins=
    # Seattle&destinations=San+Francisco&key=INSERT_API_KEY
    maps_key = 'AIzaSyBaDoxmA0conei-WUGZHS6moh7o_YphxCQ'
