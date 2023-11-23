import requests


def get_job_info(job_id):
    url = 'https://nebula.vormir.instaleap.io/jobs/' + job_id
    headers = {
        'Authorization': 'Bearer 78MVg7iwxs6De7rUI2gNmTheL5MXRC4o'
    }
    response = get_request(url, headers)
    return response


def get_request(url, headers):
    response = requests.get(url, headers=headers)
    return response
