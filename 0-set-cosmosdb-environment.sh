#!/usr/bin/env bash

RESOURCE_GROUP=${RESOURCE_GROUP:-$(az group list --query "[?contains(name, 'azure-lab')].name" --output tsv)}

if [ -z "${RESOURCE_GROUP}" ];
then
    echo
    echo "ERROR: The resource group could not be set automatically."
    echo "       Please manually set the RESOURCE_GROUP environment"
    echo "       variable and rerun this script."
    echo
    echo "       For example:"
    echo
    echo "       export RESOURCE_GROUP=YOUR_RESOURCE_GROUP_NAME_HERE"
    echo "       source ./0-set-cosmosdb-environment.sh"
    echo
else
    echo "Setting Cosmos DB environment for Cassandra API..."

    DB_HOSTNAME="${RESOURCE_GROUP}.cassandra.cosmos.azure.com"
    DB_USERNAME="${RESOURCE_GROUP}"
    DB_PASSWORD=$(az cosmosdb keys list --resource-group "${RESOURCE_GROUP}" --name "${RESOURCE_GROUP}" --query primaryMasterKey --output tsv)

    if [ -z "${DB_HOSTNAME}" ] || [ -z "${DB_USERNAME}" ] || [ -z "${DB_PASSWORD}" ];
    then
        echo "ERROR: All of the environment variables cloud not be set."
        echo "       Please confirm that the Cassandra Cosmos DB has the"
        echo "       exact same name as the resource group ${RESOURCE_GROUP}."
        echo
    else
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
fi
