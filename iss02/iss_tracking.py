import turtle
import urllib.request
import json
## Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## JSON 2 Python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our Pythonic data
print("\n\nConverted Python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')    

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)
screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set the resolution
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('iss_map.gif')
