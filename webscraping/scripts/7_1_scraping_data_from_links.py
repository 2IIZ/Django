from urllib.request import urlopen # to get the HTML page of an url.
from bs4 import BeautifulSoup
import re  # module re


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
                       # extract_data("http://nature.jardin.free.fr/"+string)
                       extract_data("http://nature.jardin.free.fr/arbre/jlv_acer_cap_aur.html")
                       return

def extract_data(full_url):
    with urlopen(full_url) as response: # open the requested url
        raw_html = response.read() # load the html
        soup = BeautifulSoup(raw_html, 'html.parser')

        p_pattern = re.compile("<[Bb]>.*")
        extracted_html = re.findall(p_pattern, str(soup))
        extracted_html = ''.join(extracted_html)

        extracted_html = re.sub('<br>', ' ', extracted_html)
        extracted_html = re.sub('&eacute;', 'é', extracted_html)
        extracted_html = re.sub('&Eacute;', 'É', extracted_html)
        extracted_html = re.sub('&egrave;', 'è', extracted_html)
        extracted_html = re.sub('&ecirc;', 'ê', extracted_html)
        extracted_html = re.sub('&agrave;', 'à', extracted_html)
        extracted_html = re.sub('&acirc;', 'â', extracted_html)
        extracted_html = re.sub('&nbsp;', ' ', extracted_html)
        extracted_html = re.sub('<([Bb]|/[Bb]|[Aa]|/[Aa]|[Ii]|/[Ii])[^>]{0,}>', '', extracted_html)

        extracted_html = re.split('Nom commun :|Nom latin :|famille :|catégorie :|port :|feuillage :', extracted_html)

        del(extracted_html[0])

        key = ["Nom commun :", "Nom latin :", "Famille :","Catégorie :", "Port :", "Feuillage :"]
        list = {}

        for x in range(0, len(key)):
            list[key[x]] = extracted_html[x]

        for key, value in list.items():
        	print(key, value, "\n")
