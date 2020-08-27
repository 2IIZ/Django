import time

from selenium import webdriver



def run():

    #open the driver
    driver = webdriver.Chrome(r'C:\Users\Iv\Downloads\chrome\chromedriver.exe')
    #get the web page
    driver.get('https://courscryptomonnaies.com/')
    # find the element by the text and click it
    driver.find_element_by_link_text('Se connecter').click()

    time.sleep(5)
    driver.quit()
