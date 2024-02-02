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
        request_config['method'],
        request_config['url'],
        headers=request_config.get('headers', {}),
        data=request_config.get('data'),
        params=request_config.get('params'),
        timeout=DEFAULT_REQUEST_TIMEOUT_IN_SECONDS,
    )
    print(response)
    print(response.json())
    response_json = response.json()
    response_text = response.text
    response_object = ResponseObject(response.status_code, response.headers, response.json())
    return response
