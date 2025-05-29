
from core.request_handler import RequestHandler
from config.setting import api_root_url

class UserApi(RequestHandler):
    def __init__(self, api_root_url = api_root_url, session = None):
        super().__init__(api_root_url, session)

    def list_all_users(self, **kwargs):
        return self.request("GET", "/users", **kwargs)
    
    def login(self, **kwargs):
        return self.request("POST", "/login", **kwargs)

user_api = UserApi()