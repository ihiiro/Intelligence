from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList
from intel_engine.intel_extractor import seleniumCxtmanager, extractData
from intel_engine.summary import summarize
import pathlib

# create objects
extract_google = UrlExtractor(query='what is IBM')
# extract_bing = UrlExtractor(query='IBM', search_engine='https://www.bing.com/')
# extract_yahoo = UrlExtractor(query='IBM', search_engine='https://www.search.yahoo.com/')

# extract urls
with extract_google.seleniumCxtmanager():
    url_list_google = extract_google.extractUrls()

# with extract_bing.seleniumCxtmanager():
#     url_list_bing = extract_bing.extractUrls()
#
# with extract_yahoo.seleniumCxtmanager():
#     url_list_yahoo = extract_yahoo.extractUrls()

# merge all lists into one & filter
filtered_urllist = list(filterUrlList(url_list=url_list_google))

# extract data

with seleniumCxtmanager() as driver:
    data_string = extractData(url_list=filtered_urllist, driver=driver)

with pathlib.Path('./intel.txt').open('w') as file:
    file.write(summarize(text=data_string, per=.1))
