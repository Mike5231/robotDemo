from src.utils.http import http_request
import os


class BifrostBase:
    def __init__(self):
        self.base_url = "https://api.vormir.instaleap.io"
        self.headers = {
            'x-api-key': ''
        }

    def make_request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        request_config = {
            'url': url,
            'method': method,
            'headers': self.headers,
            'data': data,
        }
        return http_request(request_config)
