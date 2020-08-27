import os
from dotenv import load_dotenv
import time
import requests
import json

load_dotenv()

apikey=os.getenv("RIOT_API_KEY")

# RATE LIMITS
# 20 requests every 1 seconds(s)
# 100 requests every 2 minutes(s) (120 seconds)
rateLimits = {1:20, 120:100}
rateQueues = {1:[], 120:[]}

# manages api calls to make sure rate limits are not surpassed
def apiCallManager(requestUrl):
    # both limits are not reached
    if len(rateQueues[1]) < rateLimits[1] and len(rateQueues[120]) < rateLimits[120]:

        #make api call here
        response = requests.get(requestUrl)
        retval = json.loads(response.content)

        addtime=time.time()

        # add the expiry time to all queues
        # added an extra second because when used a lot we still get {'status': {'message': 'Rate limit exceeded', 'status_code': 429}}
        rateQueues[1].append(addtime+1+1)
        rateQueues[120].append(addtime+120+1)
    
    # at least one limit is reached
    else:
        # remove expired times
        # not in any way optimized and quite inefficient.
        minWaitTime = 0
        temptime = time.time()

        for key in rateQueues:
            #nonempty check
            if len(rateQueues[key]) >= rateLimits[key]:
                if temptime < rateQueues[key][0]:
                    #remove nothing
                    #minimum required to wait is at least rateQueues[key][0]-temptime
                    minWaitTime = max(minWaitTime, rateQueues[key][0]-temptime)

                elif temptime > rateQueues[key][-1]: 
                    #remove everything
                    #no required time to wait
                    rateQueues[key].clear()

                else:
                    #at this point temptime lies somewhere in the queue
                    #no requred time to wait
                    ind = 0
                    while (len(rateQueues[key])>ind and temptime>rateQueues[key][ind]):
                        ind+=1
                    rateQueues[key]=rateQueues[key][ind:]

        #wait to make the next url request and make it.
        #sleeping for another extra second because idk what is going on

        if minWaitTime:
            print('sleeping for ',minWaitTime+1,'seconds.')
            time.sleep(minWaitTime+1)

        #make api request here
        response = requests.get(requestUrl)
        if response.status_code == 200:
            retval = json.loads(response.content)
        else:
            retval = Exception(json.loads(response.content))

        addtime=time.time()
        for key in rateQueues:
            rateQueues[key].append(addtime+key)

    return retval

#testing 1  and 2 - if limit rate works
def test1():
    for a in range(110):
        print(apiCallManager(''))
        print('1: ',len(rateQueues[1]),'; 120: ',len(rateQueues[120]),' ',a)

    print(rateQueues)

def test2(): 
    for a in range(1000):
        print(apiCallManager('poo.com'))
        print('1: ',len(rateQueues[1]),'; 120: ',len(rateQueues[120]),' ',a)
    print(rateQueues)

####################################################################
#this section to get players in master, grandmaster, and challenger#
####################################################################
def getPlayers():
    retval={}
    regions=['na1','kr','eun1','euw1']
    queues=['challengerleagues','grandmasterleagues','masterleagues']
    for r in regions:
        retval[r]={}
        for q in queues:
            retval[r][q]=apiCallManager('https://{}.api.riotgames.com/lol/league/v4/{}/by-queue/RANKED_SOLO_5x5?api_key={}'.format(r,q,apikey))
    return retval
    
# run once and rename to masterAndUpPlayers.txt
# myfile=open('output.txt','w')
# myfile.write(json.dumps(getPlayers()))

#idk why im exceeding rate limit but every time it does put it in here

#need 'accountId'. we can get it from summoner-v4 using the summonerId. we can add the other information as well.
def addSummonnerInfo(r,q):
    print('starting {} {}.'.format(r,q))

    #get the info from previous step
    myfile=open('masterAndUpPlayers.txt')
    summonerInfo=json.load(myfile)
    myfile.close()

    #take only whats needed
    summonerInfo=summonerInfo[r][q]['entries']

    keylist=['accountId','puuid','profileIconId','revisionDate','summonerLevel']

    for summoner in summonerInfo:
        while(True):
            try:
                response=apiCallManager('https://{}.api.riotgames.com/lol/summoner/v4/summoners/{}?api_key={}'.format(r,summoner['summonerId'],apikey))
                for key in keylist:
                    summoner[key]=response[key]
                break
            except:
                print(str(response))
                    
    summonerInfo={"summoners":summonerInfo}

    myfile=open('{}_{}_output.txt'.format(r,q),'w')
    myfile.write(json.dumps(summonerInfo))

    print('done {} {}.'.format(r,q))

#i became a distributed system. rate limiting is by region
def runAddSummonnerInfo(region):
    queues=['challengerleagues','grandmasterleagues','masterleagues']
    for q in queues:
        addSummonnerInfo(region, q)

# runAddSummonnerInfo('na1')
# runAddSummonnerInfo('kr')
# runAddSummonnerInfo('eun1')
# runAddSummonnerInfo('euw1')

#make an empty dict of "accountId"s per region per queue
def accountIdToMatches(region):
    # regions=['na1','kr','eun1','euw1']
    queues=['challengerleagues','grandmasterleagues','masterleagues']

    retval={region:{}}

    # preparing empty dict nicely structured
    print('accountIdToMatches starting {} prep.'.format(region))

    for q in queues:
        retval[region][q]={}

        f = open('mydata\\{}_{}_output.txt'.format(region,q))
        summonerInfo=json.load(f)
        f.close()

        for summoner in summonerInfo['summoners']:
            retval[region][q][summoner['accountId']]={}
    
    for q in queues:
        print('starting {} {}.'.format(region, q))
        for summoner in retval[region][q]:
            while(True):
                try:
                    response=apiCallManager('https://{}.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?queue=420&api_key={}'.format(region,summoner,apikey))
                    
                    if type(response) is Exception:
                        raise response

                    retval[region][q][summoner]['matches']=response['matches']
                    break
                except:
                    print(str(response))

    myfile=open('{}_matches_output.txt'.format(region),'w')
    myfile.write(json.dumps(retval))

#again, i am a distributed system (api call limits separate between regions)
# accountIdToMatches('na1')
# accountIdToMatches('kr')
# accountIdToMatches('eun1')
# accountIdToMatches('euw1')

#making a dict of all the matches
# so it turns out that this part is absolutely huge, to the point that we get a memory error if we
# try to fit everythiing into one dict, so we need to separate into separate files. (1000/file)
# also if we tried to do every match in the accountIdtoMatches we would have to do at least 30k+
# api calls per server. so we will just do 10k games per server which seems like a good size.
# also something seems wack with the eun1 so we will just avoid that one.
def matchIdToMatchData(region):
    # regions=['na1','kr','eun1','euw1']
    queues=['challengerleagues','grandmasterleagues','masterleagues']

    gameIdList = []
    retval = {region: {}}

    # preparing empty dict nicely structured
    print('matchIdToMatchData starting {}.'.format(region))

    f = open('mydata\\{}_matches_output.txt'.format(region))
    matchesByAccount=json.load(f)
    f.close()

    #make list of keys being 'gameId's
    print('retriving {} gameIds.'.format(region))
    for q in queues:
        for accountId in matchesByAccount[region][q]:
            for match in matchesByAccount[region][q][accountId]['matches']:
                gameIdList.append(match['gameId'])

    #list cleanup
    gameIdList = list(dict.fromkeys(gameIdList))
    gameIdList.sort(reverse=True)

    print('getting {} matchdata.'.format(region))
    #get matchdata for each game
    
    totalMatches=10000
    matchInd=5000
    matchesPerFile=1000
    fileNum=5

    while matchInd<totalMatches:
        for counter in range(matchesPerFile):
            if matchInd>=totalMatches:
                break
            
            while(True):
                try:
                    response=apiCallManager('https://{}.api.riotgames.com/lol/match/v4/matches/{}?api_key={}'.format(region,gameIdList[fileNum+counter],apikey))

                    # for some reason it still puts exceptions into retval and just moves on??
                    if type(response) is Exception:
                        raise response
                    else:
                        retval[region][gameIdList[fileNum+counter]]=response
                        matchInd+=1
                        break
                except:
                    print('error: {}.'.format(response))

        
        myfile=open('{}_matchId_To_MatchData_output_{}.txt'.format(region,fileNum),'w')
        myfile.write(json.dumps(retval))
        myfile.close()
        retval = {region: {}}
        fileNum+=1

    # old code
    # for gameId in retval[region]:
    #     while(True):
    #         try:
    #             response=apiCallManager('https://{}.api.riotgames.com/lol/match/v4/matches/{}?api_key={}'.format(region,gameId,apikey))

    #             if type(response) is Exception:
    #                 raise response

    #             retval[region][gameId]=response
    #             break
    #         except:
    #             print(response)
    # myfile=open('{}_matchId_To_MatchData_output.txt'.format(region),'w')
    # myfile.write(json.dumps(retval))



# matchIdToMatchData('na1')
# matchIdToMatchData('kr')
matchIdToMatchData('euw1')


####################
#stuff i need to do#
####################

#1 for each summoner, use
#matchlist='https://{}.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?api_key={}'.format(r,accountId,apikey)
#to get the matchlist for each 
