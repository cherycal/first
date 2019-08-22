__author__ = 'chance'

import sqldb
import tools
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

import push
inst = push.Push()

platform = tools.get_platform()
bdb = sqldb.DB('bdb.db')


league_dict = {}
team_dict = {}
old_rosters = {}
new_rosters = {}
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
msg = ""

c = bdb.select("SELECT * FROM Leagues")

for t in c:
    league_dict[t[0]] = t[1]

c = bdb.select("SELECT * FROM Rosters where LeagueID != 14047614")

for t in c:
    #print(t)
    old_rosters[t[0]+':'+t[1]] = t[1]
    team_dict[t[1]] = t[2]


c = bdb.delete("DELETE FROM Rosters")
c = bdb.select("SELECT * FROM Leagues where LeagueID != 14047614")

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
# if (platform == "Windows" ):
#     driver = webdriver.Chrome('C:/Users/chery/chromedriver.exe', chrome_options=options )
# elif (platform == "linux"):
#     driver = webdriver.Chrome( chrome_options=options)
# else:
#     print("Platform " + platform + " not recognized. Exiting.")
#     exit(-1)

driver = tools.get_driver()


for t in c:
    url = "http://fantasy.espn.com/baseball/league/rosters?leagueId=" + str(t[0])
    print (url)
    driver.get(url)
    time.sleep(12)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    sections = soup.find_all("section")
    for section in sections:
        section_row = section.find_all('span')
        names = section.find_all('span', {'class': 'teamName truncate'})
        for name in names:
            pass

        tables = section.find_all("table", {'class': 'Table2__table'})

        for table in tables:
            table_rows = table.find_all('tr')
            for tr in table_rows:
                title = tr.find('span')
                a = tr.find_all('a')
                row = [i.text for i in a]
                if (len(row)):
                    command = "INSERT INTO Rosters(Player, Team, LeagueID) VALUES ( \"" + row[0] + \
                              "\" ,\"" \
                                                                                       + \
                              name.text + "\"," + str(t[0]) + ")"
                    #print(command)
                    new_rosters[row[0]+':'+name.text] = name.text
                    bdb.insert(command)

c = bdb.select("SELECT count(Player) from Rosters")
players = c[0][0]
    
if (int(players) < 1145 ):
    print("Not enough players in Rosters: " + str(players))
    msg += "Not enough players in Rosters"
    inst.push("Roster error: "+str(date_time), msg)
    time.sleep(2)
    inst.push("Roster error: "+str(date_time), msg)
    time.sleep(2)
    inst.push("Roster error: "+str(date_time), msg)
else:
    print("Rosters appear to be full: " + str(players))
                    
for p in old_rosters:
    if new_rosters.get(p):
        if ( old_rosters[p] == new_rosters[p] ):
            #print(p, old_rosters[p], new_rosters[p] )
            pass
        else:
            #print("In old not in new: " + p, old_rosters[p], new_rosters[p] )
            msg += "DROPPED: " + p + ": " + old_rosters[p] + ", " + new_rosters[p]
            msg += "\n"
    else:
        #print("In old not in new: " + p)
        msg += "DROPPED: " + p
        msg += "\n"

for p in new_rosters:
    if ( old_rosters.get(p) ):
        pass
    else:
        #print("In new not in old: " + p, new_rosters[p])
        msg += "ADDED: " + p
        msg += "\n"

if (msg != ""):
    print("Msg: " + msg)
    inst.push("Roster changes: "+str(date_time), msg)
    time.sleep(2)
    inst.push("Roster changes: "+str(date_time), msg)
else:
    msg = "No changes"
    print("Msg: " + msg)
    inst.push("No changes: "+str(date_time), msg)


driver.quit()
bdb.close()

