"""

Class representing a primitive
with its mandatory, optional and not permitted parameters

"""

from Mappings import PrimitiveParameters as parameters

class Primitive:
    def __init__(self, M, NP, primitive_parameters):
        self.M = M
        self.NP = NP
        self.O = []
        self.primitive_parameters = primitive_parameters
        self.convert_tags_to_parameters()

    def convert_tags_to_parameters(self):

        mandatory = []
        optional = []
        not_present = []

        for i in range(0, len(self.M)):
            mandatory.append(parameters.map_long_to_short_primitive_parameters[self.primitive_parameters[self.M[i]]])

        for i in range(0, len(self.primitive_parameters)):
            if not (self.M.__contains__(i) or
                        self.NP.__contains__(i)):
                optional.append(parameters.map_long_to_short_primitive_parameters[self.primitive_parameters[i]])

        for i in range(0, len(self.NP)):
            not_present.append(parameters.map_long_to_short_primitive_parameters[self.primitive_parameters[self.NP[i]]])

        self.M = mandatory
        self.O = optional
        self.NP = not_present


