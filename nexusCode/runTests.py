#!/usr/bin/python

import unittest
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/lib')

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('tests', pattern='*.py')
    unittest.TextTestRunner().run(all_tests)
