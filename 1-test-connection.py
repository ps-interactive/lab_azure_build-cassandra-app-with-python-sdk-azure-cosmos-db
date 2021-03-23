#!/usr/bin/env python
'''Test connection'''
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from ssl import PROTOCOL_TLSv1_2, SSLContext, CERT_NONE
import config as cfg

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE
auth_provider = PlainTextAuthProvider(username=cfg.config['username'], password=cfg.config['password'])
cluster = Cluster([cfg.config['contactPoint']], port=cfg.config['port'], auth_provider=auth_provider, ssl_context=ssl_context)

try:
    session = cluster.connect()
    print("Connection test was successful!")
except:
    print("ERROR: Connection was not established.")
    print("Please review the environment variables with the following commands:")
    print("    echo $DB_HOSTNAME")
    print("    echo $DB_USERNAME")
    print("    echo $DB_PASSWORD")
    print()
    print("Run the environment configuraiton step with the following command:")
    print("    source 0-set-cosmosdb-environment.sh")
    print()
    print("If the environment configuration has already been run and ")
    print("the connection still fails, try setting the environment manually")
    print("with the folling steps:")
    print("1. Open the Azure Cosmos DB console for the Cassandra DB you created")
    print("2. Open the 'Connection String' panel")
    print("3. Note these values: CONTACT POINT, USERNAME, PRIMARY PASSWORD")
    print("4. In the Cloud Shell, use the Connection String values in the following exports:")
    print("      export DB_HOSTNAME=CONTACT_POINT_VALUE")
    print("      export DB_USERNAME=USERNAME_VALUE")
    print("      export DB_PASSWORD=PASSWORD_VALUE")
    print("4. After exporting these values, rerun the connection test script")
    print("5. Note that if you needed to set these values manually, DO NOT RUN the 0-set-cosmosdb-environment.sh script")
