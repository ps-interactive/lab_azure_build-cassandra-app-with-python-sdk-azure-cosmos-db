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

print("\nGenerating Data...")
fake = Faker()
for record_id in range(3000):
    record = {'id': record_id}
    record.update(fake.profile(fields=keys))
    session.execute("INSERT INTO customers.records JSON '{}'".format(json.dumps(record).replace("'", "")))
    session.execute("INSERT INTO customers.gender JSON '{}'".format(json.dumps(record).replace("'", "")))
    session.execute("INSERT INTO customers.blood_group JSON '{}'".format(json.dumps(record).replace("'", "")))
    print(json.dumps(record).replace("'", ""))
