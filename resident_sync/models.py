class Resident:
    property_id = None
    flat = None
    first_name = None
    last_name = None
    email = None  # I suppose email would be nice for primary key

    def __init__(self, property_id, flat, first_name, last_name, email):
        pass

    def save(self):
        '''
        save to database
        '''
        pass


class Property:
    property_id = None

    flats = []
    residents = []

    def __init__(self):
        pass

    def update_residents(self, residents):
        """
        Removes absent residents, update residents info in database.
        (use resident email as primary key)

        May be I'm optimistic about quality of data of different sources and this should customizable in each source

        :param residents: parsed residents list
        :return: list of new residents
        """
        pass

