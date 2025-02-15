# Analyze the sales data to identify pattern, trends, and factor affecting sales

import pandas as pd  
import matplotlib as plt
import seaborn as sns

# Define the file path  
file_path = r"C:\Users\E VELLAY\.cache\kagglehub\datasets\kyanyoga\sample-sales-data\versions\1\sales_data_sample.csv"

# Load the dataset  
df = pd.read_csv(file_path, encoding="ISO-8859-1")  

# Display first few rows  
print(df.head())  

# check data set info
df.info()
#print(df.isnull().sum())

#---------------------------------------------------------------------------------------------------
# First
# Analyze Sales Trends
# Total Sales over time

# Remove spaces from column names
df.columns = df.columns.str.strip()
print(df.columns)

# Convert date column 
df['ORDERDATE'] = pd.to_datetime(df["ORDERDATE"])

# Group the sales by month
monthly_sales = df.groupby(df['ORDERDATE'].dt.to_period('M'))['SALES'].sum()
print(monthly_sales)

# Plot Sales Trends 
# Create the graph of Monthly sales Trends and total Sales
monthly_sales.plot(kind= 'line', title= 'Monthly Sales Trend', figsize = (20,10))
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

#------------------------------------------------------------------------------------------------

# Second
# Top Selling Product
top_product = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending= False)
print(top_product)

# Create a bar chart
top_product.plot(kind= 'line', title= 'Top Selling Product', figsize= (20,10))
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.show()

#---------------------------------------------------------------------------------------------

# Third
# Factor Affecting Sales
sns.scatterplot(x=df['PRICEEACH'], y=df['SALES'])

# Show the Graph
plt.title("Price vs Sales")
plt.xlabel("Price per unit")
plt.ylabel("Total Sales")
plt.show()