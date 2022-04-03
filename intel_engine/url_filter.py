import requests

def filterUrlList(url_list):
    """Keep only useful urls."""
    def filterFunc(url):
        """Check if url is up and valid."""
        try:
            with requests.head(url) as request: #with to call request.close()
                if str(request.status_code)[0] in ['4', '5']: #check if it's an error code(starts with 4 or 5)
                    return False
                try:
                    if 'text/html' not in request.headers['content-type']:
                        return False
                except KeyError:
                    return False
        except requests.exceptions.RequestException as e: #catch all requests.exceptions
            return False
        return True

    return filter(filterFunc, url_list)
