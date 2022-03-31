from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList

extract_google = UrlExtractor(query='porn best')
extract_bing = UrlExtractor(query='porn best', search_engine='https://www.bing.com/')

with extract_google.seleniumCxtmanager():
    url_list_google = extract_google.extractUrls()

with extract_bing.seleniumCxtmanager():
    url_list_bing = extract_bing.extractUrls()


print(url_list_google)

print('\n')

print(url_list_bing)

url_list = list(dict.fromkeys(url_list_bing+url_list_google))

print('\n')

print(list(filterUrlList(url_list=url_list)))
