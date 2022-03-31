from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList

extract_urls = UrlExtractor(query='epic gamer moment')

url_list = extract_urls.extractUrls()
print(url_list)

print('\n')

print(list(filterUrlList(url_list=url_list)))
