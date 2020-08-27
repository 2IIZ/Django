
from selenium import webdriver



def run():

    #open the driver
    driver = webdriver.Chrome(r'C:\Users\Iv\Downloads\chrome\chromedriver.exe')
    #get the web page
    driver.get('http://orteil.dashnet.org/cookieclicker/')

    count = 0
    while True:
        print(count)
        driver.find_element_by_id('bigCookie').click()

        # -> the web drier simulate a real person that I think why the click is very slow.
