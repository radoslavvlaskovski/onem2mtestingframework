""" 

Module implements functions to

1) read a test file and return the arguments

2) read a custom behaviour test file and return the tests

3) read a file for a custom number of paramters functional test

"""

from etc import ParameterChecking as checker


def read_test_file(file, reader):
    file = open("testfiles/" + file, "r")
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        args = line.split(" ")
        reader.args_read(args)

    file.close()

    return lines


def read_parameters_test_file(file_name):
    file = open("functional_parameters_checking/" + file_name, "r")
    lines = file.readlines()

    parameters = list()
    values = list()

    for line in lines:
        line = line.strip()
        args = line.split(" ")

        for i in range(0, len(args)):
            parameter_value = args[i]

            if parameter_value.count("=") == 1:
                par, value = parameter_value.split("=")

                parameters.append(par)
                values.append(value)
            else:
                print("\n Parameter Value format is wrong: <parameter>=<value> \n")
                
    file.close()

    return parameters, values


def read_behaviour_test_file(file):
    file = open("behaviour_custom_tests/" + file, "r")
    lines = file.readlines()
    urls = list()
    expected_stats = list()
    json_requests = list()
    methods = list()

    for line in lines:
        line = line.strip()
        args = line.split(" ")

        if len(args) == 4:
            method = args[0]
            url = args[1]
            expected = args[2]
            json = args[3]

            data = checker.check_parameters(url, expected, json)

            if isinstance(data, str):
                print("\n" + data + "\n")
            else:
                methods.append(method)
                urls.append(url)
                expected_stats.append(expected)
                json_requests.append(data)

        elif len(args) == 3:

            method = args[0]
            url = args[1]
            expected = args[2]

            check = checker.check_parameters_simple(url, expected)

            if check == False:
                print("\n" + check + "\n")
            else:
                methods.append(method)
                urls.append(url)
                expected_stats.append(expected)
                json_requests.append({})

        else:
            print("\n Line format : <method> <url> <expected status code> [json]\n")

    file.close()
    return methods, urls, expected_stats, json_requests
