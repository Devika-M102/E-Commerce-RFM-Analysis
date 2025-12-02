import pandas as pd
from datetime import timedelta

# --- Configuration ---
# This script READS the cleaned data from Phase 1.
CLEANED_DATA_PATH = '01_cleaned_ecommerce_data.csv' 
# This is the new file the script CREATES.
OUTPUT_RFM_CSV = '03_rfm_segments.csv'

def perform_rfm_analysis(file_path):
    """
    Performs Recency, Frequency, Monetary (RFM) analysis using the cleaned data
    to segment customers.
    """
    print(f"Loading cleaned data for RFM analysis: {file_path}")
    
    try:
        # READS the output from the 01_data_cleaning_prep.py script
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"ERROR: Input file not found at {file_path}. Did you run 01_data_cleaning_prep.py first?")
        return
    
    # Ensure InvoiceDate is datetime type and CustomerID is string
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(str)
    
    # --- 1. Define Reference Date ---
    # We use the day after the last invoice date to calculate Recency (R)
    current_date = df['InvoiceDate'].max() + timedelta(days=1)
    
    # --- 2. Calculate RFM Metrics ---
    rfm_df = df.groupby('CustomerID').agg(
        Recency=('InvoiceDate', lambda x: (current_date - x.max()).days),
        Frequency=('InvoiceNo', 'nunique'),
        Monetary=('Sales', 'sum')
    ).reset_index()

    # --- 3. Assign RFM Scores (1 to 5) using Quantiles (pd.qcut) ---
    # The 'duplicates=drop' argument handles cases where many customers have the exact same low Frequency/Monetary value.
    
    # R: Higher days (older purchase) is a worse score (1) -> reverse order
    rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], 5, labels=[5, 4, 3, 2, 1], duplicates='drop') 
    
    # F & M: Higher values are a better score (5) -> forward order. We use labels=False to get 0-based codes, then add 1.
    rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'], 5, labels=False, duplicates='drop') + 1
    rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'], 5, labels=False, duplicates='drop') + 1 
    
    # Convert scores to integers for segment mapping
    rfm_df['R_Score'] = rfm_df['R_Score'].astype(int)
    rfm_df['F_Score'] = rfm_df['F_Score'].astype(int)
    rfm_df['M_Score'] = rfm_df['M_Score'].astype(int)

    # --- 4. Create RFM Segment & Value ---
    def rfm_segment(row):
        r, f, m = row['R_Score'], row['F_Score'], row['M_Score']
        
        if r >= 4 and f >= 4 and m >= 4:
            return 'Champions'
        elif r >= 3 and f >= 3:
            return 'Loyal Customers'
        elif r <= 2 and f <= 2 and m <= 2:
            return 'Lost/At-Risk'
        else:
            return 'Other'

    rfm_df['Segment'] = rfm_df.apply(rfm_segment, axis=1)

    # --- 5. Export ---
    # SAVES the final customer segment file
    rfm_df.to_csv(OUTPUT_RFM_CSV, index=False)
    
    print("\n--- Python RFM Analysis Complete (Phase 3) ---")
    print(f"Customer segmentation saved to '{OUTPUT_RFM_CSV}'.")
    return rfm_df

if __name__ == "__main__":
    perform_rfm_analysis(CLEANED_DATA_PATH)
