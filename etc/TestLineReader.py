""" 

Class that executes tests from commands

"""
from etc import ParameterChecking as checker, TestFileReader as filereader, messages


class TestLineReader:
    def __init__(self, functional_tester, syntax_tester,
                 behaviour_tester, syntax_json_tester, parameter_functional_tester):

        self.functional_tester = functional_tester
        self.syntax_tester = syntax_tester
        self.behaviour_tester = behaviour_tester
        self.syntax_json_tester = syntax_json_tester
        self.parameter_functional_tester = parameter_functional_tester

    def args_read(self, args):
        if len(args) > 0:

########################################################################################################################
##################################     Functional Tests   ##############################################################
########################################################################################################################

            test_type = args[0]

            if test_type == "create":

                if len(args) < 4:
                    print(
                    "\nCreate test format: create <url> <expected response code> <file/json> [test description]\n")

                else:
                    url = args[1]
                    expected = args[2]
                    data = args[3]
                    data = checker.check_parameters(url, expected, data)

                    if isinstance(data, str):
                        print("\n" + data + "\n")
                    else:
                        self.functional_tester.test_create_request_from_json(url, data, expected)

            elif test_type == "update":

                if len(args) < 4:
                    print(
                    "\nUpdate test format: update <url> <expected response code> <file/json> [test description]\n")

                else:
                    url = args[1]
                    expected = args[2]
                    data = args[3]
                    data = checker.check_parameters(url, expected, data)

                    if isinstance(data, str):
                        print("\n" + data + "\n")
                    else:
                        self.functional_tester.test_update_request_from_json(url, data, expected)

            elif test_type == "retrieve" or test_type == "get":

                if len(args) < 3:
                    print("\nRetrieve test format: retrieve <url> <expected response code> [test description]\n")

                else:
                    url = args[1]
                    expected = args[2]
                    result = checker.check_parameters_simple(url, expected)

                    if isinstance(result, str):
                        print("\n" + result + "\n")
                    else:
                        self.functional_tester.test_retrieve_request(url, expected)

            elif test_type == "delete":

                if len(args) < 3:
                    print(
                    "\nDelete test format: delete <url> <expected response code> <file/json> [test description] \n")

                else:
                    url = args[1]
                    expected = args[2]
                    result = checker.check_parameters_simple(url, expected)

                    if isinstance(result, str):
                        print("\n" + result + "\n")
                    else:
                        self.functional_tester.test_delete_request(args[1], args[2])

            elif test_type == "parameter":
                if len(args) < 4:
                    print(
                    "\nParameter from response checker test format : paramter console <url;> <parameter to check>"
                    " <expected value of parameter> [json] or "
                    "Parameter from response checker test format : paramter file <url>\n")

                else:
                    method_type = args[1]

                    if method_type == "console":

                        if len(args) < 4:
                            print(
                            "\nParameter from response checker test format : paramter console <url> "
                            "<expected paramater> <expected value of parameter> \n")

                        else:
                            url = args[2]
                            parameter_value = args[3]

                            if parameter_value.count("=") == 1:
                                parameter, value = parameter_value.split("=")
                                result = checker.check_url(url)

                                if result == False:
                                    print("\n" + result + "\n")
                                else:
                                    self.parameter_functional_tester.check_attribute_retrieve(url, parameter, value)
                            else:
                                print("\n Parameter Value format is wrong: <parameter>=<value> \n")

                    if method_type == "file":

                        if len(args) < 4:
                            print("\nParameter from response checker test format : paramter file <url> <file name>  \n")
                        else:
                            url = args[2]
                            file_name = args[3]

                            expected, values = filereader.read_parameters_test_file(file_name)

                            self.parameter_functional_tester.check_attributes_retrieve(url, expected, values)



########################################################################################################################
######################################     Syntax Tests   ##############################################################
########################################################################################################################

            elif test_type == "syntax":

                if len(args) >= 4:

                    syntax_test_type = args[1]

                    if syntax_test_type == "response":
                        method = args[2].lower()

                        if method == "create" or method == "update":

                            if len(args) == 5:
                                url = args[3]
                                data = args[4]
                                data = checker.check_parameters(url, "2000", data)

                                if isinstance(data, str):
                                    print("\n" + data + "\n")
                                else:
                                    self.syntax_tester.test_syntax_response(method, url, data)
                            else:
                                print("\nSyntax response test format:"
                                      " syntax response [create|update] <method> <url> <json>\n")

                        elif method == "retrieve" or method == "get" or method == "delete":

                            if len(args) == 4:
                                url = args[3]
                                result = checker.check_url(url)

                                if not result:
                                    print("\n" + "Wrong URL" + "\n")
                                else:
                                    self.syntax_tester.test_syntax_response(method, url)
                            else:
                                print("\nSyntax response test format:"
                                      " syntax response [retrieve|get|delete] <method> <url>\n")

                        else:
                            print("\nSyntax response test format:"
                                  " syntax response [create|update|retrieve|get|delete] <method> <url> [json]\n")

                    if syntax_test_type == "json":

                        instance_type = args[2]

                        if instance_type == "create":
                            self.syntax_json_tester.set_primitive_create()
                            data = args[3]
                            data = checker.check_data(data)
                            self.syntax_json_tester.test_json(data)

                        elif instance_type == "retrieve":
                            self.syntax_json_tester.set_primitive_retrieve()
                            data = args[3]
                            data = checker.check_data(data)
                            self.syntax_json_tester.test_json(data)

                        elif instance_type == "update":
                            self.syntax_json_tester.set_primitive_update()
                            data = args[3]
                            data = checker.check_data(data)
                            self.syntax_json_tester.test_json(data)

                        elif instance_type == "delete":
                            self.syntax_json_tester.set_primitive_delete()
                            data = args[3]
                            data = checker.check_data(data)
                            self.syntax_json_tester.test_json(data)

                        elif instance_type == "response":
                            self.syntax_json_tester.set_primitive_response()
                            data = args[3]
                            data = checker.check_data(data)
                            self.syntax_json_tester.test_json(data)

                        else:
                            print("\nWRONG FORMAT\n")

                else:
                    print("\nSyntax test format: syntax <response | json> [method] [url] [json]\n")

########################################################################################################################
###################################     Behaviour Tests   ##############################################################
########################################################################################################################

            elif test_type == "behaviour":

                if len(args) >= 2:

                    behaviour_type = args[1]

                    if behaviour_type == "cc":

                        if len(args) == 4:
                            url = args[2]
                            data = args[3]

                            self.behaviour_tester.test_create_create(url, data)

                        else:
                            print("\nBehaviour Create Create test: "
                                  "behaviour cc <url> <json>\n")

                    if behaviour_type == "cd":

                        if len(args) == 5:
                            url = args[2]
                            data = checker.check_data(args[3])
                            url2 = args[4]

                            if checker.check_url(url) and checker.check_url(url2) and data != False:
                                urls = list()
                                urls.append(url)
                                urls.append(url2)
                                self.behaviour_tester.test_create_delete(urls, data)

                        else:
                            print("\nBehaviour Create Delete test: "
                                  "behaviour cd <url> <json> <url2>\n")

                    if behaviour_type == "crd":

                        if len(args) == 5:

                            url = args[2]
                            data = checker.check_data(args[3])
                            url2 = args[4]

                            if checker.check_url(url) and checker.check_url(url2) and data != False:
                                urls = list()
                                urls.append(url)
                                urls.append(url2)
                                self.behaviour_tester.test_create_retrieve_delete(urls, data)

                            else:
                                if data == False:
                                    print("\n No json file with that name exists\n")
                                else:
                                    print("\n One of the urlsnot correct! \n")

                        else:
                            print("\nBehaviour Create Retrieve Delete test: "
                                  "behaviour crd <url_create> <json> <url retrieve|delete> \n")

                    if behaviour_type == "cdd":

                        if len(args) == 5:

                            url = args[2]
                            data = checker.check_data(args[3])
                            url2 = args[4]

                            if checker.check_url(url) and checker.check_url(url2) and data != False:
                                urls = list()
                                urls.append(url)
                                urls.append(url2)
                                self.behaviour_tester.test_create_delete_delete(urls, data)

                            else:
                                print("\n Either url or json not correct! \n")

                        else:
                            print("\nBehaviour Create Delete Delete test: "
                                  "behaviour cgd <url_create> <json> <url delete|delete> n")

                    if behaviour_type == "cdr":

                        if len(args) == 5:

                            url = args[2]
                            data = checker.check_data(args[3])
                            url2 = args[4]

                            if checker.check_url(url) and checker.check_url(url2) and data != False:
                                urls = list()
                                urls.append(url)
                                urls.append(url2)
                                self.behaviour_tester.test_create_retrieve_delete(urls, data)

                            else:
                                print("\n Either url or json not correct! \n")

                        else:
                            print("\nBehaviour Create Retrieve Delete test: "
                                  "behaviour cgd <url_create> <json> <url retrieve|delete> \n")

                    if behaviour_type == "custom":

                        if len(args) == 3:
                            file_name = args[2]
                            methods, urls, expected, jsons = filereader.read_behaviour_test_file(file_name)
                            self.behaviour_tester._test_behaviour(urls, jsons, methods, expected)
                        else:
                            print("\nBehaviour test custom : behaviour custom <test file>\n")

                else:
                    print("\n Behaviour tests shoud be in the format : behaviour <type> [needed arguments]\n")

