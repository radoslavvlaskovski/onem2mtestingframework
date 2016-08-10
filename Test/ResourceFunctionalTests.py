"""

Functional tests for specific resources

Each test expects a certain Status Code that is in compliance with the 
OneM2M standard

"""

class ResourceFunctionalTests:

    def __init__(self, functional_tester):
        self.functional_tester = functional_tester


    def test_csebase_create(self, url, json):
        self.functional_tester.test_create_request_from_json(url, json, 4005, "Attempt to CREATE CSEBase")

    def test_csebase_update(self, url, json):
        self.functional_tester.test_update_request_from_json(url, json, 4005, "Attempt to UPDATE CSEBase")

    def test_csebase_delete(self, url):
        self.functional_tester.test_delete_request(url, 4005, "Attempt to DELETE CSEBase")

    def test_contentInstance_update(self, url, json):
        self.functional_tester.test_update_request_from_json(url, json, 4005, "Attempt to DELETE CSEBase") 


    def test_resource_create(self, url, json):
        self.functional_tester.test_create_request_from_json(url, json, 4005, "Attempt to CREATE CSEBase")

    def test_resource_update(self, url, json):
        self.functional_tester.test_update_request_from_json(url, json, 4005, "Attempt to UPDATE CSEBase")

    def test_resource_delete(self, url):
        self.functional_tester.test_delete_request(url, 4005, "Attempt to DELETE CSEBase")
