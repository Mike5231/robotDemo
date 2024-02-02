from src.utils.http import HttpMethods
from src.bifrost.libraries.bifrostBase import BifrostBase, BifrostEntities

bifrost_instance = BifrostBase(BifrostEntities.JOBS)


def get_job(job_id):
    return bifrost_instance.make_request(HttpMethods.GET, job_id)


def get_job2(job_id):
    job_info = bifrost_instance.make_request(HttpMethods.GET, job_id)
    if job_info.status_code != 200:
        raise ValueError(f"Error fetching job info. Status code: {job_info.status_code}")
    return job_info


def get_availability(payload):
    endpoint = "availability/v2"
    return bifrost_instance.make_request(HttpMethods.POST, endpoint, payload)
