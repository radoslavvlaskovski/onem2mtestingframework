"""
Class representing a Resource
from the OneM2M standard
"""

attributes_all = ["ct", "lbl", "lt", "lnk", "pi", "ri", "ty", "rn"]


class Resource:
    def __init__(self, attributes, resource_short_name):
        self.attributes = attributes
        self.short_name = resource_short_name

        for attr in attributes_all:
            self.attributes.append(attr)

    def get_attributes(self):
        return self.attributes

    def get_short_name(self):
        return self.short_name
