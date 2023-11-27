from robot.api.deco import keyword
from src.bifrost.libraries.BifrostBaseLibrary import BifrostBase
from src.utils.http import HttpMethods


class JobRequests(BifrostBase):

    @keyword
    def get_job(self, job_id):
        endpoint = f"jobs/{job_id}"
        return self.make_request(HttpMethods.GET, endpoint)
