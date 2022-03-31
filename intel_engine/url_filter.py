import requests

def filterUrlList(url_list, blacklist=['gstatic.com', 'google.com', 'google.co', 'youtube.com']):
    """Keep only useful urls."""
    def filterFunc(url):
        """Check if url is up and valid."""
        if url == 'https:':
            print(f'url: "{url}"')
            print('Filtered out.\n')
            return False
        for black in blacklist:
            if black in url:
                print(f'url: "{url}"')
                print('Is blacklisted, filtered out.\n')
                return False
        with requests.get(url) as request: #with to call request.close()
            if request.status_code == 404:
                print(f'url: "{url}"')
                print('Is inaccessible, filtered out.\n')
                return False
        return True

    return filter(filterFunc, url_list)
