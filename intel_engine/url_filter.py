import requests

def filterUrlList(url_list):
    """Keep only useful urls."""
    def filterFunc(url):
        """Check if url is up and valid."""
        try:
            with requests.head(url) as request: #with to call request.close()
                if str(request.status_code)[0] in ['4', '5']: #check if it's an error code(starts with 4 or 5)
                    print(f'url: "{url}", status code: {request.status_code}')
                    print('Is inaccessible, filtered out.\n')
                    return False
                try:
                    if 'text/html' not in request.headers['content-type']:
                        print(f'url: "{url}", status_code: {request.status_code}')
                        print(f'content-type: {request.headers["content-type"]}, filtered out.\n')
                        return False
                except KeyError:
                    print(f'url: "{url}", status_code: {request.status_code}')
                    print(f'HTTP content-type header is not specified, filtered out.\n')
                    return False
        except requests.exceptions.RequestException as e: #catch all requests.exceptions
            print(f'url: {url}')
            print(f'filtered out because of: {e}\n')
            return False
        return True

    return filter(filterFunc, url_list)
