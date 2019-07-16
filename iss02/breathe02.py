#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI ='http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=94555&date=2019-01-21&distance=25&API_KEY=7B5521E8-24DA-4619-821C-A1AF3585FC17' 

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    # display the JSON we were returned as Pythonic datastructures
    print(r.json())

main()
