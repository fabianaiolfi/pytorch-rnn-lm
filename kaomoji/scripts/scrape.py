#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

page_num = 1

while page_num < 20:

    page_num = str(page_num)

    # Set the URL you want to webscrape from
    url = 'http://japaneseemoticons.me/all-japanese-emoticons/' + page_num

    # Connect to the URL
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    my_scrape = soup.findAll('td')

    my_output = open("scraped.txt", "a")

    n = 0
    for i in my_scrape:
        my_scrape = soup.findAll('td')[n]
        for i in my_scrape:
            try:
                my_output.write(i)
                my_output.write('\n')
            except:
                pass
        n += 1

    page_num = int(page_num)
    page_num += 1
    time.sleep(1)
