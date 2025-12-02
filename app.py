import streamlit as st
from services.blob_client import get_client, upload_file_to_blob, list_logs
from services.log_writer import write_log_record
from utils.file_utils import get_basic_file_metadata
from datetime import datetime

def main():
    st.title("Azure Blob Uploader + Log Container")
    st.text("make sure no sentive files are uploaded")

    uploaded_file = st.file_uploader("Upload file")

    if uploaded_file:
        file_bytes = uploaded_file.read()
        meta = get_basic_file_metadata(file_bytes, uploaded_file.name)

        if st.button("Upload"):
            # 1. upload file
            file_url = upload_file_to_blob(file_bytes, uploaded_file.name)

            # 2. create log
            log_record = {
                "filename": meta["filename"],
                "extension": meta["extension"],
                "size_bytes": meta["size_bytes"],
                "uploaded_at": datetime.utcnow().isoformat() + "Z",
                "blob_url": file_url
            }

            # 3. save to logs container
            log_url = write_log_record(log_record)

            st.success("Uploaded successfully!")
            st.write("File URL:", file_url)
            st.write("Log URL:", log_url)

    st.subheader("Recent Logs")
    logs = list_logs()
    st.table(logs)

if __name__ == "__main__":
    main()
