from intel_engine.intel_extractor import getUsefulText
from intel_engine.url_extractor import extractUrls
from intel_engine.url_filter import filterUrlList
from intel_engine.context_managers import seleniumCxtmanager
from intel_engine.context_managers import printNewLineAfter
from intel_engine.context_managers import hideUnhideCursor
import pathlib

with hideUnhideCursor():
    # extract urls
    print('Extracting urls...')
    with seleniumCxtmanager() as driver:
        with printNewLineAfter():
            url_list_google = extractUrls(query='elena tonra', driver=driver, debug=True)

    with seleniumCxtmanager() as driver:
        with printNewLineAfter():
            url_list_yahoo = extractUrls(extract_from='https://www.yahoo.com/', query='elena tonra', driver=driver, debug=True)

    with seleniumCxtmanager() as driver:
        with printNewLineAfter():
            url_list_bing = extractUrls(extract_from='https://www.bing.com/', query='elena tonra', driver=driver, debug=True)

    # merge all lists into one & filter
    print('Filtering through urls...')
    with printNewLineAfter():
        filtered_urllist = list(filterUrlList(url_list=url_list_google+url_list_yahoo+url_list_bing, debug=True))

    # Getting useful text
    print('Getting useful text based on the terms.txt file...')
    with seleniumCxtmanager() as driver:
        with printNewLineAfter():
            useful_text = getUsefulText(url_list=filtered_urllist, driver=driver, debug=True)

    # write text to files
    print('Writing to file...', end=' ')
    for text in useful_text:
        with pathlib.Path(f'text-{useful_text.index(text)+1}.txt').open('w') as file:
            file.write(text)
    print('done.')
