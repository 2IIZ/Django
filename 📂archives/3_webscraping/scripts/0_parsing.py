# Create a script : https://django-extensions.readthedocs.io/en/latest/runscript.html

# pip install django-extensions
# add this to the apps settings. 'django_extensions',

# pip install BeautifulSoup4

#import libraries
from urllib.request import urlopen # to get the HTML page of an url.
from bs4 import BeautifulSoup

def run():

    markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(markup)

    name_box = soup.b.string

    print(name_box)
