import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database credentials from .env file
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Connect to MySQL
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# Fetch data from each table and store it in separate DataFrames
df_orders = pd.read_sql("SELECT * FROM orders", conn)
df_customers = pd.read_sql("SELECT * FROM customers", conn)
df_products = pd.read_sql("SELECT * FROM products", conn)
df_order_items = pd.read_sql("SELECT * FROM order_items", conn)

# Close connection AFTER all queries
conn.close()

# Print to verify data loaded correctly
print(df_orders.head())
print(df_customers.head())
print(df_products.head())
print(df_order_items.head())

# Save DataFrames to CSV 
df_orders.to_csv("data/orders.csv", index=False)
df_customers.to_csv("data/customers.csv", index=False)
df_products.to_csv("data/products.csv", index=False)
df_order_items.to_csv("data/order_items.csv", index=False)

print("✅ Data successfully fetched and saved!")
