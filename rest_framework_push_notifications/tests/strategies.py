from uuid import uuid4

from hypothesis.searchstrategy import BasicStrategy
from hypothesis.strategies import basic, booleans, fixed_dictionaries, text


class UUIDStrategy(BasicStrategy):
    def generate(self, random, parameter_value):
        return uuid4()


APNSDeviceData = fixed_dictionaries({
    'registration_id': text(min_size=1, max_size=64),
    'name': text(max_size=255),
    'device_id': basic(UUIDStrategy),
    'active': booleans(),
})
