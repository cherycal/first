__author__ = 'chance'

from bs4 import BeautifulSoup
from selenium import webdriver


import requests
import time
import push
inst = push.Push()
#driver = webdriver.Firefox(executable_path = 'C:/Users/chery/geckodriver.exe')

# "http://fantasy.espn.com/baseball/league?leagueId=162788"
# "http://fantasy.espn.com/baseball/team?leagueId=6455&seasonId=2019&teamId=2&fromTeamId=2"
# http://fantasy.espn.com/baseball/recentactivity?leagueId=162788
o_pts = new_o_pts = 0
sleep_interval = 2

url = "http://fantasy.espn.com/baseball/team?leagueId=162788&seasonId=2019&teamId=4&fromTeamId=4"

driver = webdriver.Chrome('C:/Users/chery/chromedriver.exe')
driver.get(url)
time.sleep(7)


while(1):
    print("Check: " + str(o_pts))
    html = driver.page_source
    soup = BeautifulSoup(html,"lxml")
    my_data = soup.find_all("span", {"class": "team-record ttl"})
    if len( my_data) > 0:
        new_o_pts = my_data[0].get_text()[:-4]
        if( new_o_pts != o_pts ):
            chg = int(new_o_pts) - int(o_pts)
            print("Chg: " + str(chg))
            print("New: " + str(new_o_pts))
            inst.push_change(chg, "TOT PTS", str(new_o_pts))
            o_pts = new_o_pts
    else:
        print("Failed get")
    driver.refresh()
    time.sleep(60)







#time.sleep(4)
#driver.get("http://www.espn.com/nhl/scoreboard")
#html = driver.page_source
#soup = BeautifulSoup(html,"lxml")

#for a in soup.find_all('a', href=True):
#    print("Found the URL:", a['href'])

#driver.close()




# while (0):
#     if (a % 4) == 0:
#         print(a)
#     time.sleep(5)
#     a += 1
#     print(a)