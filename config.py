#!/usr/bin/env python
'''Configure credentials from the environment'''
import os

print("Configuring credentials from the environment...")

config = {
    'port': '10350',
    'username': os.environ['DB_USERNAME'],
    'password': os.environ['DB_PASSWORD'],
    'contactPoint': os.environ['DB_HOSTNAME']
}

print("Configuration complete!")
