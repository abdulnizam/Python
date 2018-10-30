#!/usr/bin/python3

import os
import sys
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/lib')
from sql import *
from core import *

conn = sqlite3.connect('nexus.db')

def create_new_user(length: int):
    fetch_users = fetch_user()
    create_users(conn, fetch_users)

def update_user_password(data: list):
    update_Password(conn, data)

if __name__ == '__main__':

    password = generate_password(8, 2)
    # # # print(password)
    # # # print(check_password_level(password))
    # # fetch_users = fetch_user()
    # # fetch_users['password'] = password
    # # print(fetch_users)
    # print(password)
    update_data = ['1', password]
    # update_user_password(update_data)
    # print(select_User_By_Id(conn, '1'))
    # create_table(conn)
    # create_new_user(10)


    # # create_users(conn, fetch_users)
    # # print(fetch_users)
    # # create_table()

    # # insert_table()
    print(select_table(conn))


# conn.close()
