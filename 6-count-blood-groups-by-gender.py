#!/usr/bin/env python
'''Create the keyspace and table'''
from cassandra.auth import PlainTextAuthProvider
from prettytable import PrettyTable
from cassandra.cluster import Cluster
from ssl import PROTOCOL_TLSv1_2, SSLContext, CERT_NONE
import config as cfg

def PrintTable(rows, keys):
    t = PrettyTable(['ID','Name', 'Sex', 'Blood Group', 'SSN'])
    for r in rows:
        t.add_row([r.id, r.name, r.sex, r.blood_group, r.ssn])
    print(t)



keys = ['id', 'address', 'blood_group', 'company', 'job', 'mail', 'name', 'residence', 'sex', 'ssn', 'username']

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE
auth_provider = PlainTextAuthProvider(username=cfg.config['username'], password=cfg.config['password'])
cluster = Cluster([cfg.config['contactPoint']], port=cfg.config['port'], auth_provider=auth_provider, ssl_context=ssl_context)
session = cluster.connect()

blood_groups = ['A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
sexes        = ['M','F']

print("Testing blood group queries....")

for group in blood_groups:
    for sex in sexes:
        print("Blood_Group = '{1}'; Sex = '{0}'".format(sex, group))
        count = session.execute("SELECT COUNT(*) FROM customers.gender WHERE sex = '{}' and  blood_group = '{}'".format(sex, group)).one()
        rows = session.execute("SELECT * FROM customers.gender WHERE sex = '{}' and  blood_group = '{}' LIMIT 5".format(sex, group))
        print("Records found: {}".format(count.system_count))
        PrintTable(rows, keys)
        print()
        print()
