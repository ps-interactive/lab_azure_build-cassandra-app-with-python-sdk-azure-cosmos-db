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

print("Counting records ...")

total = session.execute("SELECT COUNT(*) FROM candidates.records").one()
t = PrettyTable(['Total'])
t.add_row([total.system_count])
print(t)
