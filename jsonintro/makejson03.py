#!/usr/bin/env python3
import json
def main():
    ## open the file
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    ## display our decoded string
    print(datacenterstring)
    print(type(datacenterstring))           
    print("\nThe code above is string data. Python cannot easily work with this data.")
  #  input("Press Enter to continue")            

    ## Create the JSON string
    datacenterdecoded = json.loads(datacenterstring)

    ## This is now a dictionary
    print(type(datacenterdecoded))

    ## display the servers in the datacenter
    print(datacenterdecoded)

    ## display the servers in row3
    print(datacenterdecoded["row3"])

    ## display the 2nd server in row2
    print(datacenterdecoded["row2"][1])

    ## write code to
    ## display the last server in row3


main()
