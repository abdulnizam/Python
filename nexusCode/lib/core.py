#!/usr/bin/python3

import random
import sqlite3
import string
import re
import requests
import json
import sys

def generate_password(length: int, complexity: int) -> str:
    password = ''
    switcher = {
        1: "",
        2: "0123456789",
        3: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        4: "[ !#$%&'()*+,-./[\\\]^_`{|}~",
    }
    chars = 'abcdefghijklmnopqrstuvwxyz' + switcher.get(complexity)

    for x in range(length):
        password += random.choice(chars)
    return password


def check_password_level(password: str) -> int:
    try:
        level = 1
        length_error = len(password) >= 8
        digit_error = re.search(r"\d", password) is None
        uppercase_error = re.search(r"[A-Z]", password) is None
        lowercase_error = re.search(r"[a-z]", password) is None
        punctuation_error = re.search(
            r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]',
            password) is None
        if not punctuation_error:
            level = 4
        elif uppercase_error == False:
            level = 3
        elif digit_error == False:
            level = 2
        else:
            level = 1
        if not length_error:
            raise

        return level
    except BaseException:
        if level == 2:
            message = 'password length should be 8 chars and only lowercase chars'
        elif level == 3:
            message = 'password length should be 8 chars and only lowercase and digits'
        else:
            message = 'password length should be 8 chars'

        return message


def fetch_user() -> dict:
    try:
        resp = requests.get("https://randomuser.me/api/")
        if resp.status_code == 200:
            response = json.loads(resp.text)
            results = response['results'][0]
            data = {
                "full_name": "%s. %s %s" % (results['name']['title'],
                                            results['name']['first'],
                                            results['name']['last']),
                "email": results['email'],
                "password": results['login']['password']
            }

        else:
            resp.raise_for_status()
        return data
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
