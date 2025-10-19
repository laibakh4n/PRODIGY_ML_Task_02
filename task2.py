# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 12:55:46 2025
@author: Laiba
@project: Prodigy Infotech - Task 2
@description: K-Means Clustering on Retail Store Customers
"""

# =============================
# Import Libraries
# =============================
import os
os.environ["OMP_NUM_THREADS"] = "1"  # Prevents MKL thread issues on Windows
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# =============================
# Load Dataset
# =============================
data = pd.read_csv("Mall_Customers.csv")

# Display dataset summary
print("===== DATA PREVIEW =====")
print(data.head())
print("\n===== DATA INFO =====")
print(data.info())
print("\n===== STATISTICS =====")
print(data.describe())

# Check for missing values
print("\n===== MISSING VALUES =====")
print(data.isnull().sum())

# =============================
# Data Visualization
# =============================
sns.pairplot(data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']])
plt.show()

# =============================
# Prepare Data for Clustering
# =============================
X = data[['Annual Income (k$)', 'Spending Score (1-100)']].values

# =============================
# Elbow Method to find optimal K
# =============================
wcss = []  # within-cluster sum of squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o', color='purple')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')

# ----Ensure 'outputs' folder exists before saving
os.makedirs("outputs", exist_ok=True)

# 💾 Save Elbow Plot
plt.savefig("outputs/elbow_plot.png")
plt.show()

# =============================
# Apply K-Means with optimal K
# =============================
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# =============================
# Visualize Clusters
# =============================
plt.figure(figsize=(8, 6))
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=80, c='red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=80, c='blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=80, c='green', label='Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=80, c='cyan', label='Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=80, c='magenta', label='Cluster 5')

# ------Cluster Centers
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=300, c='yellow', marker='*', label='Centroids'
)

plt.title('Customer Segments')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()

# ----- Save Cluster Visualization
plt.savefig("outputs/customer_clusters.png")
plt.show()

print("\n✅ Plots saved successfully in the 'outputs' folder!")
