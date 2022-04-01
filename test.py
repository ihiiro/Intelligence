from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList

# create objects
extract_google = UrlExtractor(query='porn best')
extract_bing = UrlExtractor(query='porn best', search_engine='https://www.bing.com/')
extract_yahoo = UrlExtractor(query='porn best', search_engine='https://www.search.yahoo.com/')
extract_pse = UrlExtractor(query='porn best', search_engine='https://www.pornhub.com/')

# extract urls
with extract_google.seleniumCxtmanager():
    url_list_google = extract_google.extractUrls()

with extract_bing.seleniumCxtmanager():
    url_list_bing = extract_bing.extractUrls()

with extract_yahoo.seleniumCxtmanager():
    url_list_yahoo = extract_yahoo.extractUrls()

with extract_pse.seleniumCxtmanager():
    url_list_pse = extract_pse.extractUrls()

print(url_list_google)

print('\n')

print(url_list_bing)

print('\n')

print(url_list_yahoo)

print('\n')

print(url_list_pse)

url_list = list(dict.fromkeys(url_list_bing+url_list_google+url_list_yahoo+url_list_pse))

print('\n')

print(list(filterUrlList(url_list=url_list)))
