"""

Class for doing Behaviour Testing

How it will work:

1) Sends a couple of requests one after another
2) Saves the responses
3) Checks if all responses are as expected

"""
import time
from Mappings import StatusCodes


class BehaviorTests:
    def __init__(self, sender):

        self.sender = sender
        self.Log = sender.Log

    def test_create_create(self, url, json_request):

        expected_results = list()
        expected_results.append("2001")
        expected_results.append("4105")

        json_requests = list()
        json_requests.append(json_request)
        json_requests.append(json_request)

        methods = list()
        methods.append("create")
        methods.append("create")

        urls = list()
        urls.append(url)
        urls.append(url)

        return self._test_behaviour(urls, json_requests, methods, expected_results)

    def test_create_retrieve_delete(self, urls, json_request):

        if len(urls) == 2:
            urls.append(urls[1])

        expected_results = list()
        expected_results.append("2001")
        expected_results.append("2000")
        expected_results.append("2000")

        json_requests = list()
        json_requests.append(json_request)
        json_requests.append({})
        json_requests.append({})

        methods = list()
        methods.append("create")
        methods.append("get")
        methods.append("delete")

        return self._test_behaviour(urls, json_requests, methods, expected_results)

    def test_create_delete(self, urls, json_request):

        expected_results = list()
        expected_results.append("2001")
        expected_results.append("2000")

        json_requests = list()
        json_requests.append(json_request)
        json_requests.append({})

        methods = list()
        methods.append("create")
        methods.append("delete")

        return self._test_behaviour(urls, json_requests, methods, expected_results)

    def test_create_delete_delete(self, urls, json_request):

        if len(urls) == 2:
            urls.append(urls[1])

        expected_results = list()
        expected_results.append("2001")
        expected_results.append("2000")
        expected_results.append("4004")

        json_requests = list()
        json_requests.append(json_request)
        json_requests.append({})
        json_requests.append({})

        methods = list()
        methods.append("create")
        methods.append("delete")
        methods.append("delete")

        return self._test_behaviour(urls, json_requests, methods, expected_results)

    def test_create_delete_get(self, urls, json_request):

        if len(urls) == 2:
            urls.append(urls[1])

        expected_results = list()
        expected_results.append("2001")
        expected_results.append("2000")
        expected_results.append("4004")

        json_requests = list()
        json_requests.append(json_request)
        json_requests.append({})
        json_requests.append({})

        methods = list()
        methods.append("create")
        methods.append("delete")
        methods.append("get")

        return self._test_behaviour(urls, json_requests, methods, expected_results)

    def test_create_retrieve_update_retrieve_delete(self, urls, json_requests):
        if len(urls) == 2 and len(json_requests) == 2:
            urls.append(urls[1])
            urls.append(urls[1])
            urls.append(urls[1])

        else:
            print("\nFALSE TEST FORMAT\n")
            return

        expected_results = list()
        expected_results.append("2001")
        expected_results.append("2000")
        expected_results.append("2000")
        expected_results.append("2000")
        expected_results.append("2000")

        json_requests = list()
        json_requests.append(json_requests[0])
        json_requests.append({})
        json_requests.append(json_requests[1])
        json_requests.append({})
        json_requests.append({})

        methods = list()
        methods.append("create")
        methods.append("get")
        methods.append("update")
        methods.append("get")
        methods.append("delete")

        return self._test_behaviour(urls, json_requests, methods, expected_results)

    def test_create_update_retrieve_delete(self, urls, json_requests):
        if len(urls) == 2 and len(json_requests) == 2:
            urls.append(urls[1])
            urls.append(urls[1])

        else:
            print("\nFALSE TEST FORMAT\n")
            return

        expected_results = list()
        expected_results.append("2001")
        expected_results.append("2000")
        expected_results.append("2000")
        expected_results.append("2000")

        json_requests = list()
        json_requests.append(json_requests[0])
        json_requests.append(json_requests[1])
        json_requests.append({})
        json_requests.append({})

        methods = list()
        methods.append("create")
        methods.append("update")
        methods.append("get")
        methods.append("delete")

        return self._test_behaviour(urls, json_requests, methods, expected_results)

    def test_create_delete_update(self, urls, json_requests):
        if len(urls) == 2 and len(json_requests) == 2:
            urls.append(urls[1])

        else:
            print("\nFALSE TEST FORMAT\n")
            return

        expected_results = list()
        expected_results.append("2001")
        expected_results.append("2000")
        expected_results.append("4004")

        json_requests = list()
        json_requests.append(json_requests[0])
        json_requests.append({})
        json_requests.append(json_requests[1])

        methods = list()
        methods.append("create")
        methods.append("delete")
        methods.append("update")

        return self._test_behaviour(urls, json_requests, methods, expected_results)

    ########################################################################################################################

    #########################################     HELPER FUNCTIONS   #######################################################

    ########################################################################################################################

    def _test_behaviour(self, urls, json_requests, methods, expected_results, test_descriptions=list()):

        if len(test_descriptions) < len(expected_results):

            for i in range(len(test_descriptions), len(expected_results)):
                test_descriptions.append("")

        req_time = time.time()
        received = list()
        test_descriptions = methods

        for i in range(0, len(json_requests)):

            sc, header, data = self._get_data(urls[i], json_requests[i], methods[i])

            try:
                received.append(header['x-m2m-rsc'])
            except:
                received.append("No rsc provided!")

        res_time = time.time() - req_time

        return self.Log.save_behaviour_test(test_descriptions, urls, expected_results, received, res_time)

    def _get_data(self, url, json, method):

        if method == "create":
            return self.sender.send_create_request(url, json)
        elif method == "update":
            return self.sender.send_update_request(url, json)
        elif method == "get" or method == "retrieve":
            return self.sender.send_retrieve_request(url)
        elif method == "delete":
            return self.sender.send_delete_request(url)

    def _generate_response_code(self, sc, http_code=0):

        status_code, status = StatusCodes.map_status_input(sc)

        if http_code == 0:
            http_code = StatusCodes.map_m2m_to_http(status_code)

        return "Response Status Code: " + str(status_code) + " " + status + " HTTP: " + str(http_code)
