from selenium import webdriver



def run():

    #open the driver
    driver = webdriver.Chrome(r'C:\Users\Iv\Downloads\chrome\chromedriver.exe')
    #get the web page
    driver.get('http://www.google.com/xhtml')
    # find the name="" in the html
    search_box = driver.find_element_by_name('q')
    # type "ChromeDriver" + enter
    search_box.send_keys('ChromeDriver')
    search_box.submit()

    driver.quit()
