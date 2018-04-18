from resident_sync.models import Resident


class BaseSource:
    """
    TODO: may be I should make base classes for API, CSV and screen scrapping
          but I have no idea would each source will have some common code or it will be unique
    """
    def __init__(self, property_id):
        pass

    def get_residents(self):
        return [Resident() for x in xrange(10)]
