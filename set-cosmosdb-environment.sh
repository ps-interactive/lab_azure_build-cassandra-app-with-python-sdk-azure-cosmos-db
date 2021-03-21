#!/usr/bin/env bash
if [ -z "${RESOURCE_GROUP}" ];
then
    echo "Please manually set the RESOURCE_GROUP environment variable:"
    echo "For example:"
    echo
    echo "export RESOURCE_GROUP=YOUR_RESOURCE_GROUP_NAME_HERE"
    echo
else
    echo "Setting Cosmos DB environment for Cassandra API..."
    DOCUMENT_ENDPOINT=$(az cosmosdb show --resource-group "${RESOURCE_GROUP}" --name "${RESOURCE_GROUP}" --query documentEndpoint --output tsv)
    PRIMARY_MASTER_KEY=$(az cosmosdb keys list --resource-group "${RESOURCE_GROUP}" --name "${RESOURCE_GROUP}" --query primaryMasterKey --output tsv)
    export DOCUMENT_ENDPOINT
    export PRIMARY_MASTER_KEY
    echo "Environment set successfully!"
    echo
    echo "    DOCUMENT_ENDPOINT  = ${DOCUMENT_ENDPOINT}"
    echo "    PRIMARY_MASTER_KEY = ${PRIMARY_MASTER_KEY}"
    echo
fi
