import os
import subprocess

print("🚀 Starting the Ecommerce Analytics Project...")

# Step 1: Ensure the database is set up
print("🔹 Checking MySQL Database...")
db_check = subprocess.run(['mysql', '-u', 'root', '-p', '-e', 'USE ecommerce;'], shell=True)
if db_check.returncode != 0:
    print("❌ ERROR: Database 'ecommerce' not found. Please create it first!")
    exit()

# Step 2: Run Data Cleaning Script
print("🔹 Running Data Cleaning Script...")
subprocess.run(['python', 'scripts/data_cleaning.py'], shell=True)

# Step 3: Run Prediction Script
print("🔹 Running Prediction Script...")
subprocess.run(['python', 'scripts/prediction.py'], shell=True)

# Step 4: Launch the Streamlit Dashboard
print("🔹 Launching Streamlit Dashboard... (Open http://localhost:8501)")
subprocess.run(['streamlit', 'run', 'scripts/dashboard.py'], shell=True)
