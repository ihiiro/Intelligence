from contextlib import contextmanager
from intel_engine.url_extractor import chromedriver_location, chrome_options, webdriver
from bs4 import BeautifulSoup
import selenium
import pathlib

@contextmanager
def seleniumCxtmanager():
    """Setup and Teardown ops on selenium driver."""
    driver = webdriver.Chrome(chromedriver_location, options=chrome_options)
    try:
        yield driver
    finally:
        driver.close()
        driver.quit()

def writeIntelToFiles(url_list, driver):
    """Extract content from webpages."""
    for url in url_list:
        driver.get(url)
        try:
            bs = BeautifulSoup(driver.find_element_by_xpath('html/body').text)
            for unwanted in bs(['script', 'style', 'header', 'footer']):
                unwanted.decompose()
            with pathlib.Path(f'./intel-{url_list.index(url)}.txt').open('w') as file:
                file.write(bs.get_text())
        except selenium.common.exceptions.NoSuchElementException:
            pass
