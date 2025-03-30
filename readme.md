# 📊 E-Commerce Analytics Project

## 📌 Overview
This project analyzes e-commerce sales data, providing insights into sales trends, customer spending, and top-selling products. The dashboard is built using **Streamlit** and fetches data dynamically from a **MySQL database**.

## 🚀 Features
- **Sales Over Time:** Visualizes daily sales trends.
- **Top Spending Customers:** Identifies high-value customers.
- **Average Order Value (AOV):** Displays key revenue metrics.
- **Top-Selling Products:** Highlights the most popular products.
- **Interactive Charts:** Uses **Matplotlib** and **Seaborn** for data visualization.
- **Secure Credentials:** Uses `.env` for database authentication.

## 🛠️ Tech Stack
- **Python** (Pandas, Streamlit, Matplotlib, Seaborn, MySQL Connector)
- **MySQL** (Data storage and querying)
- **Streamlit** (Web-based dashboard for analysis)

## 📂 Project Structure
```
ecommerce-analytics/
├── .env               # Stores database credentials
├── .gitignore         # Ignores unnecessary files
├── data/              # Stores raw & cleaned data
│   ├── cleaned_data.csv
├── scripts/           # Python scripts for data processing
│   ├── prediction.py  # Contains predictive analysis logic
├── app.py             # Main Streamlit application
├── README.md          # Project documentation
```

## 🔧 Setup & Installation
1. Clone the repository:
   
   git clone https://github.com/manya12sharma/ecommerce_analytics.git
   cd ecommerce-analytics
   
2. Install dependencies:
   
   pip install -r requirements.txt
   
3. Set up your `.env` file with MySQL credentials:
   
   DB_HOST=your_host
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_NAME=ecommerce
   
4. Run the application:
   
   streamlit run app.py
   

## 📊 Visualizations & Insights
- **Line Chart:** Sales trend over time.
- **Bar Chart:** Best-selling products.
- **Histogram:** Customer order frequency.
- **Data Tables:** Customer spending insights.

## 📢 Contribution
Feel free to contribute by submitting pull requests or reporting issues!

---
🚀 **Developed with Python & Streamlit**

