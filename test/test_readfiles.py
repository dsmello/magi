import unittest
import os
import yaml
import dataclasses
import tempfile
from magi.readfiles import hello, list_files, load_file, __read_yaml__, read_yaml_files, is_folder, empty_folder, __clean_str__

FOLDER: str     = f"{os.path.dirname(__file__)}/mock"
CASE0: str      = f"{FOLDER}/case_0"
CASE1: str      = f"{FOLDER}/alpha"
CASE1_BAD: str  = f"{FOLDER}/alpha/world.txt"



class TestFileTool(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "world")

    def test_is_folder(self):
        self.assertEqual(is_folder(CASE1), CASE1)
        with self.assertRaises(IOError):
            is_folder(CASE1_BAD)

    def test__clean_str__(self):
        self.assertEqual(__clean_str__(CASE1, FOLDER), 'alpha')
        self.assertIsInstance(__clean_str__(CASE1, FOLDER), str)

    def test_list_files(self):
        self.assertIsInstance(list_files(CASE1), dict)
        self.assertEqual(len(list_files(CASE1)), 5)
        self.assertTrue(all([isinstance(file, str) for file in list_files(CASE1)]))

        with self.assertRaises(IOError):
            list_files(f"{CASE1_BAD}")


    def test_empty_folder(self):
        with tempfile.TemporaryDirectory('case-0') as CASE0:
            self.assertFalse(empty_folder(CASE0))

    def test_load_file(self):
        self.assertIsInstance(load_file(f"{CASE0}/helloworld.txt"), str)
        self.assertEqual(load_file(f"{CASE0}/helloworld.txt"), "Hello I'm Here")
        with self.assertRaises(FileNotFoundError):
            load_file(f"{CASE0}/nortfound.error")

    def test__read_yaml__(self):
        self.assertIsInstance(__read_yaml__(f"{CASE1}/mock_test_1.yaml"), dict)
        self.assertEqual(__read_yaml__(f"{CASE0}/mock_test_0.yaml")['hello'], "world")
        with self.assertRaises(yaml.YAMLError):
            __read_yaml__(f"{CASE0}/mock_test_0_bad.yaml")

    def test_read_yaml_files(self):
        self.assertIsInstance(read_yaml_files(f"{CASE1}/"), dict)
        self.assertTrue(read_yaml_files(f"{CASE1}/").get('mock_test_5'))
        self.assertAlmostEqual(len(read_yaml_files(f"{CASE1}/")), 5)

