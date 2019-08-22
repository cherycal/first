__author__ = 'chance'

import urllib.request
import requests
import json

geourl = "http://statsapi.mlb.com/api/v1/teams"
#response = urllib.request.urlopen(geourl)

response = urllib.request.urlopen(geourl)

content = response.read()
data = json.loads(content.decode("utf8"))
teams = data['teams']

for team in teams:
    league = team['league']
    if (league.get('name')):
        league_name = league['name']
    if( league_name == 'American League' or league_name == 'National League'):
        print(team['id'])
        print(team['name'])
        print(team['link'])
        print(league_name)
        roster_link = team['link'] + '/roster/fullRoster?season=2019'
        print(roster_link)
        print("")

