from urllib.request import urlopen # to get the HTML page of an url.
from bs4 import BeautifulSoup

def run():

    # specify the url
    quote_page = "https://courscryptomonnaies.com/bitcoin"

    # query the website and return the html to the variable ‘page’
    with urlopen(quote_page) as response:
           html = response.read()

           # parse the html using beautiful soup and store in variable `soup`
           soup = BeautifulSoup(html, 'html.parser')

           # Here’s where we can start coding the part that extracts the data. #
           price_xrp = soup.find("div", class_="price-value")
           name_xrp = soup.find("h1", class_="card-title")

           print(name_xrp.string, "=",price_xrp.span.string)
