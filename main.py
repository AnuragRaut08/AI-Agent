import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from helpers import upload_csv, get_google_sheet, perform_web_search, extract_info_with_llm

st.title("AI Agent for Automated Information Retrieval")

# File upload section
st.header("Upload a CSV File or Connect to Google Sheets")
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    data = upload_csv(file)
    st.write("Preview of Uploaded Data:")
    st.dataframe(data)

# Google Sheets section
st.subheader("Or Connect to a Google Sheet")
gsheet_url = st.text_input("Enter Google Sheet URL")
if gsheet_url:
    data = get_google_sheet(gsheet_url)
    st.write("Preview of Google Sheet Data:")
    st.dataframe(data)

if data is not None:
    # Select the primary column
    column = st.selectbox("Select the primary column", data.columns)
    
    # Custom prompt input
    st.header("Define Your Query")
    query_template = st.text_input("Enter your query template", "Get the email address of {entity}")
    
    if st.button("Start Information Retrieval"):
        results = perform_web_search(data[column], query_template)
        extracted_info = extract_info_with_llm(results)
        
        # Display results
        st.write("Extracted Information:")
        st.dataframe(extracted_info)
        
        # Download option
        st.download_button("Download Results as CSV", data=extracted_info.to_csv(), file_name="extracted_info.csv")

