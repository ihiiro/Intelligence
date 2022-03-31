import requests

def filterUrlList(url_list, blacklist=['gstatic.com', 'google.com', 'google.co', 'youtube.com']):
    """Keep only useful urls."""
    def filterFunc(url):
        """Check if url is up and valid."""
        if url == 'https:':
            return False
        for black in blacklist:
            if black in url:
                return False
        with requests.get(url) as request: #with to call request.close()
            return request.status_code == 200

    return filter(filterFunc, url_list)
