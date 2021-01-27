import os
import unittest
from magi.nodesolver import  __get_basic_info__, __get_requests__, __metadata_auth__, __metadata__, __inject_basic_info__, __sort_requests__
from magi.readfiles import read_yaml_files


FOLDER: str     = f"{os.path.dirname(__file__)}/mock"
CASE1: str = read_yaml_files(f"{FOLDER}/alpha")

class Test_nodesolver(unittest.TestCase):

    def test__get_basic_info__(self): 
        YAML: dict = CASE1.get("mock_test_1")

        result: dict = {
            'auth':
            {'basic': 
                {'password': 'mock_pass', 'user': 'mock_user'}},
            'url':'http://mock.site.localhost'}

        self.assertIsInstance(YAML, dict, "The Yaml must be a 'dict' instance")
        self.assertIsInstance(__get_basic_info__(raw_input=YAML.copy(), sys_env_replacer=False), dict, "The method must return 'dict' instance")
        self.assertEqual(__get_basic_info__(raw_input=YAML.copy(), sys_env_replacer=False), result, "The method must return the espect content.")


    def test__metadata_auth__(self):
        YAML: dict = CASE1.get("mock_test_1")

        result: dict = {
            "auth": ("mock_user", "mock_pass")
        }

        self.assertIsInstance(__metadata_auth__(YAML), dict, "The method must return 'dict' instance")
        self.assertEqual(__metadata_auth__(YAML.get("metadata")), result, "The method must return the espect content.")


    def test__get_requests__(self): 
        YAML: dict = CASE1.get("mock_test_1")

        result: dict = {
            "test_default": [ {"url": "/dummy"},{"url": "/dummy_2"}]
        }

        self.assertIsInstance(YAML, dict, "The Yaml must be a 'dict' instance")
        self.assertIsInstance(__get_requests__(YAML), dict, "The method must return 'dict' instance")
        self.assertEqual(__get_requests__(YAML), result, "The method must return the espect content.")


    def test__metadata__(self):
        YAML: dict = CASE1.get("mock_test_1")

        result: dict = {
            "url": "http://mock.site.localhost",
            "auth": ("mock_user", "mock_pass")
        }

        self.assertIsInstance(__metadata__(YAML), dict, "The method must return 'dict' instance")
        self.assertEqual(__metadata__(YAML), result, "The method must return the espect content.")


    def test__inject_basic_info__(self): 
        YAML: dict = CASE1.get("mock_test_1")

        result: dict = {
            "test_default": [ {
                "url": "http://mock.site.localhost/dummy",
                "auth": ("mock_user", "mock_pass"),
                "method": "GET"
            },
            {
                "url": "http://mock.site.localhost/dummy_2",
                "auth": ("mock_user", "mock_pass"),
                "method": "GET"
            }]
        }

        self.assertIsInstance(__inject_basic_info__(__metadata__(YAML), __get_requests__(YAML)), dict, "The method must return 'dict' instance")
        self.assertEqual(__inject_basic_info__(__metadata__(YAML), __get_requests__(YAML)), result, "The method must return the espect content.")

    
