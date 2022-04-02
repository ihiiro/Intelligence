from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from contextlib import contextmanager
import pathlib
import shutup

# shut those annoying warnings
shutup.please()

# configure selenium
chromedriver_location = f"{next(pathlib.Path('.').glob('**/chromedriver'))}" #dynamically find chromedriver
chrome_options = Options()
chrome_options.add_argument('--headless')

class UrlExtractor:
    """Extract intel urls from specified search engine search(default is google)."""
    def __init__(self, query='', search_engine='https://www.google.com/'):
        self.query = query
        self.search_engine = search_engine
        self.url_initial = '"https'
        self.se_url = 'search?q='.join([self.search_engine, self.query])

    @contextmanager
    def seleniumCxtmanager(self):
        """Setup and Teardown ops on selenium driver."""
        self.driver = webdriver.Chrome(chromedriver_location, options=chrome_options)
        try:
            yield None
        finally:
            self.driver.close()
            self.driver.quit()

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
        print(f'Extracting urls from {self.se_url}...')
        self.driver.get(self.se_url)
        response_html = str(self.driver.page_source.encode('utf-8')) #assign bytes in string format
        url_list = list()
        for url in range(response_html.count(self.url_initial)):
            if url == 0:
                url_list.append(self.constructUrl(start=response_html[response_html.find(self.url_initial):]))
                continue
            response_html = response_html.split(self.url_initial, 1)[1]
            url_list.append(self.constructUrl(start=response_html[response_html.find(self.url_initial):]))
        return list(dict.fromkeys(url_list)) #return list with no duplicates
