"""

Class created to Log Tests
Three types of logging exist:
1) Syntax
2) Behaviour
3) Simple

"""

# TODO : Create a Support for behaviour tests consisting of more than one test

import time
import os


class Logger:
    def __init__(self):
        self.test_counter = 0
        self.tests_passed_counter = 0
        self.id = str(time.time())
        self.log_file = "Logs/" + "testlog" + self.id + ".txt"
        self.start_test_log()
        self.printer = False
        self.tests = []


    def start_test_log(self):
        f = open(self.log_file, "a")
        f.write("\n\n" + "########################################################################################\n"
                + "Starting Test " + time.strftime("%c") + "\n" +
                "########################################################################################\n\n\n")
        f.close()

    def save_test(self, test_description, conn_url, expected, received, res_time):
        self.test_counter += 1

        output = self.generate_output(test_description, conn_url, expected, received, res_time)
        self.write_test_tofile(output)
        self.write_test_to_console(output)

        return output

    def save_behaviour_test(self, test_description, urls, expected, received, res_time):
        self.test_counter +=1
        test_id = self.id + str(self.test_counter)

        output = "\n STARTING BEHAVIOUR TEST \n\n"
        output += "Test ID: " + test_id + "\n\n"
        passed = True

        for i in range(0, len(test_description)):
            output += self.generate_output_behaviour(test_description[i], expected[i], received[i], urls[i])

        for i in range(0, len(expected)):
            if expected[i] != received[i]:
                passed = False

        if passed:
            passed = "Success"
            self.tests_passed_counter += 1
        else:
            passed = "Failed"

        output += "Test Result: " + passed + "\n\n" + \
                  "BEHAVIOR TEST DONE IN : " + str(res_time)

        self.write_test_to_console(output)
        self.write_test_tofile(output)

        return output

    def save_syntax_test(self, test_description, url, expected, received, res_time):
        self.test_counter +=1
        test_id = self.id + str(self.test_counter)

        output = "\n STARTING SYNTAX TEST \n\n"
        output += "Test ID: " + test_id +"\n\n"

        output += self.generate_output_syntax(url, expected, received, res_time, test_description)
        self.write_test_tofile(output)
        self.write_test_to_console(output)

        return output

    def save_parameters_test(self, url, parameters, expected, received, res_time):

        self.test_counter += 1
        test_id = self.id + str(self.test_counter)

        output = "\n STARTING PRAMETERS TEST \n\n"
        output += "Test ID: " + test_id + "\n\n"

        output += self.generate_output_parameters(url, parameters, expected, received, res_time)
        self.write_test_tofile(output)
        self.write_test_to_console(output)

        return output

    def generate_output_parameters(self, url, parameters, expected, received, res_time):
        res_time = round(res_time, 3)
        passed = True

        output = "Test " + str(self.test_counter) + "\n" \
                 + "Test time: " + time.strftime("%c") + "\n" \
                 + "Test description " + "parameter testing" + " for url: " + url + "\n\n"

        for i in range(0, len(expected)):
            if passed:
                passed = received[i] == expected[i]
            output += "Paramter: " + parameters[i] + "\n"
            output += "Received: " + received[i] + "\n" + "Expected: " + expected[i] + "\n" + "\n"

        if passed:
            self.tests_passed_counter += 1
            passed = "Success"
        else:
            passed = "Failed"

        output += "Test Result: " + str(passed) + "\n" + "\n" \
                  + "Response Time: " + str(res_time) + " secs" + "\n"

        output += "\n" + "\n"

        return output

    def generate_output_syntax(self, url, expected, received, res_time, test_description):
        res_time = round(res_time, 3)
        passed = True

        output = "Test " + str(self.test_counter) + "\n" \
                 + "Test time: " + time.strftime("%c") + "\n" \
                 + "Test description " + test_description + " for url: " + url + "\n\n"

        for i in range(0, len(expected)):
            if passed:
                passed = received[i] == expected[i]
            output += "Received: " + received[i] + "\n" + "Expected: " + expected[i] + "\n" + "\n" \

        if passed:
            self.tests_passed_counter += 1
            passed = "Success"
        else:
            passed = "Failed"

        output += "Test Result: " + str(passed) + "\n" + "\n" \
                  + "Response Time: " + str(res_time) + " secs" + "\n"

        output += "\n" + "\n"

        return output

    def generate_output_behaviour(self, test_description, expected, received, url):
        passed = expected == received

        if passed:
            passed = "Success"
        else:
            passed = "Failed"

        output = "Test description: " + test_description + "\n" \
                 + "URL used: " + url + "\n" \
                 + "Test Result: " + passed + "\n" \
                 + "Received: " + received + "\n" + "Expected: " + expected + "\n\n"

        return output

    def generate_output(self, test_description, conn_url, expected, received, res_time):
        res_time = round(res_time, 3)
        passed = expected == received

        if passed:
            passed = "Success"
        else:
            passed = "Failed"

        test_id = str(time.time()) + str(self.test_counter)

        output = "Test " + str(self.test_counter) + "\n" \
                 + "Test id: " + test_id + "\n" \
                 + "Test time: " + time.strftime("%c") + "\n" \
                 + "Test description " + test_description + " for url: " + conn_url + "\n" \
                 + "Test Result: " + str(passed) + "\n" + "\n" \
                 + "Received: " + received + "\n" + "Expected: " + expected + "\n" + "\n" \
                 + "Response Time: " + str(res_time) + " secs" + "\n"

        if passed:
            self.tests_passed_counter += 1

        output += "\n" + "\n"

        return output

    def write_test_tofile(self, output):

        f = open(self.log_file, "a")
        f.write(output)
        f.close()

    def write_test_to_console(self, output):

        if self.printer:
            print(output)

    def end_test_log(self):
        f = open(self.log_file, "a")
        f.write("\n\n" + "########################################################################################\n"
                + "Ending Tests " + time.strftime("%c") + "\n"
                + "Passed tests: " + str(self.tests_passed_counter) + "/" + str(self.test_counter) + "\n"
                                                                                                     "########################################################################################\n\n\n")
        print("\n\n" + "########################################################################################\n"
                + "Ending Tests " + time.strftime("%c") + " Log ID : " + self.id +"\n"
                + "Passed tests: " + str(self.tests_passed_counter) + "/" + str(self.test_counter) + "\n"
                                                                                                     "########################################################################################\n\n\n")
        f.close()

    def __del__(self):
        self.end_test_log()
