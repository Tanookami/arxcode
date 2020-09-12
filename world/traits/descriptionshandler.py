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
    @property
    def spring_desc(self):
        return self.item.db.spring_desc

    @property
    def summer_desc(self):
        return self.item.db.summer_desc

    @property
    def autumn_desc(self):
        return self.item.db.autumn_desc

    @property
    def winter_desc(self):
        return self.item.db.winter_desc

    @property
    def general_desc(self):
        "used as a fallback if a seasonal one is not set"
        return self.item.db.general_desc

    @property
    def raw_desc(self):
        "set dynamically. Can contain raw timeslot codes"
        return self.item.db.raw_desc

    @property
    def desc(self):
        "set dynamically at first look. Parsed for timeslot codes"
        return self.item.db.desc

    @property
    def last_season(self):
        "will be filled later"
        return self.item.db.last_season

    @property
    def last_timeslot(self):
        "will be filled later"
        return self.item.db.last_timeslot

    @property
    def details(self):
        "detail storage"
        if not self.item.db.details:
            self.item.db.details = {}
        return self.item.db.details

    #setter?

    @property
    def room_mood(self):
        return self.item.db.room_mood

    @room_mood.setter
    def room_mood(self, value):
        pass


