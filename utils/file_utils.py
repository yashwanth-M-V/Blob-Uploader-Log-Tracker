import os
import uuid
from datetime import datetime

def get_file_extension(filename: str) -> str:
    """
    Returns the file extension without the dot, in lowercase.
    Example: "image.PNG" → "png"
    """
    return os.path.splitext(filename)[1].lower().lstrip(".")


def generate_blob_name(filename: str) -> str:
    """
    Generate a unique blob name while keeping the original file extension.
    Example output:
    2025-02-10T12-45-22Z_a3f1c0b9d8.png
    """
    ext = get_file_extension(filename)
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
    unique_id = uuid.uuid4().hex

    if ext:
        return f"{timestamp}_{unique_id}.{ext}"
    else:
        return f"{timestamp}_{unique_id}"


def get_basic_file_metadata(file_bytes: bytes, filename: str) -> dict:
    """
    Returns simple metadata about the uploaded file.
    """
    return {
        "filename": filename,
        "size_bytes": len(file_bytes),
        "extension": get_file_extension(filename),
    }
