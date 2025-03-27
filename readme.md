# E-Commerce Analytics Project

## 📌 Overview
This project analyzes **E-Commerce sales data** to provide insights using **Python, Pandas,matplotlib, MySQL, and Streamlit**. The system cleans raw sales data, stores it in MySQL, and visualizes trends in a **Streamlit dashboard**.

---
## 📂 Project Structure
```
ecommerce-analytics/
├── .env               # Stores sensitive credentials (NEVER commit this to GitHub)
├── .gitignore         # Ignores unnecessary files
├── data/              # Stores raw & cleaned data
│   ├── cleaned_data.csv
├── scripts/           # Python scripts for processing data
│   ├── data_cleaning.py
│   ├── prediction.py  
├── app.py # Streamlit app 
├── README.md          # Project documentation
```

---
## 🛠️ Setup & Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/manya12sharma/ecommerce-analytics.git
cd ecommerce-analytics
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up MySQL Database
```sql
CREATE DATABASE ecommerce;
USE ecommerce;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(255) UNIQUE,
    signup_date DATE
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

---
## 🚀 Running the Project
### 1️⃣ Run Data Cleaning Script
```bash
python scripts/data_cleaning.py
```

### 2️⃣ Run Prediction Script
```bash
python scripts/prediction.py
```

### 3️⃣ Run Streamlit Dashboard
```bash
streamlit app.py
```

---
## 📊 Features
✅ **Data Cleaning & Processing** - Cleans raw CSV files and stores structured data in MySQL.
✅ **Sales Insights Dashboard** - Interactive visualizations with Streamlit.
✅ **Prediction Model** - Uses machine learning to predict future sales trends.
✅ **Secure Credentials** - Uses `.env` for storing database credentials safely.
✅ **Scalability** - Supports large datasets for analytics.

---
## 📢 Contributing
Want to improve this project? **Fork, clone, and submit a pull request!** 🚀
