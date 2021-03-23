from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from ssl import PROTOCOL_TLSv1_2, SSLContext, CERT_NONE
from faker import Faker
import config as cfg
import json


keys = ['id', 'address', 'blood_group', 'company', 'job', 'mail', 'name', 'residence', 'sex', 'ssn', 'username']

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE
auth_provider = PlainTextAuthProvider(username=cfg.config['username'], password=cfg.config['password'])
cluster = Cluster([cfg.config['contactPoint']], port=cfg.config['port'], auth_provider=auth_provider, ssl_context=ssl_context)
session = cluster.connect()

print("\nCreating Keyspace")
session.execute('CREATE KEYSPACE IF NOT EXISTS customers WITH replication = {\'class\': \'NetworkTopologyStrategy\', \'datacenter\' : \'1\' }')

print("\nCreating Table")
session.execute('CREATE TABLE IF NOT EXISTS customers.records (id int PRIMARY KEY, job text, company text, ssn text, residence text, blood_group text, username text, name text, sex text, address text, mail text)')

print("\nGenerating Data...")
fake = Faker()
for record_id in range(3000):
    record = {'id': record_id}
    record.update(fake.profile(fields=keys))
    session.execute("INSERT INTO uprofile.withuuidv44 JSON '{}'".format(json.dumps(record).replace("'", "")))
    print(json.dumps(record).replace("'", ""))
