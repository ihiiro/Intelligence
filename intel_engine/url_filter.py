import requests

def filterUrlList(url_list):
    """Keep only useful urls."""
    def filterFunc(url):
        """Check if url is up and valid."""
        # for black in blacklist:
        #     if black in url:
        #         print(f'url: "{url}"')
        #         print('Is blacklisted, filtered out.\n')
        #         return False
        try:
            with requests.head(url) as request: #with to call request.close()
                if str(request.status_code)[0] in ['4', '5']: #check if it's an error code(starts with 4 or 5)
                    print(f'url: "{url}", status code: {request.status_code}')
                    print('Is inaccessible, filtered out.\n')
                    return False
        except requests.exceptions.RequestException as e: #catch all requests.exceptions
            print(f'url: {url}')
            print(f'filtered out because of: {e}\n')
            return False
        return True

    return filter(filterFunc, url_list)
