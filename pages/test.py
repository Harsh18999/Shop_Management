import streamlit as st
import sqlite3
from io import BytesIO

# Function to create a download link for SQLite database
def download_sqlite_database(database_path, button_text='Download Database'):
    with open(("Darabase.db", 'rb') as f:
        database_bytes = BytesIO(f.read())
    st.download_button(label=button_text, data=database_bytes, file_name='darabase.db', mime='application/octet-stream')

def main():
    st.title('SQLite Database Downloader')

    # Path to your SQLite database
    database_path = 'darabase.db'

    # Display the download button
    download_sqlite_database(database_path)

if __name__ == "__main__":
    main()
