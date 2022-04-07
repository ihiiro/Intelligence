from bs4 import BeautifulSoup
import selenium
import pathlib

def extractImportants(text, terms_found, debug=False):
    """Extract important bits of text."""
    importants = []
    for term in terms_found:
        temp_text = text
        for ocrnc in range(temp_text.find(term)):
            try:
                for c in temp_text[temp_text.index(term):]:
                    if c == '\n':
                        importants.append('\n'*2)
                        break
                    importants.append(c)
            except ValueError:
                continue
            temp_text = temp_text.split(term, 1)[1]
    return ''.join(importants)

def getUsefulText(url_list, driver, debug=False):
    """Return list of useful text from useful urls."""
    useful_text = []
    try:
        terms_file_location = f"{next(pathlib.Path('.').glob('**/terms.txt'))}"
    except StopIteration:
        raise Exception('no terms.txt file in directory.')
    with pathlib.Path(terms_file_location).open('r') as file:
        file_content = file.read()
    if file_content.isspace() or len(file_content) == 0:
        raise Exception('terms.txt file is empty.')
    terms = file_content.strip().lower().split(',') #stripping the files of EOF newlines
    for url in url_list:
        terms_found = []
        try:
            driver.get(url)
        except selenium.common.exceptions.WebDriverException: #base webdriver exception
            continue
        try:
            bs = BeautifulSoup(driver.find_element_by_xpath('html/body').get_attribute('innerHTML'))
        except selenium.common.exceptions.NoSuchElementException:
            continue
        for unwanted in bs(['style', 'header', 'footer', 'nav', 'script']):
            unwanted.decompose()
        bs_in_lowercase = bs.get_text().lower()
        for term in terms:
            if term in bs_in_lowercase:
                terms_found.append(term)
        if len(terms_found) > 0:
            useful_text.append(extractImportants(text=bs_in_lowercase, terms_found=terms_found))
        if debug:
            print(f'{url_list.index(url)+1}/{len(url_list)}, {len(useful_text)} useful.\r', end='', flush=True)
    return useful_text
