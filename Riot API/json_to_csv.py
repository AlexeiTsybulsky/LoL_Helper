import json

def processChampionInformation():
    f = open('mydata\\csv\\json\\champions.json', encoding="utf8")
    data=json.load(f)
    f.close()

    f = open('mydata\\csv\\champions.txt','w')

    elems=['id','key','name','title','lore','allytips0','allytips1','allytips2','allytips3','allytips4','enemytips0','enemytips1','enemytips2','enemytips3','enemytips4','tags0','tags1']

    mystring=""

    #header
    mystring="\"{}\"".format(elems[0])
    for e in elems[1:]:
        if type(e) is str:
            mystring = "{}|\"{}\"".format(mystring,e)

    mystring += "\n"
    f.write(mystring)

    # not header
    for key in data:
        mystring=""
        for e in elems:
            if e in data[key]:
                mystring = "{}|{}".format(mystring,data[key][e])
            else:
                mystring = "{}|".format(mystring)
        mystring += "\n"
        f.write(mystring[1:])

    f.close()


def processItemBuildsInfo():
    f = open('mydata\\csv\\json\\item_builds_into.json', encoding="utf8")
    data=json.load(f)
    f.close()

    f = open('mydata\\csv\\item_builds_into.txt','w')

    elems=['item','into']

    mystring=""

    #header
    mystring="\"{}\"".format(elems[0])
    for e in elems[1:]:
        if type(e) is str:
            mystring = "{}|\"{}\"".format(mystring,e)

    mystring += "\n"
    f.write(mystring)

    # not header
    for key in data:
        for col2 in data[key]:
            mystring="{}|{}\n".format(key,col2)
            f.write(mystring)

    f.close()


def processItems():
    f = open('mydata\\csv\\json\\items.json', encoding="utf8")
    data=json.load(f)
    f.close()

    f = open('mydata\\csv\\items.txt','w')

    elems=['name','plaintext']

    mystring=""

    #header
    mystring="\"itemId\""
    for e in elems:
        if type(e) is str:
            mystring = "{}|\"{}\"".format(mystring,e)

    mystring += "\n"
    f.write(mystring)

    # not header
    for key in data:
        mystring=",\"{}\"".format(key)
        for e in elems:
            if e in data[key]:
                mystring = "{}|{}".format(mystring,data[key][e])
            else:
                mystring = "{}|".format(mystring)
        mystring += "\n"
        f.write(mystring[1:])

    f.close()


def processPlayers():

    output = open('mydata\\csv\\players.txt','w',encoding="utf8")

    elems=['puuid','accountId','summonerId','region','tier','summonerName','leaguePoints','rank','wins','losses','veteran','inactive','freshBlood','hotStreak','profileIconId','revisionDate','summonerLevel']

    mystring=""

    #header
    mystring="\"{}\"".format(elems[0])
    for e in elems[1:]:
        if type(e) is str:
            mystring = "{}|\"{}\"".format(mystring,e)
    mystring += "\n"
    output.write(mystring)


    # not header
    regions=['na1','kr','eun1','euw1']
    queues=['challenger','grandmaster','master']

    for r in regions:
        for q in queues:

            f = open('mydata\\summoners\\{}_{}leagues_output.txt'.format(r,q), encoding="utf8")
            data=json.load(f)
            f.close()

            for summoner in data['summoners']:
                mystring=""
                for e in elems:
                    if e in summoner:
                        mystring = "{}|{}".format(mystring,summoner[e])
                    elif e == 'region':
                        mystring = "{}|{}".format(mystring,r)
                    elif e == 'tier':
                        mystring = "{}|{}".format(mystring,q)
                    else:
                        mystring = "{}|".format(mystring)
                mystring += "\n"
                output.write(mystring[1:])

    output.close()


def processMatches():

    output = open('mydata\\csv\\matches.txt','w',encoding="utf8")

    elems=['gameId','platformId','gameCreation','gameDuration','queueId','mapId','seasonId','gameVersion','gameMode','gameType']

    mystring=""

    #header
    mystring="\"{}\"".format(elems[0])
    for e in elems[1:]:
        if type(e) is str:
            mystring = "{}|\"{}\"".format(mystring,e)
    mystring += "\n"
    output.write(mystring)


    # not header
    regions=['na1','kr','euw1']
    numfiles=10

    for r in regions:
        for n in range(numfiles):

            f = open('mydata\\matchId_To_MatchData\\{}_matchId_To_MatchData_output_{}.txt'.format(r,n), encoding="utf8")
            data=json.load(f)
            f.close()

            for key in data[r]:
                if not 'status' in data[r][key]:
                    mystring=""
                    for e in elems:
                        if e in data[r][key]:
                            mystring = "{}|{}".format(mystring,data[r][key][e])
                        else:
                            mystring = "{}|".format(mystring)
                    mystring += "\n"
                    output.write(mystring[1:])

    output.close()
    print("done!")


def processMatchTeamDetails():

    output = open('mydata\\csv\\match_team_details.txt','w',encoding="utf8")

    elems=['gameId','platformId','teamId','win','firstBlood','firstTower','firstInhibitor','firstBaron','firstDragon','firstRiftHerald','towerKills','inhibitorKills','baronKills','dragonKills','vilemawKills','riftHeraldKills','dominionVictoryScore','banChampionId1','banChampionId2','banChampionId3','banChampionId4','banChampionId5']
    bans=['banChampionId1','banChampionId2','banChampionId3','banChampionId4','banChampionId5']

    mystring=""

    #header
    mystring="\"{}\"".format(elems[0])
    for e in elems[1:]:
        if type(e) is str:
            mystring = "{}|\"{}\"".format(mystring,e)
    mystring += "\n"
    output.write(mystring)


    # not header
    regions=['na1','kr','euw1']
    numfiles=10

    for r in regions:
        for n in range(numfiles):

            f = open('mydata\\matchId_To_MatchData\\{}_matchId_To_MatchData_output_{}.txt'.format(r,n), encoding="utf8")
            data=json.load(f)
            f.close()

            for key in data[r]:
                if not 'status' in data[r][key]:
                    for team in data[r][key]['teams']:
                        mystring=""
                        for e in elems:
                            if e in team:
                                mystring = "{}|{}".format(mystring,team[e])
                            elif e == 'gameId':
                                mystring = "{}|{}".format(mystring,data[r][key]['gameId'])
                            elif e == 'platformId':
                                mystring = "{}|{}".format(mystring,data[r][key]['platformId'])
                            elif e in bans:
                                tempChampId=0
                                for ban in team['bans']:
                                    if ban['pickTurn']==int(e[-1]):
                                        tempChampId=ban['championId']
                                mystring = "{}|{}".format(mystring,tempChampId)
                            else:
                                mystring = "{}|".format(mystring)
                        mystring += "\n"
                        output.write(mystring[1:])

    output.close()
    print("done!")


def processMatchParticipantDetails():

    output = open('mydata\\csv\\matches_participant_details.txt','w',encoding="utf8")

    elems=['gameId','platformId','participantId','summonerId','teamId','championId','spell1Id','spell2Id','win','item0','item1','item2','item3','item4','item5','item6','kills','deaths','assists','largestKillingSpree','largestMultiKill','killingSprees','longestTimeSpentLiving','doubleKills','tripleKills','quadraKills','pentaKills','unrealKills','totalDamageDealt','magicDamageDealt','physicalDamageDealt','trueDamageDealt','largestCriticalStrike','totalDamageDealtToChampions','magicDamageDealtToChampions','physicalDamageDealtToChampions','trueDamageDealtToChampions','totalHeal','totalUnitsHealed','damageSelfMitigated','damageDealtToObjectives','damageDealtToTurrets','visionScore','timeCCingOthers','totalDamageTaken','magicalDamageTaken','physicalDamageTaken','trueDamageTaken','goldEarned','goldSpent','turretKills','inhibitorKills','totalMinionsKilled','neutralMinionsKilled','neutralMinionsKilledTeamJungle','neutralMinionsKilledEnemyJungle','totalTimeCrowdControlDealt','champLevel','visionWardsBoughtInGame','sightWardsBoughtInGame','wardsPlaced','wardsKilled','firstBloodKill','firstBloodAssist','firstTowerKill','firstTowerAssist','firstInhibitorKill','firstInhibitorAssist','role','lane']
    stats=['win','item0','item1','item2','item3','item4','item5','item6','kills','deaths','assists','largestKillingSpree','largestMultiKill','killingSprees','longestTimeSpentLiving','doubleKills','tripleKills','quadraKills','pentaKills','unrealKills','totalDamageDealt','magicDamageDealt','physicalDamageDealt','trueDamageDealt','largestCriticalStrike','totalDamageDealtToChampions','magicDamageDealtToChampions','physicalDamageDealtToChampions','trueDamageDealtToChampions','totalHeal','totalUnitsHealed','damageSelfMitigated','damageDealtToObjectives','damageDealtToTurrets','visionScore','timeCCingOthers','totalDamageTaken','magicalDamageTaken','physicalDamageTaken','trueDamageTaken','goldEarned','goldSpent','turretKills','inhibitorKills','totalMinionsKilled','neutralMinionsKilled','neutralMinionsKilledTeamJungle','neutralMinionsKilledEnemyJungle','totalTimeCrowdControlDealt','champLevel','visionWardsBoughtInGame','sightWardsBoughtInGame','wardsPlaced','wardsKilled','firstBloodKill','firstBloodAssist','firstTowerKill','firstTowerAssist','firstInhibitorKill','firstInhibitorAssist']
    rolelane=['role','lane']

    mystring=""

    #header
    mystring="\"{}\"".format(elems[0])
    for e in elems[1:]:
        if type(e) is str:
            mystring = "{}|\"{}\"".format(mystring,e)
    mystring += "\n"
    output.write(mystring)


    # not header
    regions=['na1','kr','euw1']
    numfiles=10

    for r in regions:
        for n in range(numfiles):

            f = open('mydata\\matchId_To_MatchData\\{}_matchId_To_MatchData_output_{}.txt'.format(r,n), encoding="utf8")
            data=json.load(f)
            f.close()

            for key in data[r]:
                if not 'status' in data[r][key]:
                    for p in data[r][key]['participants']:
                        mystring=""
                        for e in elems:
                            try:
                                if e in p:
                                    mystring = "{}|{}".format(mystring,p[e])
                                elif e == 'gameId':
                                    mystring = "{}|{}".format(mystring,data[r][key]['gameId'])
                                elif e == 'platformId':
                                    mystring = "{}|{}".format(mystring,data[r][key]['platformId'])
                                elif e == 'summonerId':
                                    mystring = "{}|{}".format(mystring,data[r][key]['participantIdentities'][p['participantId']-1]['player']['summonerId'])
                                elif e in stats:
                                    mystring = "{}|{}".format(mystring,p['stats'][e])
                                elif e in rolelane:
                                    mystring = "{}|{}".format(mystring,p['timeline'][e])
                                else:
                                    mystring = "{}|".format(mystring)
                            except:
                                mystring = "{}|".format(mystring)

                        mystring += "\n"
                        output.write(mystring[1:])

    output.close()
    print("done!")


def processMatchParticipantTimelineDetails():

    output = open('mydata\\csv\\match_participant_timeline_details.txt','w',encoding="utf8")

    elems=['gameId','platformId','participantId','deltaId','creepsPerMinDeltas','xpPerMinDeltas','goldPerMinDeltas','damageTakenPerMinDeltas']
    donothing=['creepsPerMinDeltas','xpPerMinDeltas','goldPerMinDeltas','damageTakenPerMinDeltas']
    deltaIds=["0-10","10-20","20-30","30-end"]

    mystring=""

    #header
    mystring="\"{}\"".format(elems[0])
    for e in elems[1:]:
        if type(e) is str:
            mystring = "{}|\"{}\"".format(mystring,e)
    mystring += "\n"
    output.write(mystring)


    # not header
    regions=['na1','kr','euw1']
    numfiles=10

    for r in regions:
        for n in range(numfiles):

            f = open('mydata\\matchId_To_MatchData\\{}_matchId_To_MatchData_output_{}.txt'.format(r,n), encoding="utf8")
            data=json.load(f)
            f.close()

            for key in data[r]:
                if not 'status' in data[r][key]:
                    for p in data[r][key]['participants']:
                        mystring=""
                        for e in elems:
                            try:
                                if e == 'gameId':
                                    mystring = "{}|{}".format(mystring,data[r][key]['gameId'])
                                elif e == 'platformId':
                                    mystring = "{}|{}".format(mystring,data[r][key]['platformId'])
                                elif e == 'participantId':
                                    mystring = "{}|{}".format(mystring,p['participantId'])
                                elif e == 'deltaId':
                                    for d in deltaIds:
                                        stringcopy = mystring
                                        if d in p['timeline'][donothing[0]]:
                                            stringcopy = "{}|{}".format(stringcopy,d)
                                            for stat in donothing:
                                                if d in p['timeline'][stat]:
                                                    stringcopy = "{}|{}".format(stringcopy,p['timeline'][stat][d])
                                                else:
                                                    stringcopy = "{}|".format(stringcopy)
                                            stringcopy += "\n"
                                            output.write(stringcopy[1:])
                                elif e in donothing:
                                    pass
                                else:
                                    mystring = "{}|".format(mystring)
                            except:
                                mystring = "{}|".format(mystring)


    output.close()
    print("done!")




# i ran these

# processChampionInformation()
# processItemBuildsInfo()
# processItems()
# processPlayers()
# processMatches()
# processMatchTeamDetails()
processMatchParticipantDetails()
# processMatchParticipantTimelineDetails()