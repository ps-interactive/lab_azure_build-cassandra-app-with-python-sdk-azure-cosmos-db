#!/usr/bin/env bash
RESOURCE_GROUP=$(az group list --query "[?contains(name, 'azure')].name" --output tsv)

if [ -z "${RESOURCE_GROUP}" ];
then
    echo "Please manually set the RESOURCE_GROUP environment variable:"
    echo "For example:"
    echo
    echo "export RESOURCE_GROUP=YOUR_RESOURCE_GROUP_NAME_HERE"
    echo
else
    echo "Setting Cosmos DB environment for Cassandra API..."

    DB_HOSTNAME="${RESOURCE_GROUP}.cassandra.cosmos.azure.com"
    DB_USERNAME="${RESOURCE_GROUP}"
    DB_PASSWORD=$(az cosmosdb keys list --resource-group "${RESOURCE_GROUP}" --name "${RESOURCE_GROUP}" --query primaryMasterKey --output tsv)

    export DB_HOSTNAME
    export DB_USERNAME
    export DB_PASSWORD

    echo "Environment set successfully!"
    echo
    echo "    DB_HOSTNAME = ${DB_HOSTNAME}"
    echo "    DB_USERNAME = ${DB_USERNAME}"
    echo "    DB_PASSWORD = ${DB_PASSWORD}"
    echo
fi
