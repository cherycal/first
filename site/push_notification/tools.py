import sys
import sqldb
import tools
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

def get_driver():
    platform = get_platform()
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    if (platform == "Windows"):
        driver = webdriver.Chrome('C:/Users/chery/chromedriver.exe', chrome_options=options)
    elif (platform == "linux"):
        driver = webdriver.Chrome(chrome_options=options)
    else:
        print("Platform " + platform + " not recognized. Exiting.")
        exit(-1)
    return driver