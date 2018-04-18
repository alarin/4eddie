from resident_sync.models import Property
from resident_sync.sources.base_source import BaseSource


@app.task
def update_properties_residents():
    """
    For each property from settings.property_sources create update_property_residents task
    Called daily by celery.schedules

    :return:
    """
    pass


@app.task
def update_property_residents(property_id, source):
    """
    :param property_id:
    :param source: property source class path
    :return:
    """
    property = Property(property_id)
    source = BaseSource() #load source class from file
    residents = source.get_residents()
    new_residents = property.update_residents(residents)
    for resident in new_residents:
        greet_resident.s(resident.email, resident).apply_async()



@app.task
def greet_resident(email, first_name):
    """
    Send greetins by email for new resident
    """
    pass

