# 🛍️ Customer Segmentation using K-Means Clustering

This project groups customers of a retail store based on their **Annual Income** and **Spending Score** using the **K-Means clustering algorithm**.  
It was created as part of the **ProDigy Infotech Internship**.

---

## 📂 Dataset

**Source:** [Kaggle – Customer Segmentation Tutorial in Python](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)  
**File used:** `Mall_Customers.csv`

### Dataset Features

| Column | Description |
|--------|--------------|
| `CustomerID` | Unique customer identifier |
| `Gender` | Male / Female |
| `Age` | Customer age |
| `Annual Income (k$)` | Annual income (in thousands) |
| `Spending Score (1–100)` | Store-assigned spending score |

---

## ⚙️ Project Workflow

1. **Import Libraries** – Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn  
2. **Load Dataset** – `Mall_Customers.csv`  
3. **Data Preprocessing** – Select relevant features  
4. **Elbow Method** – Determine optimal number of clusters  
5. **Apply K-Means** – Cluster customers by income & spending score  
6. **Visualize Results** – Save graphs in the `outputs/` folder  

---

## 🧠 Algorithms Used

- **K-Means Clustering:** Unsupervised ML algorithm for grouping data  
- **Elbow Method:** Finds optimal cluster count by minimizing WCSS (Within-Cluster Sum of Squares)

---

## 🖼️ Output Files

All visualizations are saved in the `outputs/` directory:

| File Name | Description |
|------------|-------------|
| `elbow_plot.png` | Elbow Method graph showing optimal clusters |
| `clusters_plot.png` | Visualization of customer clusters |
| `spending_income_plot.png` | Income vs. Spending Score distribution |

---

## 🧩 Tools & Libraries

| Tool | Purpose |
|------|----------|
| 🐍 **Python** | Core language |
| 📊 **Pandas** | Data manipulation |
| 🔢 **NumPy** | Numerical computations |
| 📈 **Matplotlib / Seaborn** | Data visualization |
| 🤖 **Scikit-learn** | Machine learning (K-Means) |

---

## 🚀 How to Run

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/customer-segmentation.git
cd customer-segmentation
```

2️⃣ **Install dependencies**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3️⃣ **Run the Python script**
```bash
python task2.py
```

4️⃣ **View Outputs**

Visualizations are saved inside the `outputs/` folder.  
You can open them to explore customer group patterns.

---

## 💡 Insights

- Customers are grouped by spending habits and income levels.  
- Helps identify high-value vs low-spending customer segments.  
- Enables data-driven marketing and business decisions.  

---

## 🏁 Future Improvements

- Add hierarchical clustering for comparison.  
- Include demographic analysis for deeper insights.  
- Deploy as a web dashboard (Streamlit or Flask).  

---

## 🧑‍💻 Author

**Layba Khan**  
📚 *Electrical Engineering Student* | 💼 *Machine Learning Enthusiast*  

