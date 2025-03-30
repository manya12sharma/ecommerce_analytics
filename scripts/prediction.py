import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database Connection
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Fetch data from MySQL tables
def fetch_data(query):
    return pd.read_sql(query, conn)

# Load all necessary tables
df_orders = fetch_data("SELECT * FROM orders")
df_customers = fetch_data("SELECT * FROM customers")
df_products = fetch_data("SELECT * FROM products")
df_order_items = fetch_data("SELECT * FROM order_items")

conn.close()  # Close the connection after fetching data

# Merge orders with order_items to get product_id and total_amount
df_merged = df_orders.merge(df_order_items, on="order_id")

# Streamlit UI
st.title("📊 E-Commerce Sales Analytics")

# ✅ **1️ Sales Over Time (Date-wise)**
st.subheader("📅 Sales Over Time")
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])  # Ensure date format
sales_trend = df_orders.groupby("order_date")['total_amount'].sum().reset_index()

fig, ax = plt.subplots()
sns.lineplot(x='order_date', y='total_amount', data=sales_trend, marker="o", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# ✅ **2️ Top 10 Spending Customers**
st.subheader("💰 Top Customers by Spending")
top_customers = df_orders.groupby("customer_id")['total_amount'].sum().nlargest(10).reset_index()
top_customers = top_customers.merge(df_customers, on="customer_id")  # Add customer names
st.dataframe(top_customers)

# ✅ **3 Average Order Value (AOV)**
st.subheader("📦 Average Order Value")
aov = df_orders['total_amount'].mean()
st.metric(label="Average Order Value ($)", value=round(aov, 2))


# ✅ **4 Top-Selling Products (Bar Chart)**
st.subheader("📈 Top-Selling Products")
product_sales = df_merged.groupby("product_id")['total_amount'].sum().reset_index()
product_sales = product_sales.merge(df_products, on="product_id")  # Add product names

fig, ax = plt.subplots()
sns.barplot(x="total_amount", y="product_name", data=product_sales.sort_values(by="total_amount", ascending=False), ax=ax)
st.pyplot(fig)

st.write("✅ Analysis Complete!")
