import requests
import json

#returns a dict of all champion information required.
def getChampInfo():
    url = "http://ddragon.leagueoflegends.com/cdn/10.15.1/data/en_US/champion.json"

    urlBefore = "http://ddragon.leagueoflegends.com/cdn/10.15.1/data/en_US/champion/"
    urlAfter = ".json"

    #get basic champion names
    response = requests.get(url)
    data = json.loads(response.content)

    #get detailed champion info
    championInfo = {}
    requiredAttributes=["id","key","name","title","lore","allytips","enemytips","tags"]

    #for each champion
    for champName in data["data"]:
        #get the champion's info
        championInfo[champName]={}
        response = requests.get(urlBefore+champName+urlAfter)
        champData = json.loads(response.content)
        champData=champData['data'][champName]

        #copy over the parts we want into championInfo[champName]
        for attribute in requiredAttributes:
            if type(champData[attribute]) is list:
                for ind, subattribute in enumerate(champData[attribute]):
                    championInfo[champName][attribute+str(ind)]=subattribute
            else:
                championInfo[champName][attribute]=champData[attribute]
    return championInfo



# test=open('text.txt','w')
# test.write(str(championInfo))

