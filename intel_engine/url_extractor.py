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

def constructUrl(start):
    """Construct urls from start string."""
    constructed_url = list()
    for c in start[1:]: # avoid the initial double quote
        # append valid url characters
        if c.isalnum() or c in ['-','.','_','~',':','/','?','#','[',']','@','!','$','&',"'",'(',')','*','+',',',';','=']:
            constructed_url.append(c)
        else:
            break
    return ''.join(constructed_url)

def extractUrls(driver, extract_from='https://www.google.com/', query='', debug=False):
    """Extract urls from page."""
    url_initial = '"https'
    se_url = 'search?q='.join([extract_from, query])
    driver.get(se_url)
    response_html = str(driver.page_source.encode('utf-8')) #assign bytes in string format
    url_list = list()
    for url in range(response_html.count(url_initial)):
        if debug:
            print(f'{len(url_list)} urls extracted from {se_url}\r', end='', flush=True)
        if url == 0:
            url_list.append(constructUrl(start=response_html[response_html.find(url_initial):]))
            continue
        response_html = response_html.split(url_initial, 1)[1]
        url_list.append(constructUrl(start=response_html[response_html.find(url_initial):]))
    url_list_no_duplicates = list(dict.fromkeys(url_list))
    if debug:
        print(f'\nwithout duplicates: {len(url_list_no_duplicates)}', end='')
    return url_list_no_duplicates
