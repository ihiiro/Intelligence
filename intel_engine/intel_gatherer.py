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

    def constructUrl(self, start):
        """Construct urls from start string."""
        constructed_url = list()
        for c in start:
            # only append valid url characters
            if c.isalnum() or c in ['-','.','_','~',':','/','?','#','[',']','@','!','$','&',"'",'(',')','*','+',',',';','=']:
                constructed_url.append(c)
        return ''.join(constructed_url)

    def extractUrls(self):
        """Extract urls from search engine results page."""
        response_html = self.initialLookup().text
        url_list = list()
        return self.constructUrl(start=response_html[response_html.find('https'):])

gather_intel = GatherIntel(query='the man')

print(gather_intel.extractUrls())
