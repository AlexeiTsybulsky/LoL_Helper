import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
cur = conn.cursor()


cur.execute("""
    CREATE TABLE champions(

    id text,
    key smallint PRIMARY KEY,
    name text,
    title text,
    lore text,
    allytips0 text,
    allytips1 text,
    allytips2 text,
    allytips3 text,
    allytips4 text,
    enemytips0 text,
    enemytips1 text,
    enemytips2 text,
    enemytips3 text,
    enemytips4 text,
    tags0 text,
    tags1 text

)
""")

conn.commit()

print("created champions table")

with open('data/champions.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'champions', sep='|')

conn.commit()

print("populated champions table")


cur.execute("""
    CREATE TABLE items(

    itemId smallint PRIMARY KEY,
    name text,
    description text

)
""")

conn.commit()

print("created items table")

with open('data/items.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'items', sep='|')

conn.commit()

print("populated items table")


cur.execute("""
    CREATE TABLE item_builds_into(

    item smallint,
    builds_into smallint

)
""")

conn.commit()

print("created item builds into table")

with open('data/item_builds_into.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'item_builds_into', sep='|')

conn.commit()

print("populated item builds into table")


cur.execute("""
    CREATE TABLE players(

    puuid text PRIMARY KEY,
    accountId text,
    summonerId text,
    region text,
    tier text,
    summonerName text,
    leaguePoints smallint,
    rank text,
    wins smallint,
    losses smallint,
    veteran boolean,
    inactive boolean,
    freshBlood boolean,
    hotStreak boolean,
    profileIconId smallint,
    revisionDate bigint,
    summonerLevel smallint

)
""")

conn.commit()

print("created players table")

with open('data/players.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'players', sep='|')

conn.commit()

print("populated players table")


cur.execute("""
    CREATE TABLE matches(

    gameId bigint PRIMARY KEY,
    platformId text,
    gameCreation bigint,
    gameDuration smallint,
    queueId smallint,
    mapId smallint,
    seasonId smallint,
    gameVersion text,
    gameMode text,
    gameType text

)
""")

conn.commit()

print("created matches table")

with open('data/matches.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'matches', sep=',')

conn.commit()

print("populated matches table")


cur.execute("""
    CREATE TABLE match_team_details(

    gameId bigint,
    platformId text,
    teamId smallint,
    win text,
    firstBlood boolean,
    firstTower boolean,
    firstInhibitor boolean,
    firstBaron boolean,
    firstDragon boolean,
    firstRiftHerald boolean,
    towerKills smallint,
    inhibitorKills smallint,
    baronKills smallint,
    dragonKills smallint,
    vilemawKills smallint,
    riftHeraldKills smallint,
    dominionVictoryScore smallint,
    banChampionId1 smallint,
    banChampionId2 smallint,
    banChampionId3 smallint,
    banChampionId4 smallint,
    banChampionId5 smallint

)
""")

conn.commit()

print("created match team details table")

with open('data/match_team_details.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'match_team_details', sep=',')

conn.commit()

print("populated match team details table")


cur.execute("""
    CREATE TABLE match_participant_details(

    gameId bigint,
    platformId text,
    participantId smallint,
    teamId smallint,
    championId smallint,
    spell1Id smallint,
    spell2Id smallint,
    win boolean,
    item0 smallint,
    item1 smallint,
    item2 smallint,
    item3 smallint,
    item4 smallint,
    item5 smallint,
    item6 smallint,
    kills smallint,
    deaths smallint,
    assists smallint,
    largestKillingSpree smallint,
    largestMultiKill smallint,
    killingSprees smallint,
    longestTimeSpentLiving smallint,
    doubleKills smallint,
    tripleKills smallint,
    quadraKills smallint,
    pentaKills smallint,
    unrealKills smallint,
    totalDamageDealt integer,
    magicDamageDealt integer,
    physicalDamageDealt integer,
    trueDamageDealt integer,
    largestCriticalStrike integer,
    totalDamageDealtToChampions integer,
    magicDamageDealtToChampions integer,
    physicalDamageDealtToChampions integer,
    trueDamageDealtToChampions integer,
    totalHeal integer,
    totalUnitsHealed integer,
    damageSelfMitigated integer,
    damageDealtToObjectives integer,
    damageDealtToTurrets integer,
    visionScore smallint,
    timeCCingOthers smallint,
    totalDamageTaken integer,
    magicalDamageTaken integer,
    physicalDamageTaken integer,
    trueDamageTaken integer,
    goldEarned integer,
    goldSpent integer,
    turretKills smallint,
    inhibitorKills smallint,
    totalMinionsKilled smallint,
    neutralMinionsKilled smallint,
    neutralMinionsKilledTeamJungle smallint,
    neutralMinionsKilledEnemyJungle smallint,
    totalTimeCrowdControlDealt smallint,
    champLevel smallint,
    visionWardsBoughtInGame smallint,
    sightWardsBoughtInGame smallint,
    wardsPlaced smallint,
    wardsKilled smallint,
    firstBloodKill boolean,
    firstBloodAssist boolean,
    firstTowerKill boolean,
    firstTowerAssist boolean,
    firstInhibitorKill boolean,
    firstInhibitorAssist boolean,
    role text,
    lane text

)
""")

conn.commit()

print("created match participant details table")

with open('data/match_participant_details.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'match_participant_details', sep=',', null='None')

conn.commit()

print("populated match participant details table")


cur.execute("""
    CREATE TABLE match_participant_timeline_details(

    gameId bigint,
    platformId text,
    participantId smallint,
    deltaId text,
    creepsPerMinDeltas real,
    xpPerMinDeltas real,
    goldPerMinDeltas real,
    damageTakenPerMinDeltas real

)
""")

conn.commit()

print("created match participant timeline details table")

with open('data/match_participant_timeline_details.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'match_participant_timeline_details', sep=',')

conn.commit()

print("populated match participant timeline details table")