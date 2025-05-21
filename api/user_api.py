
from autopytest.core.request_handler import RequestHandler

class UserApi(RequestHandler):
    def __init__(self, api_root_url, session = None):
        super().__init__(api_root_url, session)

    def list_all_users(self, **kwargs):
        return self.request("GET", "/users", **kwargs)