from azure.storage.blob import BlobServiceClient
from config import AZURE_STORAGE_CONNECTION_STRING, UPLOAD_CONTAINER
from utils.file_utils import generate_blob_name

_blob_service_client = None

def get_client():
    global _blob_service_client
    if _blob_service_client is None:
        _blob_service_client = BlobServiceClient.from_connection_string(
            AZURE_STORAGE_CONNECTION_STRING
        )
    return _blob_service_client

def upload_file_to_blob(file_bytes, filename):
    client = get_client()
    container = client.get_container_client(UPLOAD_CONTAINER)

    try:
        container.create_container()
    except:
        pass

    blob_name = generate_blob_name(filename)
    blob = container.get_blob_client(blob_name)
    blob.upload_blob(file_bytes, overwrite=True)

    return blob.url

def list_logs(limit=50):
    client = get_client()
    container = client.get_container_client("logs")

    logs = []
    for i, blob in enumerate(container.list_blobs()):
        if i >= limit:
            break
        logs.append({
            "name": blob.name,
            "last_modified": blob.last_modified
        })
    return logs
