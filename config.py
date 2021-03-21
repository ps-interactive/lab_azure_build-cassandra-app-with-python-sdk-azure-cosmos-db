#!/usr/bin/env python
'''Configure credentials from the environment'''
import os

print("Configuring credentials from the environment...")

config = {
    'port': '10350',
    'username': 'testing-terraform',
    'password': os.environ['PRIMARY_MASTER_KEY'],
    'contactPoint': os.environ['DOCUMENT_ENDPOINT'],
}

print("Configuration complete!")
