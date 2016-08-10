"""

Class that will represent the Basic primitives
that can be later modified for the specific resource type cases

"""

from Mappings import Primitive

request_primitive_parameters = \
    ["Operation","To","From","Request Identifier","Resource Type","Content","Role","Originating Timestamp",
     "Request Expiration Timestamp","Result Expiration Time","Operation Execution Time",
     "Response Type","Result Persistence","Result Content","Event Category","Delivery Aggregation",
     "Group Request Identifier","Filter Criteria","Discovery Result Type"]

request_primitive_create = Primitive.Primitive([0, 1, 2, 3, 4, 5], [17, 18], request_primitive_parameters)

request_primitive_retrieve = Primitive.Primitive([0, 1, 2, 3], [4], request_primitive_parameters)

request_primitive_update = Primitive.Primitive([0, 1, 2, 3, 5], [4, 18], request_primitive_parameters)

request_primitive_delete = Primitive.Primitive([0, 1, 2, 3], [4, 5, 18], request_primitive_parameters)

response_primitive_parameters = \
    ["Response Status Code","Request Identifier","Content","To","From","Originating Timestamp",
     "Result Expiration Timestamp","Event Category"]

response_primitive= Primitive.Primitive([0, 1], [], response_primitive_parameters)