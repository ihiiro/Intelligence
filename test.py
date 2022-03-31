from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList

extract_urls = UrlExtractor(query='rick and morty')

url_list = extract_urls.extractUrls()
print(url_list)

print('\n')

r = filterUrlList(url_list=url_list)
print('\n')
print(list(r))
