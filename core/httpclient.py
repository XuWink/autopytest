import requests


class HttpClient:
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.Session()

    def get(self, url, **kwargs):
        pass