""" 

Module that craete from a simple Primitive
a HTTP primitive by applying the 
HTTP mapping described in the OneM2M standard

"""

m2m_parameters_to_header_parameters = {
    "fr": "x-m2m-origin",
    "rqi": "x-m2m-ri",
    "gid": "x-m2m-gid",
    "rt": "x-m2m-rtu",
    "ot": "x-m2m-ot",
    "rset": "x-m2m-rst",
    "rqet": "x-m2m-ret",
    "oet": "x-m2m-oet",
    "ec": "x-m2m-ec",
    "rsc": "x-m2m-rsc"
}


class PrimitiveHTTP:
    def __init__(self, primitive):

        self.primitive_onem2m = primitive
        self.short_m = primitive.M
        self.short_o = primitive.O
        self.short_np = primitive.NP

        self.header_M = []
        self.header_O = []
        self.header_NP = []

        self.content_M = []
        self.content_O = []
        self.content_NP = []
        self.map_onem2m_to_http()

    def map_onem2m_to_http(self):

        for m in self.short_m:

            if m in m2m_parameters_to_header_parameters.keys():
                self.header_M.append(m2m_parameters_to_header_parameters[m])
            else:
                self.content_M.append(m)

        for o in self.short_o:

            if o in m2m_parameters_to_header_parameters.keys():
                self.header_O.append(m2m_parameters_to_header_parameters[o])
            else:
                self.content_O.append(o)

        for np in self.short_np:

            if np in m2m_parameters_to_header_parameters.keys():
                self.header_NP.append(m2m_parameters_to_header_parameters[np])
            else:
                self.content_NP.append(np)
