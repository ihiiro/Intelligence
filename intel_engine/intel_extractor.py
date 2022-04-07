from bs4 import BeautifulSoup
import selenium
import pathlib

def getUsefulText(url_list, driver, debug=False):
    """Return list of useful text from useful urls."""
    useful_text = []
    try:
        keywords_file_location = f"{next(pathlib.Path('.').glob('**/keywords.txt'))}"
    except StopIteration:
        raise Exception('no keywords.txt file in directory.')
    with pathlib.Path(keywords_file_location).open('r') as file:
        file_content = file.read()
    if file_content.isspace() or len(file_content) == 0:
        raise Exception('keywords.txt file is empty.')
    keywords = file_content.split(',')
    length_of_keywords_list = len(keywords)
    for url in url_list:
        if debug:
            print(f'{url_list.index(url)+1}/{len(url_list)}, {len(useful_urls)} useful.\r', end='', flush=True)
        try:
            driver.get(url)
        except selenium.common.exceptions.WebDriverException: #base webdriver exception
            continue
        try:
            bs = BeautifulSoup(driver.find_element_by_xpath('html/body').text)
        except selenium.common.exceptions.NoSuchElementException:
            continue
        for unwanted in bs(['script', 'style', 'header', 'footer']):
            unwanted.decompose()
        bs_in_lowercase = bs.get_text().lower()
        num_of_keywords_found = 0
        for keyword in keywords:
            if keyword.lower() in bs_in_lowercase:
                num_of_keywords_found += 1
        if num_of_keywords_found > 0:
            useful_urls.append(f'{url}:\n{bs.get_text()}\n')
    return useful_urls
