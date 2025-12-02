import os
from dotenv import load_dotenv

# Load .env file (for local development)
load_dotenv()

# --------------------------
# Azure Blob Storage Settings
# --------------------------

# This must come from your Storage Account → Access Keys → Connection string
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")

# Container for storing uploaded files
UPLOAD_CONTAINER = os.getenv("UPLOAD_CONTAINER", "uploads")

# Container for storing log files
LOG_CONTAINER = os.getenv("LOG_CONTAINER", "logs")

# App title (for Streamlit UI)
APP_TITLE = "Simple Blob Uploader + Log Container"
