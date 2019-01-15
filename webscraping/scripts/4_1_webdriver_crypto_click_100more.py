import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


def run():

    #open the driver
    driver = webdriver.Chrome(r'C:\Users\Iv\Downloads\chrome\chromedriver.exe')
    #get the web page
    driver.get('https://courscryptomonnaies.com/')

    count = 0
    ok = True
    while ok:
        print(count)
        # find the element by the text and click it
        driver.find_element(By.XPATH, '//button[text()="Voir les 100 prochaines"]').click()
        # wait 5 seconds
        time.sleep(5)
        count += 1
        #if this looped x time or more stop
        if count >=2:
            ok = False

    #save the html generated in "html"
    html = driver.page_source

    soup = BeautifulSoup(html)

    print(soup)
