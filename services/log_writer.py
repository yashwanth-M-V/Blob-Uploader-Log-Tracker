import json
from datetime import datetime
from azure.storage.blob import BlobServiceClient
from config import AZURE_STORAGE_CONNECTION_STRING, LOG_CONTAINER
import uuid

_blob_service_client = None

def get_blob_client():
    global _blob_service_client
    if _blob_service_client is None:
        _blob_service_client = BlobServiceClient.from_connection_string(
            AZURE_STORAGE_CONNECTION_STRING
        )
    return _blob_service_client

def write_log_record(record: dict) -> str:
    client = get_blob_client()
    container = client.get_container_client(LOG_CONTAINER)

    # create if not exists
    try:
        container.create_container()
    except:
        pass

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
    log_name = f"{timestamp}_{uuid.uuid4().hex}.json"

    blob_client = container.get_blob_client(log_name)

    blob_client.upload_blob(
        json.dumps(record, indent=2),
        overwrite=True,
        content_type="application/json"
    )

    return blob_client.url
