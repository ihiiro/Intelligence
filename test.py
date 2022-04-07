from intel_engine.intel_extractor import getUsefulText
from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList
from intel_engine.context_managers import seleniumCxtmanager
from intel_engine.context_managers import printNewLineAfter
from intel_engine.context_managers import hideUnhideCursor
import pathlib

with hideUnhideCursor():
    # create objects
    # extract_google = UrlExtractor(query='anthony hopkins')
    # extract_yahoo = UrlExtractor(query='anthony hopkins', extract_from='https://www.yahoo.com/')
    # extract_bing = UrlExtractor(query='anthony hopkins', extract_from='https://www.bing.com/')
    #
    # # extract urls
    # print('Extracting urls...')
    # with extract_google.seleniumCxtmanager():
    #     with printNewLineAfter():
    #         url_list_google = extract_google.extractUrls(debug=True)
    #
    # with extract_yahoo.seleniumCxtmanager():
    #     with printNewLineAfter():
    #         url_list_yahoo = extract_yahoo.extractUrls(debug=True)
    #
    # with extract_bing.seleniumCxtmanager():
    #     with printNewLineAfter():
    #         url_list_bing = extract_bing.extractUrls(debug=True)
    #
    # # merge all lists into one & filter
    # print('Filtering through urls...')
    # with printNewLineAfter():
    #     filtered_urllist = list(filterUrlList(url_list=url_list_google+url_list_yahoo+url_list_bing, debug=True))

    # Getting useful text
    print('Getting useful text based on the terms.txt file...')
    with seleniumCxtmanager() as driver:
        with printNewLineAfter():
            useful_text = getUsefulText(url_list=['https://en.wikipedia.org/wiki/Anthony_Hopkins'], driver=driver, debug=True)

    # write text to files
    for text in useful_text:
        with pathlib.Path(f'text-{useful_text.index(text)+1}.txt').open('w') as file:
            file.write(text)
