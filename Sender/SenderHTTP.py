"""

Class that sends a request
to a given url and returns the
Response

"""
import json
import requests
try:
    import xmltodict
except:
    print("USING XML DISABLED XMLTODICT NOT FOUND")
from etc import Logger


class SenderHTTP:

    def __init__(self):
        self.Log = Logger.Logger()

    def send_create_request(self, url, data):

        if( isinstance(data, dict)):
            headers = {'Content-Type': 'application/json'}
            json_data = json.dumps(data)
            res = requests.post(url, data=json_data, headers=headers)

            try:
                return res.status_code, res.headers, res.json()

            except:
                return res.status_code, res.headers, {}

        else:
            headers = {'Content-Type': 'application/xml'}
            res = requests.post(url, data=data, headers=headers)

            try:
                content = res.content
                content = xmltodict.parse(content)
                return res.status_code, res.headers, content

            except:
                return res.status_code, res.headers, {}

    def send_retrieve_request(self, url):

        res = requests.get(url)

        try:
            return res.status_code, res.headers, res.json()

        except:
            try:
                content = res.content
                content = xmltodict.parse(content)
                return res.status_code, res.headers, content
            except:
                return res.status_code, res.headers, {}


    def send_update_request(self, url, data):

        if (isinstance(data, dict)):
            headers = {'Content-Type': 'application/json'}
            json_data = json.dumps(data)
            res = requests.put(url, data=json_data, headers=headers)

            try:
                return res.status_code, res.headers, res.json()

            except:
                return res.status_code, res.headers, {}

        else:
            headers = {'Content-Type': 'application/xml'}
            res = requests.put(url, data=data, headers=headers)

            try:
                content = res.content
                content = xmltodict.parse(content)
                return res.status_code, res.headers, content

            except:
                return res.status_code, res.headers, {}

    def send_delete_request(self, url):

        res = requests.delete(url)

        try:
            return res.status_code, res.headers, res.json()

        except:
            try:
                content = res.content
                content = xmltodict.parse(content)
                return res.status_code, res.headers, content
            except:
                return res.status_code, res.headers, {}



