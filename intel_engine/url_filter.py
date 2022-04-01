import requests

def filterUrlList(url_list, blacklist=['gstatic.com', 'google.com', 'google.co', 'youtube.com']):
    """Keep only useful urls."""
    def filterFunc(url):
        """Check if url is up and valid."""
        for black in blacklist:
            if black in url:
                print(f'url: "{url}"')
                print('Is blacklisted, filtered out.\n')
                return False
        try:
            with requests.get(url) as request: #with to call request.close()
                if request.status_code == 404:
                    print(f'url: "{url}"')
                    print('Is inaccessible, filtered out.\n')
                    return False
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL, requests.exceptions.SSLError) as e:
            print(f'url: {url}')
            print(f'filtered out because of: {e}\n')
            return False
        return True

    return filter(filterFunc, url_list)
