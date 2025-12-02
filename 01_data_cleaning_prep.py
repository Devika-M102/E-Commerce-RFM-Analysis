import pandas as pd
from datetime import datetime

# --- Configuration ---
# IMPORTANT: Ensure 'Online Retail.xlsx' is in the same folder as this script.
FILE_PATH = 'Online Retail.xlsx' 
OUTPUT_CLEAN_CSV = '01_cleaned_ecommerce_data.csv'

def clean_and_prepare_data(file_path):
    """
    Loads the raw dataset, cleans it using pure Pandas methods, calculates 
    key financial metrics, and prepares it for SQL ingestion.
    """
    print(f"Loading raw data from: {file_path}")
    try:
        # Load the data - assuming it's an XLSX file
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path, header=0) 
        else:
            # Fallback for CSV
            df = pd.read_csv(file_path, encoding='unicode_escape')
    except Exception as e:
        print(f"Error loading file: {e}")
        print("Please ensure the data file is in the correct path.")
        return None

    # --- 1. Data Cleaning ---
    df.dropna(subset=['CustomerID', 'StockCode', 'Description'], inplace=True)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    df['CustomerID'] = df['CustomerID'].astype(int).astype(str)

    # --- 2. Feature Engineering (Financial Metrics) ---
    df['Sales'] = df['Quantity'] * df['UnitPrice']
    
    # Deterministic Cost Proxy (Fixed 40% Gross Margin)
    df['UnitCost'] = df['UnitPrice'] * 0.60
    df['TotalCost'] = df['Quantity'] * df['UnitCost']
    
    df['Profit'] = df['Sales'] - df['TotalCost']

    # --- 3. Final Selection & Export ---
    df_clean = df[['InvoiceNo', 'StockCode', 'Description', 'Quantity', 
                   'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country', 
                   'Sales', 'TotalCost', 'Profit']]
    
    df_clean.to_csv(OUTPUT_CLEAN_CSV, index=False)
    
    print("\n--- Python Cleaning Step Complete (Pure Pandas) ---")
    print(f"Cleaned data saved to '{OUTPUT_CLEAN_CSV}'. Ready for SQL.")
    return df_clean

if __name__ == "__main__":
    clean_and_prepare_data(FILE_PATH)