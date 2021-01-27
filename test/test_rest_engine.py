import unittest
import responses
import requests
import os
from magi.rest_engine import rest_call

# Project Magi dependencies
from magi.nodesolver import  nodesolver
from magi.readfiles import read_yaml_files
from magi.rest_engine import rest_call



FOLDER: str = f"{os.path.dirname(__file__)}/mock"
CASE1: str = read_yaml_files(f"{FOLDER}/alpha")
YAML: str = CASE1["mock_test_1"]
request_list : list = nodesolver(YAML)


TEST_CASE_1_1 = {
    "method": "GET",
    "url": "http://mock.site.localhost/dummy",
    "status": 200
}

TEST_CASE_1_2 = {
    "method": "GET",
    "url": "http://mock.site.localhost/dummy_2",
    "status": 200
}

class Test_rest_engine(unittest.TestCase):
    
    @responses.activate
    def test_rest_call(self):
        status_code: int = 200
        # Using request Lib
        responses.add(**TEST_CASE_1_1)
        responses.add(**TEST_CASE_1_2)

        for rest_request in request_list:
            print(rest_request["url"])
            self.assertEqual(status_code, rest_call(**rest_request))
            