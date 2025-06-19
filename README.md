
# Price Recommender Web App

This Streamlit web app processes an Excel file with inventory data and recommends prices based on competitor pricing from gun.deals.

## Files

- `app.py`: The main Streamlit app script
- `requirements.txt`: Python dependencies
- `README.md`: Setup and deployment instructions

## Setup and Deployment

### 1. Create a GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository.
2. Name your repo (e.g., `price-recommender`).
3. Set it to **Public**.
4. Click **Create repository**.

### 2. Upload Files to GitHub

1. Upload `app.py`, `requirements.txt`, and `README.md` to your new repository.
2. Optionally, upload a sample Excel file (e.g., `highly overstocked inventory 061825 1.xlsx`).

### 3. Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in with GitHub.
2. Click **“New App”**.
3. Select your GitHub repo and branch.
4. Set the main file to `app.py`.
5. Click **Deploy**.

### 4. Use the App

1. Upload your Excel file.
2. Click **Process File**.
3. Download the updated file with recommended prices.

## Notes

- Ensure your Excel file has the columns: `SKU`, `On Hand`, `Supplier SKU`, `Barcode`, `Inventory Value`, and `Unit Cost`.
- The app will search gun.deals using either the Supplier SKU or Barcode (whichever is available and not 'NA').
- The recommended price is 5% below the lowest competitor price, but not below your unit cost.
