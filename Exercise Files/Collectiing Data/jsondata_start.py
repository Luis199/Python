import urllib.request
import json


def printResults(data):

    theJSON = json.loads(data)



def main():

    urlData = "https://earthquake.usgs.gov/earthquakes/map/?extent=9.1021,-144.22852&extent=59.31077,-45.79102"
    
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))


if __name__ == '__main__':
    main()