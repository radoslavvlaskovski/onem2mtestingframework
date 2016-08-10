"""

Impelements tests that 

1) Send a request, receive response

2) Check if a specified parameter has a certain value

"""

import time


class ResponseParameterTests:
    def __init__(self, sender):

        self.sender = sender
        self.log = sender.Log

    def check_attributes_retrieve(self, url, parameters, values):

        if len(parameters) != len(values):
            print("Testing failed: \n The number of parameters must be equal to the number of values \n\n")
            return

        t = time.time()
        headers, content = self.__get_data("retrieve", url)
        res_time = time.time() - t
        res_values = list()

        for i in range(0, len(parameters)):
            res_value = self._get_parameter_value(parameters[i], content)
            res_value = str(res_value)

            res_values.append(res_value)

        return self.log.save_parameters_test(url, parameters, values, res_values, res_time)

    def check_attribute_retrieve(self, url, parameter, value):

        t = time.time()
        headers, content = self.__get_data("retrieve", url)
        res_time = time.time() - t

        res_value = self._get_parameter_value(parameter, content)

        if res_value == None:
            return self.log.save_test("Check attribute " + parameter, url, value, "No such parameter found", res_time)
        else:
            return self.log.save_test("Check attribute " + parameter, url, value, res_value, res_time)


########################################################################################################################

###################################     HELPER FUNCTIONS   #############################################################

########################################################################################################################

    def _get_parameter_value(self, parameter, content):

        for resource_type in content.keys():

            for key in content[resource_type].keys():

                if key == parameter:
                    return content[resource_type][key]

        return None

    def __get_data(self, method, url, data_json={}):

        headers = {}

        if method == "create":
            sc, headers, data_json = self.sender.send_create_request(url, data_json)
        elif method == "retrieve" or method == "get":
            sc, headers, data_json = self.sender.send_retrieve_request(url)
        elif method == "update":
            sc, headers, data_json = self.sender.send_update_request(url, data_json)
        elif method == "delete":
            sc, headers, data_json = self.sender.send_delete_request(url)

        return headers, data_json
