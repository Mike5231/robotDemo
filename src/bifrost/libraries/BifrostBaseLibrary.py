from src.utils.http import http_request


class BifrostBase:
    def __init__(self):
        self.base_url = "https://nebula.vormir.instaleap.io"
        self.headers = {
            'Authorization': 'Bearer'
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
