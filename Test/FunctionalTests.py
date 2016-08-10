"""

Class for doing functional Tests

Send a request and check the response
after that save the test 

"""

import json
import time

from Mappings import StatusCodes

class FunctionalTests:
    def __init__(self, sender):
        self.sender = sender
        self.log = sender.Log
        self.status_codes = StatusCodes.status_codes_m2m

########################################################################################################################

################################     TEST CUSTOM REQUEST AND CHECK STATUS   ############################################

########################################################################################################################

    def test_create_request_from_file(self, url, file_name, expected, test_name="Custom Test"):
        f = open(file_name)

        self.test_create_request_from_json(url,f,expected,test_name)

    def test_update_request_from_file(self, url, file_name, expected, test_name="Custom Test"):
        f = open(file_name)

        try:
            json_data = json.load(f)
        except:
            print("\n Test could not be run because the string is not a valid JSON String! \n")
            return

        self.test_update_request_from_json(url, json_data, expected, test_name)

    def test_create_request_from_json(self, url, json_data, response_expected, test_name="Custom Test"):

        exp = self._generate_response_code(response_expected)

        t = time.time()
        http_sc, headers, data = self.sender.send_create_request(url, json_data)
        res_time = time.time() - t

        rcv= self._generate_response_code(headers['x-m2m-rsc'],int(http_sc))

        return self.log.save_test(test_name, url, exp, rcv, res_time)

    def test_update_request_from_json(self, url, json_data, response_expected, test_name="Custom Test"):

        exp = self._generate_response_code(response_expected)

        t = time.time()
        http_sc, headers, data = self.sender.send_update_request(url, json_data)
        res_time = time.time() - t

        rcv = self._generate_response_code(headers['x-m2m-rsc'], int(http_sc))

        return self.log.save_test(test_name, url, exp, rcv, res_time)


    def test_retrieve_request(self,url,expected,test_name="Custom Test"):

        exp = self._generate_response_code(expected)

        t = time.time()
        http_sc, headers, data = self.sender.send_retrieve_request(url)
        res_time = time.time() - t

        rcv = self._generate_response_code(headers['x-m2m-rsc'],int(http_sc))

        return self.log.save_test(test_name, url, exp, rcv, res_time)

    def test_delete_request(self,url,expected,test_name="Custom Test"):

        exp = self._generate_response_code(expected)

        t = time.time()
        http_sc, headers, data = self.sender.send_delete_request(url)
        res_time = time.time() - t

        rcv = self._generate_response_code(headers['x-m2m-rsc'],int(http_sc))

        return self.log.save_test(test_name, url, exp, rcv, res_time)


########################################################################################################################

#########################################     HELPER FUNCTIONS   #######################################################

########################################################################################################################


    def _generate_response_code(self,sc,http_code = 0):

        status_code,status = StatusCodes.map_status_input(sc)

        if http_code == 0:
            http_code = StatusCodes.map_m2m_to_http(status_code)

        return "Response Status Code: " + str(status_code) + " " + status + " HTTP: " + str(http_code)
