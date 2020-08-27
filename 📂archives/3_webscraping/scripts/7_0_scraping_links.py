from urllib.request import urlopen # to get the HTML page of an url.
from bs4 import BeautifulSoup

def run():

    quote_page = "http://nature.jardin.free.fr/listea.html"

    with urlopen(quote_page) as response:
           html = response.read()
           soup = BeautifulSoup(html, 'html.parser')

           for link in soup.find_all('a'):
               string = link.get('href')
               substring = "/"
               subsubstring = "html"
               if substring in string:
                   if subsubstring in string:
                       extract_data("http://nature.jardin.free.fr/"+string)


def extract_data(full_url):
    with urlopen(full_url) as response: # open the requested url
        # html = response.read()  # load the html
        # soup = BeautifulSoup(html, 'html.parser')
        print(full_url)
