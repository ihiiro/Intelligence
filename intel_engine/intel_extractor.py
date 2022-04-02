from contextlib import contextmanager
from intel_engine.url_extractor import chromedriver_location, chrome_options, webdriver

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
        driver.get(url)
        data_list.append(driver.page_source.encode('utf-8'))
    return data_list
