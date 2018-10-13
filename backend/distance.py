import json
import urllib
import urllib2
import urllib3
import time

def getDistance(startLoc, endLoc):
    # startLoc and endloc can only take in full addresses

    # https://maps.googleapis.com/maps/api/distancematrix/json?origins=
    # Seattle&destinations=San+Francisco&key=INSERT_API_KEY
    # TODO: replace spaces with plus signs in startLoc and endLoc

    maps_key = 'AIzaSyBaDoxmA0conei-WUGZHS6moh7o_YphxCQ'
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    startLoc.replace(" ", "+")
    endLoc.replace(" ", "+")
    url = base_url + '?' + urllib.urlencode({
        'units' : 'imperial',
        'origins': startLoc,
        'destinations': endLoc,
        'key': maps_key,
    })

    current_delay = 0.1
    max_delay = 3600

    while True:
        try:
            response = str(urllib2.urlopen(url).read())
        except IOError:
            pass #Fall thru
        else:
            result = json.loads(response.replace('\\n', ''))
            if result['status']  == 'OK':
                return result['rows'][0]['elements'][0]['distance']['text']
            elif result['status'] != 'UNKNOWN_ERROR':
                raise Exception(result['error_message'])

        if current_delay > max_delay:
            raise Exception('Too many retry attempts. :(')
        print('Waiting', current_delay, 'seconds before retrying...')
        time.sleep(current_delay)
        current_delay *= 2

print(getDistance('UC San Diego', 'Vallartas San Diego'))
