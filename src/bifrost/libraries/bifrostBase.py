import json

from src.utils.http import http_request
import os


class BifrostBase:
    def __init__(self):
        self.base_url = "https://api.vormir.instaleap.io"
        self.headers = {
            'x-api-key': '',
            'Content-Type': 'application/json'
        }

    def make_request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        request_config = {
            'url': url,
            'method': method,
            'headers': self.headers,
        }
        if data is not None:
            request_config['data'] = json.dumps(data)
        return http_request(request_config)
