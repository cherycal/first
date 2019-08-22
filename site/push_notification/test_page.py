__author__ = 'chance'

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import push
inst = push.Push()

sleep_interval = 120


url = "http://fantasy.espn.com/baseball/recentactivity?leagueId=162788"

driver = webdriver.Chrome('C:/Users/chery/chromedriver.exe')
driver.get(url)
time.sleep(sleep_interval)

