import json
import os
from dotenv import load_dotenv
from src.utils.http import http_request

load_dotenv()


class BifrostEntities:
    JOBS = 'jobs'


class BifrostBase:
    def __init__(self, entity: BifrostEntities):
        self.base_url = f"{os.getenv('BIFROST_URL')}/{entity}"
        self.headers = {
            'x-api-key': os.getenv('BIFROST_API_KEY'),
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
