from src.utils.http import HttpMethods
from src.bifrost.libraries.BifrostBaseLibrary import BifrostBase

bifrost_instance = BifrostBase()


def get_job(job_id):
    endpoint = f"jobs/{job_id}"
    return bifrost_instance.make_request(HttpMethods.GET, endpoint)
