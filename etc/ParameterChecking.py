""" 

Module implements checking of test inputs : 
Input types
1)  URL
2) JSON OR XML FILE
3) STATUS CODE

"""

try:
    import urllib.parse as parse
except ImportError:
    try:
        import urlparse as parse
    except:
        print("Python should be updated! \n\n")
import json
from Mappings import StatusCodes
import xml.etree.ElementTree as eTree

fails = {
    -1: "Not a valid URL Address",
    -2: "Not a valid Status Code",
    -3: "Not a valid JSON file",
    -4: "Not a valid JSON String"
}


########################################################################################################################

#########################################    URL STATUS CHECKER  #######################################################

########################################################################################################################

def check_url(url, qualifying=None):
    min_attributes = ('scheme', 'netloc')

    qualifying = min_attributes if qualifying is None else qualifying
    token = parse.urlparse(url)

    return all([getattr(token, qualifying_attr)
                for qualifying_attr in qualifying])


def check_response_code(expected):
    try:
        expected = int(expected)
    except:
        expected = expected

    if isinstance(expected, int):

        if expected >= 1000:

            if expected in StatusCodes.status_codes_m2m_reverse.keys():
                return True
            else:
                return False
        elif 0 <= expected < 1000:
            if expected in StatusCodes.status_m2m_to_http.items():
                return True
            else:
                return False
        else:
            return False

    elif isinstance(expected, str):
        if expected in StatusCodes.status_codes_m2m.keys():
            return True
        else:
            return False
    else:
        return False


########################################################################################################################

##############################################    DATA CHECKER   #######################################################

########################################################################################################################

def check_json_file(file_name):
    try:
        f = open("jsons_for_testing/" + file_name, "r")
        data = json.load(f)
        return data
    except:
        return False


def check_xml_file(data):
    try:
        data = eTree.parse(data).getroot()
        return data
    except:
        return False


def check_string(data):
    try:
        data = json.loads(data)
        return data
    except:
        try:
            eTree.fromstring(data)
            return data
        except:
            return False


def check_file(file_name):
    try:
        f = open("jsons_for_testing/" + file_name, "r")
        f.close()
        return True
    except:
        return False


def check_data(data):
    if check_file(data):
        if ".json" in data:
            return check_json_file(data)

        elif ".xml" in data:
            return check_xml_file(data)

    elif isinstance(data, dict):
        return data
    else:
        return check_string(data)


########################################################################################################################

##############################################    MAIN FUNCTIONS   #####################################################

########################################################################################################################


def check_parameters(url, expected, data):
    data = check_data(data)
    if check_url(url) is False:
        return fails[-1]
    elif check_response_code(expected) is False:
        return fails[-2]
    elif data is False:
        return fails[-3]
    else:
        return data


def check_parameters_simple(url, expected):
    if check_url(url) is False:
        return fails[-1]
    elif check_response_code(expected) is False:
        return fails[-2]
    else:
        return True
