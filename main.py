import streamlit as st
import pandas as pd
from utils import search_web, parse_results_with_groq
import config
import gspread
from google.oauth2.service_account import Credentials

st.title("AI Agent for Automated Information Retrieval")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
google_sheet_url = st.text_input("Or, enter Google Sheet URL")

data = None

if uploaded_file:
    # Load data from CSV
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded CSV data:", data.head())

elif google_sheet_url:
    # Google Sheets authentication and data loading
    try:
        credentials = Credentials.from_service_account_info(config.GOOGLE_SHEETS_CREDENTIALS)
        gc = gspread.authorize(credentials)
        sheet = gc.open_by_url(google_sheet_url).sheet1
        data = pd.DataFrame(sheet.get_all_records())
        st.write("Google Sheet data:", data.head())
    except Exception as e:
        st.error(f"Failed to load Google Sheet: {e}")

if data is not None:
    # Display columns and allow user to select the main column
    main_column = st.selectbox("Select the main column for entity retrieval", data.columns)
    st.write("Selected main column:", main_column)

    # Custom prompt input
    prompt_template = st.text_input("Enter custom prompt (e.g., 'Get the email address of {company}')")
    st.write("Note: Use `{company}` as a placeholder in your prompt. It will be replaced by each entity in the selected column.")

    # Initialize a list to store extracted data
    extracted_data = []

    # Start processing when the button is clicked and the prompt is filled
    if st.button("Start Processing") and prompt_template:
        # Iterate over each entity in the selected column
        for entity in data[main_column]:
            # Replace placeholder with the actual entity name
            search_query = prompt_template.format(company=entity)
            
            # Perform a web search using the custom query
            search_results = search_web(entity, prompt_template)
            
            # Check if search results were retrieved successfully
            if search_results:
                extracted_info = parse_results_with_groq(search_results, prompt_template)
                extracted_data.append({"Entity": entity, "Extracted Info": extracted_info})
            else:
                extracted_data.append({"Entity": entity, "Extracted Info": "No data found"})

        # Convert results to DataFrame for display
        result_df = pd.DataFrame(extracted_data)
        st.write("Extracted Information:")
        st.write(result_df)

        # Allow user to download extracted data as CSV
        def convert_df_to_csv(df):
            return df.to_csv(index=False).encode('utf-8')

        # If there is extracted data, enable the download button
        csv = convert_df_to_csv(result_df)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='extracted_data.csv',
            mime='text/csv'
        )
