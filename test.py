from intel_engine.url_extractor import UrlExtractor
from intel_engine.url_filter import filterUrlList
from intel_engine.intel_extractor import writeIntelToFiles, seleniumCxtmanager

# create objects
extract_google = UrlExtractor(query='is it okay if I shower with cold water right after hot water?')

# extract urls
print('Extracting urls...', end=' ', flush=True)
with extract_google.seleniumCxtmanager():
    url_list_google = extract_google.extractUrls()
print('done.')

# merge all lists into one & filter
print('Filtering through urls...', end=' ', flush=True)
filtered_urllist = list(filterUrlList(url_list=url_list_google))
print('done.')

# output to files
print('Writing intel to files...', end=' ', flush=True)
with seleniumCxtmanager() as driver:
    writeIntelToFiles(url_list=filtered_urllist, driver=driver)
print('done.')
