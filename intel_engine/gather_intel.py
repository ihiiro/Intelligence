import requests

class GatherIntel:
    """Gather intelligence from the internet."""
    def __init__(self, query, search_engine='https://www.google.com/'):
        self.query = query
        self.search_engine = search_engine

    def initialLookup(self):
        """Look something up using specified search engine(google by default)."""
        url = 'search?q='.join([self.search_engine, self.query])
        return requests.get(url)

    def extractUrls(self):
        """Extract urls from search engine results page."""
        response_text = self.initialLookup().text
        url_list = list()
        print(response_text[response_text.find('https')-20:response_text.find('https')+len('https')+80])
        response_text = response_text.split('https', 1)[1]
        print(response_text[response_text.find('https')-20:response_text.find('https')+len('https')+80])
        response_text = response_text.split('https', 1)[1]
        print(response_text[response_text.find('https'):response_text.find('https')+len('https')+80])
        response_text = response_text.split('https', 1)[1]
        print(response_text[response_text.find('https'):response_text.find('https')+len('https')+80])
        response_text = response_text.split('https', 1)[1]
        print(response_text[response_text.find('https'):response_text.find('https')+len('https')+80])
        response_text = response_text.split('https', 1)[1]
        print(response_text[response_text.find('https'):response_text.find('https')+len('https')+80])
        response_text = response_text.split('https', 1)[1]
        print(response_text[response_text.find('https'):response_text.find('https')+len('https')+80])
        response_text = response_text.split('https', 1)[1]
        print(response_text[response_text.find('https'):response_text.find('https')+len('https')+80])
        response_text = response_text.split('https', 1)[1]
        print(response_text[response_text.find('https'):response_text.find('https')+len('https')+80])

gather_intel = GatherIntel('the man')

gather_intel.extractUrls()
