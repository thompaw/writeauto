import requests
from bs4 import BeautifulSoup


class reportdeets:
    def __init__(self, identification):
        self.id = identification



def reqlink(url):
    # Get webpage and turn it into soup for extraction
    r = requests.get(url)
    if r.status_code != 200:
        print('There has been an issue retrieving the webpage')
        return
    soup = BeautifulSoup(r.content, 'html.parser')

    # Dive in and find main div tag, where everything else I need will branch off of
    jsdiv = soup.body.find_all('div')[1].find('div', "sc-gsDKAQ cFoFbs")
    print(jsdiv)    # I am having problems finding the next div tag due to js, this article explains how to bypass 
    # https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python

# reqlink(input('Link: '))
reqlink('https://hackerone.com/reports/1439026')