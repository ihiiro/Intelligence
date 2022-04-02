from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList

# create objects
extract_google = UrlExtractor(query='vladimir putin')
extract_bing = UrlExtractor(query='vladimir putin', search_engine='https://www.bing.com/')
extract_yahoo = UrlExtractor(query='vladimir putin', search_engine='https://www.search.yahoo.com/')

# extract urls
with extract_google.seleniumCxtmanager():
    url_list_google = extract_google.extractUrls()

with extract_bing.seleniumCxtmanager():
    url_list_bing = extract_bing.extractUrls()

with extract_yahoo.seleniumCxtmanager():
    url_list_yahoo = extract_yahoo.extractUrls()

print(url_list_google)

print('\n')

print(url_list_bing)

print('\n')

print(url_list_yahoo)

url_list = list(dict.fromkeys(url_list_bing+url_list_google+url_list_yahoo))

print('\n')

filtered_urllist = list(filterUrlList(url_list=url_list))
print(filtered_urllist, len(filtered_urllist))
