#!/usr/bin/env python3
import urllib.request
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## put fileobject into helmet
helmet = groundctrl.read()
print(helmet)
hemmet1=json.loads(helmet)
print(hemmet1)
## decode JSON to Python data structure
helmetson = json.loads(helmet.decode('utf-8'))

## display our Pythonic data
print("\n\nConverted Python data")
print(helmetson)

print("\n\nPeople in Space: ", helmetson['number'])
count=int(helmetson['number'])
print(count)
for var in range(count):

    people = helmetson['people'][var]['name']
    print(f"People name is {people}")
people1=hemmet1['people']
print(people1)
print(people)
