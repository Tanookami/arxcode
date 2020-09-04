"""
The descriptionshandler is an abstraction layer to fetch descriptions for
objects while hiding data storage. The original implementation of descs
used Evennia attributes, which denormalized data. Using an abstraction layer
both allows for caching, and hiding data storage for ease of refactoring.
"""
#import


class DescriptiveTrait:
    """Wrapper for description, will later be replaced by a model"""
    def __init__(self, name, value):
        self.name = name
        self.value = value


class DescriptionsHandler:
    """
    Handler that instantiates with item, which will then store the instance
    as a cached property on the item.
    """
    def __init__(self, item):
        self.item = item

    def get_desc_value(self, name: str) -> str:
        return self.item.attributes.get(name, "")

    def set_desc_value(self, name: str, value: str):
        self.item.attributes.add(name, value)

    #myriad properties for Rooms, Characters, and Items
    #Characters

    #Rooms
    #spring_desc
    #summer_desc
    #autumn_desc
    #winter_desc
    #general_desc - used as a fallback if a seasonal one is not set
    #raw_desc - set dynamically. Can contain raw timeslot codes
    #desc - set dynamically at first look. Parsed for timeslot codes
    #last_season - will be filled later
    #last_timeslot - will be filled later

    @property
    def details(self):
        "detail storage"
        return self.item.db.details

    #setter

    @property
    def room_mood(self):
        return self.item.db.room_mood

    @room_mood.setter
    def room_mood(self, value):
        pass
