import logging
import os
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

def main(event: func.EventGridEvent):
    logging.info("Event received: %s", event.get_json())

    data = event.get_json()
    resource_id = data.get('data', {}).get('resourceId', '')

    if not resource_id:
        logging.error("No resourceId in event data")
        return

    credential = DefaultAzureCredential()

    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        logging.error("AZURE_SUBSCRIPTION_ID environment variable is not set")
        return

    client = ResourceManagementClient(credential, subscription_id)

    try:
        resource = client.resources.get_by_id(resource_id, api_version="2021-04-01")
        tags = resource.tags or {}
        if "env" not in tags:
            tags["env"] = "remediated"
            client.resources.update_by_id(resource_id, "2021-04-01", {"tags": tags})
            logging.info("Tag 'env=remediated' added to resource: %s", resource_id)
    except Exception as e:
        logging.error("Error processing resource %s: %s", resource_id, str(e))
