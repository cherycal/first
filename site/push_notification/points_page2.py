__author__ = 'chance'

import time
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
import push

file_name = 'espn_layout.csv'

sz = 25
cols = 15
my_results = [None] * sz
for i in range(0,sz-1):
    my_results[i] = [None] * cols


inst = push.Push()
sleep_interval = 4

scoring_interval = 12


url = "http://fantasy.espn.com/baseball/team?leagueId=162788&seasonId=2019&teamId=4&fromTeamId=4" \
      "&scoringPeriodId=" + str(scoring_interval)

driver = webdriver.Chrome('C:/Users/chery/chromedriver.exe')
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
lines = 14
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
        #print(str(iter) + " : " + str(j) + " : " + str(my_ds) )
        if(iter == 1):
            batting[str(j)] = my_ds
        if(iter == 2 or iter == 3 ):
            batting[str(j)].append(my_ds)
        if( iter == 4):
            lines = 10
            pitching[str(j)] = my_ds
        if(iter > 4 ):
            pitching[str(j)].append(my_ds)
        count += 1
        j += 1

for i in range(0,14):
    print(batting[str(i)])

for i in range(0,10):
    print(pitching[str(i)])

driver.close()
exit(0)


my_offset = my_base - my_newbase

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    line_count = 0
    my_dict = {}
    my_lol = []

    for row in csv_reader:
        col_count = 0
        for col in row:
            index = col
            col_count += 1
            if(int(col) >= my_base - my_offset and int(col) < 1000 ):
                index = str(int(col) - my_offset)
            #print("col: " + col + " index: " + index + " offset: " + str(my_offset))
            print("index: " + index + "(" + str(line_count) + "," + str(col_count) + ")")
            my_dict[index] = (line_count,col_count)
        line_count += 1


count = 0
for i in my_data:
    my_td = i.find_all("div",{"class":"jsx-2893327412 player-column__bio"})
    if (len(my_td)):
        for i in my_td:
            my_a = i.find("a")
            #print(str(count) + ": " + my_a.text)
            my_data_dict[str(count)] = my_a.text
    count = count + 1

for i in range(0,600):
    x = str(i)
    if (my_dict.get(x)):
        #print(x, my_dict[x][0], my_dict[x][1], my_data_dict[x])
        my_results[ my_dict[x][0] ][0] = my_dt
        my_results[ my_dict[x][0] ][ my_dict[x][1] ] = my_data_dict[x]

for i in range(0,sz-1):
    print(my_results[i])

driver.close()



