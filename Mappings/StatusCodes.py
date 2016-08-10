"""

These are the Status Codes according to the :

OneM2M Service Layer Core Protocol Specification
Document Number: TS-0004-V1.6.0

"""

status_codes_m2m = {
    'ACCEPTED': 1000,

    'OK': 2000,
    'CREATED': 2001,
    'DELETED': 2002,
    'UPDATED': 2004,
    'CONTENT_EMPTY': 2100,

    'BAD_REQUEST': 4000,
    'NOT_FOUND': 4004,
    'OPERATION_NOT_ALLOWED': 4005,
    'REQUEST_TIMEOUT': 4008,
    'SUBSCRIPTION_CREATOR_HAS_NO_PRIVILEGE': 4101,
    'CONTENTS_UNACCEPTABLE': 4102,
    'ACCESS_DENIED': 4103,
    'GROUP_REQUEST_IDENTIFIER_EXISTS': 4104,
    'CONFLICT': 4105,

    'INTERNAL_SERVER_ERROR': 5000,
    'NOT_IMPLEMENTED': 5001,
    'TARGET_NOT_REACHABLE': 5103,
    'NO_PRIVILEGE': 5105,
    'ALREADY_EXISTS': 5106,
    'TARGET_NOT_SUBSCRIBABLE': 5203,
    'SUBSCRIPTION_VERIFICATION_INITIATION_FAILED': 5204,
    'SUBSCRIPTION_HOST_HAS_NO_PRIVILEGE': 5205,
    'NON_BLOCKING_REQUEST_NOT_SUPPORTED': 5206,
    'NOT_ACCEPTABLE': 5207,

    'EXTERNAL_OBJECT_NOT_REACHABLE': 6003,
    'EXTERNAL_OBJECT_NOT_FOUND': 6005,
    'MAX_NUMBER_OF_MEMBER_EXCEEDED': 6010,
    'MEMBER_TYPE_INCONSISTENT': 6011,
    'MGMT_SESSION_CANNOT_BE_ESTABLISHED': 6020,
    'MGMT_SESSION_ESTABLISHMENT_TIMEOUT': 6021,
    'INVALID_CMDTYPE': 6022,
    'INVALID_ARGUMENTS': 6023,
    'INSUFFICIENT_ARGUMENTS': 6024,
    'MGMT_CONVERSION_ERROR': 6025,
    'MGMT_CANCELLATION_FAILED': 6026,
    'ALREADY_COMPLETE': 6028,
    'MGMT_COMMAND_NOT_CANCELLABLE': 6029
}

status_codes_m2m_reverse = {
    1000: 'ACCEPTED',

    2000: 'OK',
    2001: 'CREATED',
    2002: 'DELETED',
    2004: 'UPDATED',
    2100: 'CONTENT_EMPTY',

    4000: 'BAD_REQUEST',
    4004: 'NOT_FOUND',
    4005: 'OPERATION_NOT_ALLOWED',
    4008: 'REQUEST_TIMEOUT',
    4101: 'SUBSCRIPTION_CREATOR_HAS_NO_PRIVILEGE',
    4102: 'CONTENTS_UNACCEPTABLE',
    4103: 'ACCESS_DENIED',
    4104: 'GROUP_REQUEST_IDENTIFIER_EXISTS',
    4105: 'CONFLICT',

    5000: 'INTERNAL_SERVER_ERROR',
    5001: 'NOT_IMPLEMENTED',
    5103: 'TARGET_NOT_REACHABLE',
    5105: 'NO_PRIVILEGE',
    5106: 'ALREADY_EXISTS',
    5203: 'TARGET_NOT_SUBSCRIBABLE',
    5204: 'SUBSCRIPTION_VERIFICATION_INITIATION_FAILED',
    5205: 'SUBSCRIPTION_HOST_HAS_NO_PRIVILEGE',
    5206: 'NON_BLOCKING_REQUEST_NOT_SUPPORTED',
    5207: 'NOT_ACCEPTABLE',

    6003: 'EXTERNAL_OBJECT_NOT_REACHABLE',
    6005: 'EXTERNAL_OBJECT_NOT_FOUND',
    6010: 'MAX_NUMBER_OF_MEMBER_EXCEEDED',
    6011: 'MEMBER_TYPE_INCONSISTENT',
    6020: 'MGMT_SESSION_CANNOT_BE_ESTABLISHED',
    6021: 'MGMT_SESSION_ESTABLISHMENT_TIMEOUT',
    6022: 'INVALID_CMDTYPE',
    6023: 'INVALID_ARGUMENTS',
    6024: 'INSUFFICIENT_ARGUMENTS',
    6025: 'MGMT_CONVERSION_ERROR',
    6026: 'MGMT_CANCELLATION_FAILED',
    6028: 'ALREADY_COMPLETE',
    6029: 'MGMT_COMMAND_NOT_CANCELLABLE'
}

status_m2m_to_http = {
    1000: 202,

    2000: 200,
    2001: 201,

    4000: 400,
    4004: 404,
    4005: 405,
    4008: 408,
    4101: 403,
    4102: 400,
    4103: 403,
    4104: 409,
    4105: 409,

    5000: 500,
    5001: 501,
    5103: 404,
    5105: 403,
    5106: 403,
    5203: 403,
    5204: 500,
    5205: 403,
    5206: 501,
    5207: 406,

    6003: 404,
    6005: 404,
    6010: 400,
    6011: 400,
    6020: 500,
    6021: 500,
    6022: 400,
    6023: 400,
    6024: 400,
    6025: 500,
    6026: 500,
    6028: 400,
    6029: 400
}


def map_status_input(status_input):
    if isinstance(status_input, int):

        if status_input >= 1000:
            return status_input, status_codes_m2m_reverse[status_input]

    if isinstance(status_input, str):

        try:
            status_code = int(status_input)

            if status_code >= 1000:
                return status_code, status_codes_m2m_reverse[status_code]
        except:
            status_code = status_codes_m2m[status_input]

        if status_code >= 1000:
            return status_code, status_input

    return


def map_m2m_to_http(status):
    if isinstance(status, int):
        return status_m2m_to_http[status]

    if isinstance(status, str):

        try:
            status = int(status)
            return status_m2m_to_http[status]
        except:
            return 0
