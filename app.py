
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to get the lowest price from gun.deals
def get_lowest_price(search_term):
    url = f"https://gun.deals/search/apachesolr_search/{search_term}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    price_tags = soup.select(".search-results .price")

    prices = []
    for tag in price_tags:
        try:
            price = float(tag.text.replace("$", "").replace(",", "").strip())
            prices.append(price)
        except:
            continue

    return min(prices) if prices else None

# Function to process the inventory file
def process_inventory(file):
    df = pd.read_excel(file, engine='openpyxl')
    lowest_prices = []
    recommended_prices = []

    for _, row in df.iterrows():
        supplier_sku = str(row["Supplier SKU"]).strip()
        barcode = str(row["Barcode"]).strip()
        unit_cost = row["Unit Cost"]

        search_term = None
        if supplier_sku and supplier_sku.upper() != "NA":
            search_term = supplier_sku
        elif barcode and barcode.upper() != "NA":
            search_term = barcode

        if search_term:
            lowest_price = get_lowest_price(search_term)
        else:
            lowest_price = None

        if lowest_price:
            recommended_price = max(unit_cost, round(lowest_price * 0.95, 2))
        else:
            recommended_price = unit_cost

        lowest_prices.append(lowest_price)
        recommended_prices.append(recommended_price)

    df["Lowest Competitor Price"] = lowest_prices
    df["Recommended Price"] = recommended_prices
    return df

# Streamlit app
st.title("Price Recommender")

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
if uploaded_file is not None:
    df = process_inventory(uploaded_file)
    st.write("Processed Data:")
    st.dataframe(df)

    # Download the processed file
    df.to_excel("recommended_prices_output.xlsx", index=False)
    with open("recommended_prices_output.xlsx", "rb") as file:
        btn = st.download_button(
            label="Download Processed File",
            data=file,
            file_name="recommended_prices_output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
