import os 
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import _mysql_connector

# import variables from .env file 
load_dotenv()

# get values from environment variables
db_host = os.getenv("DB_HOST")
db_user= os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# connect to database
conn= mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db_name
)
# fetch data from database
query = " SELECT * FROM orders"
df = pd.read_sql( query , conn)
conn.close()

 # save data to csv file
df.to_csv("data/cleaned_data.csv", index=False)
print("Data saved to cleaned_data.csv")