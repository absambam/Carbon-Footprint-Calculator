import json
import urllib
import urllib2
import time
import extract_number

def getDistance(startLoc, endLoc):
    maps_key = ''
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json'

    # e.g.
    # https://maps.googleapis.com/maps/api/distancematrix/json?origins=
    # Seattle&destinations=San+Francisco&key=INSERT_API_KEY

    # Process strings with spaces by replacing spaces with +
    startLoc = startLoc.replace(" ", "+")
    endLoc = endLoc.replace(" ", "+")

    info = [startLoc, endLoc, 0]

    if (startLoc == endLoc):
        info[2] = -1
        return info

    url = base_url + '?' + urllib.urlencode({
        'units' : 'imperial',
        'origins': startLoc,
        'destinations': endLoc,
        'key': maps_key,
    })

    current_delay = 0.1 # Initial retry delay at 100ms
    max_delay = 3600 # Max retry delay at 1 hour

    while True:
        try:
            # Get API response
            response = str(urllib2.urlopen(url).read())
        except IOError:
            pass # Fall through to retry loop (next loop)
        else:
            # No IOError has occurred, so parse result
            result = json.loads(response.replace('\\n', ''))
            if result['status']  == 'OK':
                # Get distance value
                print(result['rows'][0]['elements'])
                info[2] = extract_number.extract_number(result['rows'][0]['elements'][0]['distance']['text'])
                # dist = result['rows'][0]['elements'][0]['distance']['text']

                # Check if there is no distance
                if info[2] == 0:
                    info[2] = -1

                return info
            elif result['status'] != 'UNKNOWN_ERROR':
                # Error cannot be fixed by retrying
                raise Exception(result['error_message'])
                info[2] = -1
                return info

        # Check if current retry delay has exceeded max retry delay
        if current_delay > max_delay:
            raise Exception('Too many retry attempts. :(')
            info[2] = -1
            return info
        print('Waiting', current_delay, 'seconds before retrying...')
        time.sleep(current_delay)
        current_delay *= 2 # Increase delay each time we need to retry

# Test call
print(getDistance('UC San Diego', 'Vallartas San Diego'))
