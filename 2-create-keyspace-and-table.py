#!/usr/bin/env python
'''Create the keyspace and table'''
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from ssl import PROTOCOL_TLSv1_2, SSLContext, CERT_NONE
import config as cfg


keys = ['id', 'address', 'blood_group', 'company', 'job', 'mail', 'name', 'residence', 'sex', 'ssn', 'username']

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE
auth_provider = PlainTextAuthProvider(username=cfg.config['username'], password=cfg.config['password'])
cluster = Cluster([cfg.config['contactPoint']], port=cfg.config['port'], auth_provider=auth_provider, ssl_context=ssl_context)
session = cluster.connect()

print("\nCreating Keyspace 'candidates' ...")
session.execute('CREATE KEYSPACE IF NOT EXISTS candidates WITH replication = {\'class\': \'NetworkTopologyStrategy\', \'datacenter\' : \'1\' }')

print("\nCreating Table 'records' with PRIMARY KEY (id) ...")
session.execute('CREATE TABLE IF NOT EXISTS candidates.records (id int, job text, company text, ssn text, residence text, blood_group text, username text, name text, sex text, address text, mail text, PRIMARY KEY (id))')

print("\nCreating Table 'gender' with PRIMARY KEY (sex) ...")
session.execute('CREATE TABLE IF NOT EXISTS candidates.gender (id int, job text, company text, ssn text, residence text, blood_group text, username text, name text, sex text, address text, mail text, PRIMARY KEY ((sex), blood_group, residence))')

print("\nCreating Table 'blood_groups' with PRIMARY KEY (blood_group) ...")
session.execute('CREATE TABLE IF NOT EXISTS candidates.blood_group (id int, job text, company text, ssn text, residence text, blood_group text, username text, name text, sex text, address text, mail text, PRIMARY KEY ((blood_group), sex, residence))')
