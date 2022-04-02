from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList
from intel_engine.intel_extractor import seleniumCxtmanager, extractData
# from intel_engine.intel_builder import getText

# create objects
extract_google = UrlExtractor(query='porn')
# extract_bing = UrlExtractor(query='porn', search_engine='https://www.bing.com/')
# extract_yahoo = UrlExtractor(query='porn', search_engine='https://www.search.yahoo.com/')
#
# # extract urls
# with extract_google.seleniumCxtmanager():
#     url_list_google = extract_google.extractUrls()
#
# with extract_bing.seleniumCxtmanager():
#     url_list_bing = extract_bing.extractUrls()
#
# with extract_yahoo.seleniumCxtmanager():
#     url_list_yahoo = extract_yahoo.extractUrls()

# merge all lists into one & filter
# filtered_urllist = list(filterUrlList(url_list=list(dict.fromkeys(url_list_google+url_list_bing+url_list_yahoo))))

# extract data

with seleniumCxtmanager() as driver:
    data_list = extractData(url_list=['https://en.wikipedia.org/wiki/Computer_science'], driver=driver)

print(data_list)
