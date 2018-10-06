#!/usr/bin/env python

import environ

env = environ.Env()

# reading .env file
environ.Env.read_env()

print(env('HOST'))