import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
try:
    df = pd.read_csv("data/cleaned_data.csv")
    if df.empty:
        raise ValueError("❌ ERROR: The dataset is empty! Ensure that 'cleaned_data.csv' has valid data.")
    print("✅ Cleaned data loaded successfully")
except FileNotFoundError:
    print("❌ ERROR: 'cleaned_data.csv' file not found. Run data_cleaning.py first.")
    exit()

# Sales trend analysis
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')

# Total sales per month
monthly_sales = df.groupby('month')['total_amount'].sum()

# Plot sales trends
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.title("Monthly Sales Trend")
plt.grid()
plt.show()
