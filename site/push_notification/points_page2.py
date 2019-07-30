__author__ = 'chance'

import time
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
import push

sz = 25
cols = 15
my_results = [None] * sz
for i in range(0,sz-1):
    my_results[i] = [None] * cols

out_file = 'totals.csv'

inst = push.Push()
sleep_interval = 5

driver = webdriver.Chrome('C:/Users/chery/chromedriver.exe')

scoring_intervals = range(1,131)

for scoring_interval in scoring_intervals:

    url = "http://fantasy.espn.com/baseball/team?leagueId=162788&seasonId=2019&teamId=4&fromTeamId=4" \
          "&scoringPeriodId=" + str(scoring_interval)


    driver.get(url)
    time.sleep(sleep_interval)

    html = driver.page_source
    soup = BeautifulSoup(html,"lxml")

    my_th = soup.find_all("th",{"class": "tc bg-clr-white Table2__th"})
    my_dt = my_th[1].text

    my_data = soup.find_all("tr",{"class":"Table2__tr Table2__tr--lg Table2__odd"})
    my_data_dict = {}

    iter = 0
    count = 0
    batlines = 14
    pitchlines = 10
    lines = batlines
    j = 0
    batting = {}
    pitching = {}
    for i in my_data:
        if (int( i['data-idx'] ) < lines ):
            if( int(i['data-idx']) == 0 ):
                j = 0
                iter += 1
            my_ds = []
            my_divs = i.find_all("div")
            for ds in my_divs:
                my_ds.append(ds.text)
            if( ( iter == 1 or iter == 4 ) and len(my_ds) > 6):
                my_ds = [my_dt, str(scoring_interval), '', my_ds[0],my_ds[6]]
            if(iter == 1):
                batting[str(j)] = my_ds
            if(iter == 2 or iter == 3 ):
                dc = 0
                for d in my_ds:
                    batting[str(j)].append(d)
                    if(iter == 2 and dc == 8):
                        batting[str(j)].append('')
                    dc += 1
                batting[str(j)][0] = my_dt
                batting[str(j)][1] = scoring_interval
            if( iter == 4):
                lines = pitchlines
                pitching[str(j)] = my_ds
            if(iter > 4 ):
                for d in my_ds:
                    pitching[str(j)].append(d)
                pitching[str(j)][0] = my_dt
                pitching[str(j)][1] = scoring_interval
            count += 1
            j += 1

    batcell = str(batlines-1)
    pitchcell = str( pitchlines -1)
    battotal = batting[batcell][len(batting[batcell]) - 1]
    if (battotal == "--"):
        battotal = "0"
    pitchtotal = pitching[pitchcell][len(pitching[pitchcell])-1]
    if(pitchtotal == "--"):
        pitchtotal = "0"

    pitching[pitchcell].append( str( int( pitchtotal ) + int( battotal ) ) )

    with open(out_file, 'a', newline='') as output:
        csv_writer = csv.writer(output)

        for i in range(0,14):
            print(batting[str(i)])
            csv_writer.writerow(batting[str(i)])

        for i in range(0,10):
            print(pitching[str(i)])
            csv_writer.writerow(pitching[str(i)])



driver.close()
exit(0)




