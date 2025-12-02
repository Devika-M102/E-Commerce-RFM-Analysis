📊 E-commerce RFM Customer Segmentation \& Visualization



Recency, Frequency, and Monetary Value Analysis



📌 Overview



This project delivers a comprehensive solution for analyzing customer value in e-commerce using the RFM (Recency, Frequency, Monetary Value) model. The analysis identifies distinct customer segments, enabling targeted marketing campaigns to maximize customer lifetime value (CLV).



The final output is a clean, segmented dataset, which is visually presented through an interactive dashboard hosted on Tableau Public.



🔗 Final Visualization: Tableau Public Dashboard



The complete, interactive results of the RFM segmentation are visualized in this live dashboard.



Click here to explore the interactive RFM analysis on Tableau Public



🛠️ Repository Contents (The Analysis Pipeline)



This repository contains the Python scripts and documentation used to perform the data cleaning and segmentation, leading to the data imported into the Tableau dashboard.



File/Folder



Description



01\_data\_cleaning\_prep.py



Python script for initial data preparation, handling missing values, and outlier treatment.



03\_rfm\_analysis.py



Python script for calculating RFM scores and performing K-Means clustering to create customer segments.



03\_rfm\_segments.csv



The final output dataset containing customer IDs and their assigned RFM segment labels (used as the data source for Tableau).



README.md



This documentation file.



.gitignore



Ensures large data files (like the original Excel/CSV) are excluded from the GitHub repository.



🐍 Analysis Pipeline (Python Setup)



To replicate the segmentation process locally, use the following steps:



Install Dependencies:



pip install pandas numpy scikit-learn





Execute Cleaning:



python 01\_data\_cleaning\_prep.py





Execute Segmentation:



python 03\_rfm\_analysis.py





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



At-Risk/Lapsed



Low / Mid / Low



Launch win-back campaigns, personalized offers, and gentle reminders.



Hibernating



Low / Low / Low



Minimal marketing effort, focusing resources on high-potential groups.



Project by DEVIKA M

