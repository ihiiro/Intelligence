from intel_engine.intel_extractor import getUsefulUrls
from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList
from intel_engine.context_managers import seleniumCxtmanager
from intel_engine.context_managers import printNewLineAfter
from intel_engine.context_managers import hideUnhideCursor
import pathlib

with hideUnhideCursor():
    # create objects
    extract_google = UrlExtractor(query='ukraine')

    # extract urls
    print('Extracting urls...')
    with extract_google.seleniumCxtmanager():
        with printNewLineAfter():
            url_list_google = extract_google.extractUrls(debug=True)

    # merge all lists into one & filter
    print('Filtering through urls...')
    with printNewLineAfter():
        filtered_urllist = list(filterUrlList(url_list=url_list_google, debug=True))

    # get useful urls
    print('Getting useful urls based on the keywords.txt file...')
    with seleniumCxtmanager() as driver:
        with printNewLineAfter():
            useful_urls = getUsefulUrls(url_list=filtered_urllist, driver=driver, debug=True)

    # write intel to files
    with pathlib.Path('./intel.txt').open('a') as file:
        for url, info in useful_urls[0]:
            file.write(f'{url}, {info}\n')
        file.write(f'{useful_urls[1]}/{useful_urls[2]} are useful.')
