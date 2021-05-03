import requests
import json
import string


def all_stations(term):
    url="https://www.aanavandi.com/search/autocompleteTest?term={}"
    allstations=[]
    resp=json.loads(requests.get(url.format(term)).content)
    for i in resp:
        allstations.append(i["value"].lower())
    return allstations





