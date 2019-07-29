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


with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    line_count = 0
    my_dict = {}
    my_lol = []

    for row in csv_reader:
        col_count = 0
        for col in row:
            col_count += 1
            my_dict[col] = (line_count,col_count)
        line_count += 1

inst = push.Push()
sleep_interval = 4

url = "http://fantasy.espn.com/baseball/team?leagueId=162788&seasonId=2019&teamId=4&fromTeamId=4&scoringPeriodId=124"

driver = webdriver.Chrome('C:/Users/chery/chromedriver.exe')
driver.get(url)
time.sleep(sleep_interval)

html = driver.page_source
soup = BeautifulSoup(html,"lxml")


driver.close()
exit()

my_data = soup.find_all("td",{"class":"Table2__td"})
my_data_dict = {}

count = 0
for i in my_data:
    #print(str(count) + ": " + str(i.text))
    my_data_dict[str(count)] = str(i.text)
    count+=1

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
        my_results[ my_dict[x][0] ][ my_dict[x][1] ] = my_data_dict[x]

for i in range(0,sz-1):
    print(my_results[i])

driver.close()



