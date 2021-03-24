#!/usr/bin/env python
'''Count records by gender'''
from cassandra.auth import PlainTextAuthProvider
from prettytable import PrettyTable
from cassandra.cluster import Cluster
from ssl import PROTOCOL_TLSv1_2, SSLContext, CERT_NONE
import config as cfg

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE
auth_provider = PlainTextAuthProvider(username=cfg.config['username'], password=cfg.config['password'])
cluster = Cluster([cfg.config['contactPoint']], port=cfg.config['port'], auth_provider=auth_provider, ssl_context=ssl_context)
session = cluster.connect()

report = {}
sexes = ['M', 'F']

print("Counting records by gender ...")

total = session.execute("SELECT COUNT(*) FROM customers.records").one()
t = PrettyTable(['Male', 'Female', 'Total'])

for sex in sexes:
    count = session.execute("SELECT COUNT(*) FROM customers.records WHERE sex = '{}'".format(sex)).one()
    report[sex] = count.system_count

t.add_row([report['M'], report['F'], total.system_count])
print(t)
