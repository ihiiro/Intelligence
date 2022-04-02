from contextlib import contextmanager
from intel_engine.url_extractor import chromedriver_location, chrome_options, webdriver
from bs4 import BeautifulSoup

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
    data_list = list()
    for url in url_list:
        print(f'Extracting data from pages {int((url_list.index(url)+1)/len(url_list)*100)}%\r', flush=True, end='')
        driver.get(url)
        data_list.append(driver.find_element_by_xpath('html/body').text)
    bs = BeautifulSoup(''.join(data_list))
    for unwanted in bs(['script', 'style']):
        unwanted.decompose()
    return bs.get_text()
