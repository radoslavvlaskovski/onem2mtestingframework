"""

Class created to check if a given Resource Primtive ( Request / Response )
is syntactically correct, which includes:

1) All Mandatory Parameters are contained in the Resource

2) Every given Parameter is either a optional or a mandatory Parameter

3) None of the given Parameters belong to the Not Permitted for the given Resource

"""

import json
import time
from Mappings import Resources


class SyntaxTests:
    # Initialize Class either with the mandatory, optional and not permitted parameter lists

    def __init__(self, sender, primitive):

        self.sender = sender
        self.log = self.sender.Log
        self.primitive = primitive

    def __set_parameters(self,primitive ):

        self.primitive = primitive

########################################################################################################################

################################     TESTS FROM FILE     ###############################################################

########################################################################################################################


    def test_all_parameters_primitive_from_file(self, file_name):

        f = open(file_name)

        try:
            data_json = json.load(f)

            self.__test_mandatory("Local Test", data_json, 0)
            self.__test_if_parameters_exist("Local Test",data_json,0)
        except:
            print("\n Not a valid JSON! \n ")


    def test_mandatory_parameters_primitive_from_file(self, file_name):

        f = open(file_name)

        try:
            json_data = json.load(f)

            self.__test_mandatory("Local Test", json_data, 0)
        except:
            print("\n Not a valid JSON! \n ")


    def test_not_present_parameters_from_file(self,file_name):

        f = open(file_name)

        try:
            json_data = json.load(f)

            self.__test_not_present("Local Test",json_data,0)
        except:
            print("\n Not a valid JSON! \n ")

    def test_if_all_prameters_exist_from_file(self,file_name):

        f = open(file_name)

        try:
            json_data = json.load(f)

            self.__test_if_parameters_exist("Local Test",json_data,0)
        except:
            print("\n Not a valid JSON! \n ")



########################################################################################################################

################################     TESTS RESPONSE    #################################################################

########################################################################################################################

    def test_syntax_response(self, method, url, data_json={}):

        req_time = time.time()
        headers, content = self.__get_data(method, url=url, data_json=data_json)

        res_time = time.time() - req_time

        exp_list = list()
        rcv_list = list()

        exp, rcv = self.__test_mandatory(headers, content)
        exp_list += exp
        rcv_list += rcv
        exp, rcv = self.__test_if_parameters_exist(url, headers, content, res_time)
        exp_list += exp
        rcv_list += rcv
        exp, rcv = self.__test_not_present(url, headers, content,res_time)
        exp_list += exp
        rcv_list += rcv

        return self.log.save_syntax_test("Syntax Test", url, exp_list, rcv_list, res_time)



########################################################################################################################

################################     TESTS FROM JSON   #################################################################

########################################################################################################################

    def __test_mandatory(self, headers, content):

        exp_content_list = list()
        rcv_content_list = list()

        if len(content) > 0:
            exp_content_list, rcv_content_list = self.__test_mandatory_content(headers)

        exp_headers_list, rcv_headers_list = self.__test_mandatory_headers(headers)

        return exp_content_list + exp_headers_list, rcv_content_list + rcv_headers_list


    def __test_not_present(self, url, headers, content, res_time):

        exp_content_list = list()
        rcv_content_list = list()

        if len(content) > 0:
            exp_content_list, rcv_content_list = self.__test_not_present_content(url, content, res_time)

        exp_headers_list, rcv_headers_list = self.__test_not_present_headers(url, headers, res_time)

        return exp_content_list + exp_headers_list, rcv_content_list + rcv_headers_list

    def __test_if_parameters_exist(self, url, headers, content, res_time):

        exp_content_list = list()
        rcv_content_list = list()

        if len(content) > 0:
            exp_content_list, rcv_content_list = self.__test_if_parameters_exist_content(url, content, res_time)

        exp_headers_list, rcv_headers_list = self.__test_if_parameters_exist_headers(url, headers, res_time)

        return exp_content_list + exp_headers_list, rcv_content_list + rcv_headers_list

    def __test_mandatory_content(self, content):

        exp_list = list()
        rec_list = list()

        for parameter in self.primitive.content_M:
            is_given = self.__search_parameter(content, parameter)

            expected = "Mandatory Parameter: " + parameter + " given: " + str(True)
            received = "Mandatory Parameter: " + parameter + " given: " + str(is_given)

            exp_list.append(expected)
            rec_list.append(received)

        return exp_list, rec_list

    def __test_mandatory_headers(self, headers):

        exp_list = list()
        rec_list = list()

        for parameter in self.primitive.header_M:
            is_given = self.__search_parameter(headers, parameter)

            expected = "Mandatory Parameter: " + parameter + " given: " + str(True)
            received = "Mandatory Parameter: " + parameter + " given: " + str(is_given)

            exp_list.append(expected)
            rec_list.append(received)

        return exp_list, rec_list

    def __test_not_present_content(self, url, content, res_time):

        exp_list = list()
        rec_list = list()

        for parameter in self.primitive.content_NP:
            is_given = self.__search_parameter(content, parameter)

            expected = "Not Permitted Parameter: " + parameter + " given: " + str(False)
            received = "Not Permitted Parameter: " + parameter + " given: " + str(is_given)

            exp_list.append(expected)
            rec_list.append(received)

        return exp_list, rec_list

    def __test_not_present_headers(self, url, headers, res_time):

        exp_list = list()
        rec_list = list()

        for parameter in self.primitive.header_NP:
            is_given = self.__search_parameter(headers, parameter)

            expected = "Not Permitted Parameter: " + parameter + " given: " + str(False)
            received = "Not Permitted Parameter: " + parameter + " given: " + str(is_given)

            exp_list.append(expected)
            rec_list.append(received)

        return exp_list, rec_list

    # Check all parameters

    def __test_if_parameters_exist_content(self, url, content, res_time):

        resource_type, parameters = self.__get_parameters(content)
        resource = Resources.find_resource(resource_type)
        exp_list = list()
        rec_list = list()

        try:
            for parameter in parameters.keys():

                if parameter not in self.primitive.content_M:
                    exists = self.__check_parameter_content(parameter, resource)

                    expected = "Optional Parameter: " + parameter + " exists"
                    if exists:
                        received = "Optional Parameter: " + parameter + " exists"
                    else:
                        received = "Optional Parameter: " + parameter + " does not exist"

                    exp_list.append(expected)
                    rec_list.append(received)

            return exp_list, rec_list
        except:
            print("\n No Content in Response \n")
            return list(), list()

    def __test_if_parameters_exist_headers(self, url, headers, res_time):

        header_ps = self.__get_relative_parameters_from_headers(headers)

        exp_list = list()
        rec_list = list()

        for parameter in header_ps:

            if parameter not in self.primitive.header_M:
                exists = self.__check_parameter_headers(parameter)

                expected = "Optional Parameter: " + parameter + " exists"
                if exists:
                    received = "Optional Parameter: " + parameter + " exists"
                else:
                    received = "Optional Parameter: " + parameter + " does not exist"

                exp_list.append(expected)
                rec_list.append(received)

        return exp_list, rec_list


########################################################################################################################

###################################     HELPER FUNCTIONS   #############################################################

########################################################################################################################

    def __search_parameter(self, json_data, parameter):

        is_given = False

        for key in json_data.keys():

            if key == parameter:
                is_given = True

        return is_given

    def __check_parameter_content(self, response_parameter, resource):

        exists = False

        for parameter in resource.get_attributes():

            if response_parameter == parameter :
                exists = True

        return exists

    def __check_parameter_headers(self, response_parameter):

        exists = False

        for parameter in self.primitive.header_O:

            if response_parameter == parameter:
                exists = True

        return exists


    def __get_parameters(self, data_json):

        for key in data_json.keys():
            return key, data_json[key]

    def __get_data(self, method, url, data_json):

        if method == "create":
            sc, headers, data_json = self.sender.send_create_request(url, data_json)
        elif method == "retrieve" or method == "get":
            sc, headers, data_json = self.sender.send_retrieve_request(url)
        elif method == "update":
            sc, headers, data_json = self.sender.send_update_request(url, data_json)
        elif method == "delete":
            sc, headers, data_json = self.sender.send_delete_request(url)

        return headers, data_json

    def __get_relative_parameters_from_headers(self, headers):

        relative_ps = []
        for p in headers.keys():

            if 'x-m2m-' in p:
                relative_ps.append(p)

        return relative_ps


