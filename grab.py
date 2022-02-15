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
    main_div = soup
    print(main_div)

reqlink(input('Link: '))
