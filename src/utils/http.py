import requests

DEFAULT_REQUEST_TIMEOUT_IN_SECONDS = 15


class HttpMethods:
    POST = 'POST'
    GET = 'GET'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'


class ResponseObject:
    def __init__(self, status_code, headers, data):
        self.status_code = status_code
        self.headers = headers
        self.data = data


def http_request(request_config):
    response = requests.request(
        method=request_config['method'],
        url=request_config['url'],
        headers=request_config.get('headers', {}),
        data=request_config.get('data'),
        params=request_config.get('params'),
        timeout=DEFAULT_REQUEST_TIMEOUT_IN_SECONDS,
    )
    return ResponseObject(response.status_code, response.headers, response.json())
