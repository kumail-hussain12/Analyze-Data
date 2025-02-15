import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file path  
file_path = r"C:\Users\E VELLAY\.cache\kagglehub\datasets\kyanyoga\sample-sales-data\versions\1\sales_data_sample.csv"

# Load the dataset  
df = pd.read_csv(file_path, encoding="ISO-8859-1")  

# Display first few rows  
print(df.head())  

# Check dataset info
df.info()
# print(df)
# Remove spaces from column names
df.columns = df.columns.str.strip()
# print(df.columns)

# ---------------------------------------------------------------------------------------------------
# Analyze Sales Trends
# Convert ORDERDATE to datetime 
df['ORDERDATE'] = pd.to_datetime(df["ORDERDATE"])

# Group sales by month
monthly_sales = df.groupby(df['ORDERDATE'].dt.to_period('M'))['SALES'].sum()
print(monthly_sales)

# Plot Monthly Sales Trend
plt.figure(figsize=(12, 6))  # Ensure figure size is set correctly
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values, marker='o', color='b')
plt.subplots_adjust(bottom= 0.165)
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# ------------------------------------------------------------------------------------------------
# Top Selling Products

# Group sales by product line
top_product = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
print(top_product)

# Plot Top Selling Products
plt.figure(figsize=(12, 6))
plt.subplots_adjust(bottom=0.200)
top_product.plot(kind='bar', color='g')
plt.title("Top Selling Products")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.grid(axis='y')
plt.show()

# --------------------------------------------------------------------------------------------
# Sales by Region

# Group sales by country
top_countries = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False)

# Plot Sales by Country
plt.figure(figsize=(12, 6))  
top_countries.plot(kind='bar', color='orange')  
plt.title("Sales by Country")  
plt.xlabel("Country")  
plt.ylabel("Total Sales")  
plt.xticks(rotation=15)  
plt.grid(axis='y')
plt.show()

# ---------------------------------------------------------------------------------------------
# Factor Affecting Sales

plt.figure(figsize=(10,6))
sns.scatterplot(x=df['PRICEEACH'], y=df['SALES'], alpha=0.5)
plt.title("Price vs Sales")
plt.xlabel("Price per Unit")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()
