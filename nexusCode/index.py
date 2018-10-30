#!/usr/bin/python3

import os
import sys
import sqlite3
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/lib')
from sql import *
from core import *

conn = sqlite3.connect('nexus.db')


def create_users(count: int):
    for x in range(1, count):
        length, complex_level = generate_random_data()
        # generate password using random length and complex level
        password = generate_password(length, complex_level)

        fetch_users = fetch_user()
        # creating new password for each users
        fetch_users['password'] = password
        # creating new user one by one
        create_new_users(conn, fetch_users)


def select_all_users():
    users = select_table(conn)
    return users


def update_user_password(data: list):
    update_Password(conn, data)


def generate_random_data() -> list:
    return [random.randint(8, 12), random.randint(1, 4)]


if __name__ == '__main__':

    create_table(conn)  # create table

    create_users(10)  # create users

    print(select_all_users())  # print all users

    # update password
    length, complex_level = generate_random_data()
    password = generate_password(length, complex_level)
    update_data = ['1', password]
    update_user_password(update_data)
