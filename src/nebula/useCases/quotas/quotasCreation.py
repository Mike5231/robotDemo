from typing import List

from src.bifrost.libraries.jobs import get_availability
from src.nebula.libraries.capacity import create_capacity
from src.bifrost.data.jobsMock import create_availability_payload
from src.nebula.data.capacityMock import create_capacity_payload


class Resources:
    def __init__(self, resource_id: str, fleet_id: str):
        self.resource_id = resource_id
        self.fleet_id = fleet_id


def setup_quotas(client_id: str, resources: List[Resources]):
    availability_payload = create_availability_payload(client_id)
    availability = get_availability(availability_payload)
    if availability.status_code > 400 or not availability.data:
        for resource in resources:
            capacity_payload = create_capacity_payload(
                resource_id=resource.resource_id,
                fleet_id=resource.fleet_id
            )
            capacity_response = create_capacity(capacity_payload)
            if capacity_response.status_code > 400:
                raise ValueError(f"Error creating capacity. Status code: {capacity_response.status_code}, Error message: {capacity_response.data}")
