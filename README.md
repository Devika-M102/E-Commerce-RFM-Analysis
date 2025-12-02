📊 E-commerce RFM Customer Segmentation & Visualization

Recency, Frequency, and Monetary Value Analysis

📌 Overview

This project provides a comprehensive data science solution for analyzing customer value using the RFM (Recency, Frequency, Monetary Value) model on an e-commerce transactional dataset.

The analysis provides deep insights into customer behavior, allowing the business to optimize retention efforts, personalized promotions, and overall customer lifetime value. The core output is a clean, segment-labeled dataset, which is then visualized in a single-file D3.js dashboard to provide immediate, actionable insights into the customer base structure.

✨ Features

Data Ingestion & Cleaning: Robust Python pipeline for handling missing data, outliers, and preparing the dataset for analysis.

RFM Calculation: Accurate calculation of R, F, and M scores for all customers.

Clustering & Segmentation: Application of K-Means clustering to automatically group customers into strategic segments (e.g., Champions, At-Risk, Loyalists).

Web Visualization: A responsive, single-page dashboard (rfm_dashboard.html) built with D3.js and Tailwind CSS to visually display the segment breakdown.

🛠️ Repository Contents

File/Folder

Description

01_data_cleaning_prep.py

Python script for initial data preparation and cleaning.

03_rfm_analysis.py

Python script for calculating RFM scores and performing K-Means segmentation.

03_rfm_segments.csv

Final Output Data: Contains CustomerID and the assigned RFM_Segment.

rfm_dashboard.html

Interactive Dashboard: A self-contained HTML file (D3.js/Tailwind) that visualizes the segmentation results using embedded data.

README.md

This documentation file.

🚀 How to Run the Dashboard

The visualization is designed for immediate viewing because the data is embedded directly into the HTML file (a necessary fix for online execution environments).

Locate the File: Navigate to the rfm_dashboard.html file in the repository.

Open in Browser: Double-click the file to open it in any modern web browser.

🐍 Analysis Pipeline (Python)

To re-run the segmentation process locally, you need Python and the core data science libraries:

Install Dependencies:

pip install pandas numpy scikit-learn


Execute Cleaning:

python 01_data_cleaning_prep.py


Execute Segmentation:

python 03_rfm_analysis.py


(Note: This step generates the 03_rfm_segments.csv file, which should ideally be used to update the embedded data in the HTML file for the dashboard.)

💡 Strategic Segment Definitions

Segment Name

Definition (R/F/M)

Recommended Strategy

Champions

High / High / High

Reward and prioritize. Encourage referrals and early access to new products.

Loyal Customers

Mid / High / Mid

Upsell higher-value products and encourage participation in loyalty programs.

Potential Loyalist

High / Mid / Mid

Offer targeted incentives to increase purchase frequency (F).

At-Risk

Low / Mid / Mid

Launch win-back campaigns, personalized offers, and gentle reminders of past value.

Hibernating

Low / Low / Low

Deep discounts or minimal marketing efforts, focusing resources on higher-potential groups.


Project by Devika M
