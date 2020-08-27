from django.db import models

class Player(models.Model):
    puuid = models.CharField(primary_key=True, max_length=78)
    accountid = models.CharField(max_length=56, blank=True, null=True)
    summonerid = models.CharField(max_length=48, blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    tier = models.TextField(blank=True, null=True)
    summonername = models.TextField(blank=True, null=True)
    leaguepoints = models.IntegerField(blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    veteran = models.BooleanField(blank=True, null=True)
    inactive = models.BooleanField(blank=True, null=True)
    freshblood = models.BooleanField(blank=True, null=True)
    hotstreak = models.BooleanField(blank=True, null=True)
    profileiconid = models.IntegerField(blank=True, null=True)
    revisiondate = models.CharField(max_length=13, blank=True, null=True)
    summonerlevel = models.IntegerField(blank=True, null=True)

    class Meta:
       managed = False
       db_table = 'players'