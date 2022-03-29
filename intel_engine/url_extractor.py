from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from contextlib import contextmanager
import shutup

# shut those annoying warnings
shutup.please()

# configure selenium
chromedriver_location = './chromedriver'
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chromedriver_location, options=chrome_options)

class UrlExtractor:
    """Extract intel urls from specified search engine search(default is google)."""
    def __init__(self, query, search_engine='https://www.google.com/'):
        self.query = query
        self.search_engine = search_engine
        self.url_initial = '"https'
        self.se_url = 'search?q='.join([self.search_engine, self.query])

    @contextmanager
    def seleniumCxtmanager(self, func):
        """Setup and Teardown ops on selenium driver."""
        driver.get(self.se_url)
        try:
            yield func()
        finally:
            driver.close()
            driver.quit()

    def initialLookup(self):
        """Look something up using specified search engine(google by default)."""
        return str(driver.page_source.encode('utf-8')) #return bytes in string format

    def constructUrl(self, start):
        """Construct urls from start string."""
        constructed_url = list()
        for c in start[1:]: # avoid the initial double quote
            # append valid url characters
            if c.isalnum() or c in ['-','.','_','~',':','/','?','#','[',']','@','!','$','&',"'",'(',')','*','+',',',';','=']:
                constructed_url.append(c)
            else:
                break
        return ''.join(constructed_url)

    def extractUrls(self):
        """Extract urls from search engine results page."""
        with self.seleniumCxtmanager(func=self.initialLookup) as response_html:
            pass
        url_list = list()
        for url in range(response_html.count(self.url_initial)):
            if url == 0:
                url_list.append(self.constructUrl(start=response_html[response_html.find(self.url_initial):]))
                continue
            response_html = response_html.split(self.url_initial, 1)[1]
            url_list.append(self.constructUrl(start=response_html[response_html.find(self.url_initial):]))
        return url_list
