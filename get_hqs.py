from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import requests
import pandas as pd


## get companies having hqs in China 
for id_num in range(106454, 108000):
    url = requests.get(f'http://securities.stanford.edu/filings-case.html?id={id_num}').text
    soup = BeautifulSoup(url, 'xml')
    company = soup.find_all('h4')[4]
    tags = soup.find_all('div', {"class": 'span4'})[2]
    if " China" in tags.text:
        print(id_num, company)

## get non-U.S. based compaines for comparison
    for tag in tags:
        if ("United States" not in tags.text) & (" " not in tags.text):
            print(id_num)



