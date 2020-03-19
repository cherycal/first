__author__ = 'chance'

import tools
from bs4 import BeautifulSoup
import time
import push
from git import Repo
from datetime import datetime

inst = push.Push()

sleep_interval = 6

url = "https://www.stubhub.com/the-strokes-tickets-the-strokes-inglewood-the-forum-los-angeles-3" \
      "-14-2020/event/104567878/?sliderMax=203.84%2C34.92&qty=2&sort=quality%20desc%2Cprice%20asc&sortKey=bestSeats&excl=1"

gitfile_name = "site/mobile/stub.txt"
outfile_name = "/media/sf_Shared/first/site/mobile/stub.txt"

repo = Repo("/media/sf_Shared/first")
assert not repo.bare
git = repo.git

flag = 0

while (1):

    now = datetime.now()  # current date and time
    date_time = now.strftime("%m/%d/%Y-%H:%M:%S")

    f = open(outfile_name, "w")
    driver = tools.get_driver()
    driver.get(url)
    time.sleep(sleep_interval)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    for div in soup.find_all('div', class_='RoyalTicketListPanel__column'):
        for h1 in div.find_all('h1'):
            flag = 0
            section = h1.text
            section_name = section.split()
            len_sec_num = len(section_name)
            section_short = section_name[len_sec_num-1]
            if(section_short.isnumeric()):
                section_number = int(section_short)
                if( (section_number >= 108 and section_number <= 113 ) or (section_number < 4) or (
                        section_number >= 124 and section_number <= 129 )):
                    flag = 1
                    print(section_short)
                    f.write(section_short)
                    f.write("\n")
                    break
            else:
                flag = 1
                print(section_short)
                f.write(section_short)
                f.write("\n")
                break

        for px in div.find_all('div', class_='PriceDisplay__price'):
            if(flag):
                print(px.text)
                f.write(px.text)
                print('')
                f.write("\n\n")


    print(date_time)
    f.write(date_time)
    f.close()


    git.add(gitfile_name)
    time.sleep(sleep_interval)
    git.commit('-m','update',gitfile_name)
    time.sleep(sleep_interval)
    git.push()
    time.sleep(sleep_interval)
    driver.quit()
    time.sleep(120)


