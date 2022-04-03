from contextlib import contextmanager
from intel_engine.url_extractor import chromedriver_location, chrome_options, webdriver
from bs4 import BeautifulSoup
import selenium

@contextmanager
def seleniumCxtmanager():
    """Setup and Teardown ops on selenium driver."""
    driver = webdriver.Chrome(chromedriver_location, options=chrome_options)
    try:
        yield driver
    finally:
        driver.close()
        driver.quit()

def extractData(url_list, driver):
    """Extract content from webpages."""
    print('\033[? 25l', end='') #hide cursor
    data_list = list()
    for url in url_list:
        print('\x1b[2K', end='') #delete previous line.
        print(f'Extracting data from pages {int((url_list.index(url)+1)/len(url_list)*100)}%\r', end='')
        driver.get(url)
        try:
            data_list.append(driver.find_element_by_xpath('html/body').text)
        except selenium.common.exceptions.NoSuchElementException:
            continue
    bs = BeautifulSoup(''.join(data_list))
    for unwanted in bs(['script', 'style']):
        unwanted.decompose()
    print('\033[? 25h', end='') #unhide cursor
    return bs.get_text()
