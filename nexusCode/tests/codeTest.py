#!/usr/bin/python3

import unittest
import os.path
import sys
import sqlite3

# to run the test inside the test folder you may need to uncomment
# dir_path = os.path.abspath(os.path.join(os.pardir))
# sys.path.append(dir_path + '/lib')
from core import *
from sql import *
conn = sqlite3.connect('../nexus.db')


class NexuscodeTest(unittest.TestCase):

    def testFetchUsers(self):
        user = fetch_user()
        self.assertEqual(type(user), dict)

    def testCreateTable(self):
        user = fetch_user()
        ret = create_table(conn)
        self.assertEqual(ret, 'table created.')

    def testCreateUser(self):
        user = fetch_user()
        ret = create_new_users(conn, user)
        self.assertEqual(ret, None)

    def testUpdatePassword(self):
        password = generate_password(8, 2)
        update_data = ['1', password]
        update_Password(conn, update_data)
        user = select_User_By_Id(conn, '1')
        self.assertEqual(user[0]['password'], password)


if __name__ == "__main__":
    unittest.main()
    print(dir_path)
