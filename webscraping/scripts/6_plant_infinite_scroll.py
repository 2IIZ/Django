import time
from selenium import webdriver
from bs4 import BeautifulSoup



def run():

    #open the driver
    driver = webdriver.Chrome(r'C:\Users\Iv\Downloads\chrome\chromedriver.exe')
    #get the web page
    driver.get('https://identify.plantnet-project.org/explo/provence/')

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    #save the html generated in "html"
    html = driver.page_source

    soup = BeautifulSoup(html)

    print(soup)
