from resident_sync.models import Resident
from resident_sync.sources.base_source import BaseSource


class ResidenceSource(BaseSource):
    def __init__(self, property_id):
        pass

    def get_residents(self):
        return [Resident() for x in xrange(10)]
