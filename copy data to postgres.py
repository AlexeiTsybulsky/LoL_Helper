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
    CREATE TABLE players(

    puuid varchar(78) PRIMARY KEY,
    accountId varchar(56),
    summonerId varchar(48),
    region text,
    tier text,
    summonerName text,
    leaguePoints integer,
    rank text,
    wins integer,
    losses integer,
    veteran boolean,
    inactive boolean,
    freshBlood boolean,
    hotStreak boolean,
    profileIconId integer,
    revisionDate varchar(13),
    summonerLevel integer

)
""")

conn.commit()

with open('data/players.csv', 'r', encoding='utf-8') as f:
    next(f) # Skip the header row
    cur.copy_from(f, 'players', sep='|')

conn.commit()