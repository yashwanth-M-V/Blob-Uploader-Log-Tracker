import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

AZURE_STORAGE_CONNECTION_STRING = (
    st.secrets.get("AZURE_STORAGE_CONNECTION_STRING")
    or os.getenv("AZURE_STORAGE_CONNECTION_STRING")
)

UPLOAD_CONTAINER = (
    st.secrets.get("UPLOAD_CONTAINER")
    or os.getenv("UPLOAD_CONTAINER", "uploads")
)

LOG_CONTAINER = (
    st.secrets.get("LOG_CONTAINER")
    or os.getenv("LOG_CONTAINER", "logs")
)

APP_TITLE = "Blob Uploader & Log Tracker"
APP_DESCRIPTION = "A simple app to upload files to Azure Blob Storage and track logs."