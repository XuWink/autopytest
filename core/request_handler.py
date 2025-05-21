import requests
import json
from typing import Optional, Dict, Any, Union

class RequestHandler:
    def __init__(self, api_root_url: str, session: Optional[requests.Session] = None):
        self.api_root_url = api_root_url.rstrip('/') # 确保不以斜杠结尾
        self.session = session or requests.Session()

        """
        request(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None)
        """

    def request(self, method, url, **kwargs):
        url = f"{self.api_root_url}/{url}"
        return self.session.request(method, url, **kwargs)
    
    def close(self) -> None:
        """关闭Session连接"""
        self.session.close()

    def __enter__(self) -> 'RequestHandler':
        """上下文管理器入口"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """上下文管理器退出时自动关闭连接"""
        self.close()