#!/usr/bin/python3

import unittest
import os.path
import sys
import sqlite3

dir_path = os.path.abspath(os.path.join(os.pardir))
sys.path.append(dir_path + '/lib')
from core import *

class NexuscodeTest(unittest.TestCase):

    def testLength(self):
        password = generate_password(8, 2)
        self.assertEqual(len(password), 8)

    def testComplexityLevel4(self):
        password = generate_password(8, 4)
        level = check_password_level(password)
        self.assertEqual(level, 4)

    def testComplexityLevel3(self):
        password = generate_password(8, 3)
        level = check_password_level(password)
        self.assertEqual(level, 3)

    def testComplexityLevel2(self):
        password = generate_password(8, 2)
        level = check_password_level(password)
        self.assertEqual(level, 2)

    def testComplexityLevel1(self):
        password = generate_password(8, 1)
        level = check_password_level(password)
        self.assertEqual(level, 1)

    def testError1(self):
        password = generate_password(6, 1)
        level = check_password_level(password)
        self.assertEqual(level, 'password length should be 8 chars')

    def testError2(self):
        password = generate_password(6, 2)
        level = check_password_level(password)
        self.assertEqual(
            level, 'password length should be 8 chars and only lowercase chars')

    def testError3(self):
        password = generate_password(6, 3)
        level = check_password_level(password)
        self.assertEqual(
            level,
            'password length should be 8 chars and only lowercase and digits')

    def testFetchUsers(self):
        level = fetch_user()
        self.assertEqual(type(level), dict)


if __name__ == "__main__":
    unittest.main()
