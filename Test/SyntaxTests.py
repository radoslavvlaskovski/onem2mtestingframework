"""

Syntax tests that check a primitive
if it is written in compliance with the OneM2M standard

"""
from Mappings import BasicPrimitives
from Mappings import Resources

class SyntaxTests:
    # Initialize Class either with the mandatory, optional and not permitted parameter lists

    def __init__(self, Log):

        self.log = Log
        self.primitive = BasicPrimitives.request_primitive_create

    def set_primitive_create(self):
        self.primitive = BasicPrimitives.request_primitive_create

    def set_primitive_delete(self):
        self.primitive = BasicPrimitives.request_primitive_delete

    def set_primitive_update(self):
        self.primitive = BasicPrimitives.request_primitive_update

    def set_primitive_response(self):
        self.primitive = BasicPrimitives.response_primitive

    def set_primitive_retrieve(self):
        self.primitive = BasicPrimitives.request_primitive_retrieve

    def test_json(self, data_json):

        url = "Local Test"
        res_time = 0

        exp_list = list()
        rcv_list = list()

        exp, rcv = self.__test_mandatory(data_json)
        exp_list += exp
        rcv_list += rcv
        exp, rcv = self.__test_not_present(data_json)
        exp_list += exp
        rcv_list += rcv
        exp, rcv = self.__test_content(data_json)
        exp_list += exp
        rcv_list += rcv

        return self.log.save_syntax_test("Syntax Test", url, exp_list, rcv_list, res_time)

    def __test_mandatory(self, data_json):
        exp_list = list()
        rec_list = list()

        for parameter in self.primitive.M:
            is_given = self.__search_parameter(data_json, parameter)

            expected = "Mandatory Parameter: " + parameter + " given: " + str(True)
            received = "Mandatory Parameter: " + parameter + " given: " + str(is_given)

            exp_list.append(expected)
            rec_list.append(received)

        return exp_list, rec_list

    def __test_not_present(self, data_json):
        exp_list = list()
        rec_list = list()

        for parameter in self.primitive.NP:
            is_given = self.__search_parameter(data_json, parameter)

            expected = "Not Permitted Parameter: " + parameter + " given: " + str(False)
            received = "Not Permitted Parameter: " + parameter + " given: " + str(is_given)

            exp_list.append(expected)
            rec_list.append(received)

        return exp_list, rec_list

    def __test_content(self, data_json):
        resource_type, parameters = self.__get_parameters(data_json)
        resource = Resources.find_resource(resource_type)

        exp_list = list()
        rec_list = list()

        try:
            for parameter in parameters.keys():

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

########################################################################################################################

###################################     HELPER FUNCTIONS   #############################################################

########################################################################################################################

    def __search_parameter(self, json_data, parameter):

            is_given = False

            for key in json_data.keys():

                if key == parameter:
                    is_given = True

            return is_given

    def __get_parameters(self, data_json):

        try:
            pc = data_json["pc"]

            for resource_type in pc.keys():
                return resource_type, pc[resource_type]

        except:
            return "",{}

    def __check_parameter_content(self, response_parameter, resource):

        exists = False

        for parameter in resource.get_attributes():

            if response_parameter == parameter:
                exists = True

        return exists
