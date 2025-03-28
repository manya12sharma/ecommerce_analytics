import streamlit as st
import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv
 
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "ecommerce"

def fetch_data():
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    df = pd.read_sql("SELECT * FROM orders", conn)
    conn.close()
    return df

st.title("E-commerce Analytics Dashboard")
data = fetch_data()
st.write(data)



