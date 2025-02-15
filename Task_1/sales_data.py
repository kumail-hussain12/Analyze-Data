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

# Remove spaces from column names
df.columns = df.columns.str.strip()
print(df.columns)

#---------------------------------------------------------------------------------------------------
# First
# Analyze Sales Trends
# Total Sales over time
# Monthly Sales Trends 

# Convert orderdate to datetime 
df['ORDERDATE'] = pd.to_datetime(df["ORDERDATE"])

# Group the sales by month
monthly_sales = df.groupby(df['ORDERDATE'].dt.to_period('M'))['SALES'].sum()
print(monthly_sales)

# Plot Sales Trends 
# Create a Plot bar chart
monthly_sales.plot(kind= 'line', marker= 'o', color= 'b')
plt.figure(figsize =(25,12))
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

#------------------------------------------------------------------------------------------------

# Second
# Top Selling Product
top_product = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending= False)
print(top_product)

# Create a Plot bar chart
plt.figure(figsize= (25,12))
top_product.plot(kind= 'bar', color= 'g')
plt.title("Top Selling Product")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation= 45)
plt.show()

#--------------------------------------------------------------------------------------------
# Sales By Region
# Sales by country  
top_countries = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False)

# Create a Plot bar chart  
plt.figure(figsize=(25,12))  
top_countries.plot(kind='bar', color='orange')  
plt.title("Sales by Country")  
plt.xlabel("Country")  
plt.ylabel("Total Sales")  
plt.xticks(rotation=45)  
plt.show()


#---------------------------------------------------------------------------------------------

# Factor Affecting Sales
plt.figure(figsize=(12,8) )
sns.scatterplot(x=df['PRICEEACH'], y=df['SALES'], alpha= 0.5)

# Show the Graph
plt.title("Price vs Sales")
plt.xlabel("Price per unit")
plt.ylabel("Total Sales")
plt.show()