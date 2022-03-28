class GatherIntel:
    """Gather intelligence from the internet"""
    def __init__(self, query, search_engine='https://www.google.com/'):
        self.query = query
        self.search_engine = search_engine
        self.response = None

    def initialLookup(self):
        """Look something up using specified search engine(google by default)."""
        import requests
        url = 'search?q='.join([self.search_engine, self.query])
        self.response = requests.get(url)
        return self.response

    def extractUrls(self):
        """Extract urls from search engine results page"""
        if self.response != None: #true if .initialLookup() was called by object
            if self.response.status_code == 200:
                print('can be exracted')
        else: #true if object did not call .initialLookup()
            if self.initialLookup().status_code == 200:
                print('can be extraced(had to call method)')

gather_intel = GatherIntel('hefkdf')

gather_intel.initialLookup()
gather_intel.extractUrls()
