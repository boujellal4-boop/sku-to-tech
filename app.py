
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import time

# Predefined technology categories
TECH_CATEGORIES = [
    "Addressable",
    "Conventional",
    "Wireless",
    "Aspirating Smoke Detection",
    "Heat Detection",
    "Flame Detection",
    "Security-related Solutions"
]

BASE_URL = "https://firesecurityproducts.com"
SEARCH_URL = BASE_URL + "/search?q="

st.title("SKU Technology Mapper with Web Scraping")
st.write("Upload an Excel file with SKUs, and we'll scrape firesecurityproducts.com to map SKUs to technology categories.")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    progress_bar = st.progress(0)
    status_text = st.empty()

    def scrape_technology(sku):
        try:
            search_page = requests.get(SEARCH_URL + sku)
            soup = BeautifulSoup(search_page.text, 'html.parser')
            text_content = soup.get_text().lower()
            for tech in TECH_CATEGORIES:
                if tech.lower().split()[0] in text_content:
                    return tech
            return "Conventional"  # Default if no match
        except Exception:
            return "Conventional"

    # Add new column for technology category
    df["technology_category"] = ""

    total_rows = len(df)
    for i, sku in enumerate(df["sku"]):
        df.at[i, "technology_category"] = scrape_technology(str(sku))
        progress = int(((i + 1) / total_rows) * 100)
        progress_bar.progress(progress)
        status_text.text(f"Processing row {i+1}/{total_rows} ({progress}%)")
        time.sleep(0.5)  # To avoid overwhelming the server

    # Convert back to Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    st.download_button(
        label="Download Updated Excel",
        data=output.getvalue(),
        file_name="updated_orders.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
