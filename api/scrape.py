import requests
import time
import pprint
from bs4 import BeautifulSoup
import json
import difflib
from . import station_getter

def corrector(place):
    place=place.lower()
    correct=""
    for i in range(len(place)+1):
        if(place in station_getter.all_stations(place[:i])):
            correct=place
        else:
            try:
                correct=difflib.get_close_matches(place,station_getter.all_stations(place[:i]))[0]
            except:
                pass
    return correct


# print(station_getter.all_stations("trivandrum"))
def routes(starting_point,destination,timing):
    timing=difflib.get_close_matches(timing,["morning","afternoon","night","all"])
    
    starting_point=corrector(starting_point)       #Pass the corrected value from stations
    destination=corrector(destination)              #Pass the corrected value from stations
    timing=timing                          #Pass the corrected value from stations

    url="https://www.aanavandi.com/search/results/source/{}/destination/{}/timing/{}".format(starting_point,destination,timing)
    page=requests.get(url)


    soup=BeautifulSoup(page.content,'html.parser')
    schedules=soup.find_all('div',class_="col-md-6 col-sm-6 col-lg-6 col-xs-6 schedule")
    departure=soup.find_all('div',class_="col-md-3 col-sm-3 col-lg-3 col-xs-3 departure")
    arrivals=soup.find_all('div',class_="col-md-3 col-sm-3 col-lg-3 col-xs-3 arrival")
    result=[]
    for i in range(len(schedules)):
        result.append({"route":schedules[i].text,"departure":departure[i].text,"arrival":arrivals[i].text})
    return json.dumps(result)




