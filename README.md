# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 14:08:54 2025

@author: laiba
"""

🛍️ Customer Segmentation using K-Means Clustering

Internship Project — ProDigy Infotech
Developed by Layba Khan 👩‍💻

🌟 Overview

This project applies K-Means Clustering to group customers of a retail store based on their purchase history.
By identifying unique customer segments, businesses can tailor marketing strategies, improve customer satisfaction, and boost sales.

📂 Dataset

Source: Kaggle – Customer Segmentation Tutorial in Python

File used: Mall_Customers.csv

Dataset Features:
Column	Description
CustomerID	Unique customer identifier
Gender	Male/Female
Age	Customer age
Annual Income (k$)	Annual income in thousands
Spending Score (1–100)	Store-assigned spending score
⚙️ Project Workflow

Import Libraries – Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn

Load Dataset – Mall_Customers.csv

Data Preprocessing – Select relevant features

Elbow Method – Determine the optimal number of clusters

Apply K-Means – Cluster customers based on income and spending score

Visualize Results – Save and display graphs in the outputs/ folder

🧠 Algorithms Used

K-Means Clustering – Unsupervised ML algorithm for grouping data

Elbow Method – Identifies the optimal cluster count by minimizing WCSS (Within-Cluster Sum of Squares)

🖼️ Output Files

All visualizations are saved in the outputs/ directory:

File Name	Description
elbow_plot.png	Elbow Method graph showing optimal clusters
clusters_plot.png	Visualization of customer clusters
spending_income_plot.png	Income vs Spending Score distribution
🧩 Tools & Libraries
Tool	Purpose
🐍 Python	Core language
📊 Pandas	Data manipulation
🔢 NumPy	Numerical computations
📈 Matplotlib / Seaborn	Data visualization
🤖 Scikit-learn	Machine learning (K-Means)
🚀 How to Run
1️⃣ Clone the repository
git clone https://github.com/yourusername/customer-segmentation.git
cd customer-segmentation

2️⃣ Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

3️⃣ Run the script
python task2.py

4️⃣ View outputs

All generated graphs will appear in the outputs/ folder.

📈 Example Visuals
Elbow Method	Cluster Visualization

	
💡 Insights

Customers are grouped by spending habits and income levels.

Helps identify high-value vs low-spending customer groups.

Enables data-driven marketing decisions.

🏁 Future Improvements

Use hierarchical clustering for comparison.

Add customer demographics for richer segmentation.

Deploy model in a web dashboard (Streamlit/Flask).

🧑‍💻 Author

Layba Khan
📚 Electrical Engineering Student | 💼 Machine Learning Enthusiast
📍 ProDigy Infotech Internship Project