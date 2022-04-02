from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList
from intel_engine.intel_extractor import seleniumCxtmanager, extractData

# create objects
# extract_google = UrlExtractor(query='last kingdom')
# extract_bing = UrlExtractor(query='last kingdom', search_engine='https://www.bing.com/')
# extract_yahoo = UrlExtractor(query='last kingdom', search_engine='https://www.search.yahoo.com/')

# extract urls
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
    print(extractData(url_list=['https://www.google.com/', 'https://www.youtube.com/'], driver=driver))
