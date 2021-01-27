import os
import unittest
from magi.sys_env import replace_by_sys_variables


class Test_sys_env(unittest.TestCase):

    def test_replace_by_sys_variables(self):
        CASE : dict = {
            "test": {
                "user": "hello",
                "pass": "pass"
            }
        }

        CASE_out : dict = {
            "test": {
                "user": "test",
                "pass": "test_Pass0rd"
            }
        }

        os.environ["MAGI_YAML_TEST_USER"] = CASE_out["test"]["user"]
        os.environ["MAGI_YAML_TEST_PASS"] = CASE_out["test"]["pass"]

        
        self.assertIsNone(replace_by_sys_variables(CASE.copy()))
        
        replace_by_sys_variables(CASE.copy())
        self.assertIsInstance(CASE, dict)
        self.assertEqual(CASE, CASE_out)
