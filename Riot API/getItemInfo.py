import requests
import json

#returns a dict of all champion information required.
def getItemInfo():
    url = "http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/item.json"

    #get item info
    response = requests.get(url)
    data = json.loads(response.content)

    requiredAttributes=["name","plaintext"]

    retval={}

    for itemId in data['data']:
        retval[itemId]={}
        for attribute in requiredAttributes:
            retval[itemId][attribute]=data['data'][itemId][attribute]

    return retval

def itemBuildsInto():
    url = "http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/item.json"

    #get item info
    response = requests.get(url)
    data = json.loads(response.content)

    retval={}

    for itemId in data['data']:
        if 'into' in data['data'][itemId]:
            retval[itemId]=data['data'][itemId]['into']

    return retval



f=open('items_builds_into.txt','w')
f.write(json.dumps(itemBuildsInto()))
