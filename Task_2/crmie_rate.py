# 1) Analyze crime data to identify patterns and factors influencing crime rates.
# 2) Create visualizations and suggest strategies for crime prevention.

# Step1: Load the datasets
import pandas as pd
filepath = "uscrime.csv"
df = pd.read_csv(filepath)
print(df)  # Display complete dataset
print(df.head(10)) # Dispaly 10 rows
print(df.isnull().sum()) # check for missing values
print(df.columns) # Display coumn name

#-----------------------------------------------------------------------------------

# Step2: Analyze Correlation between Crime rate and factors
import matplotlib.pyplot as plt
import seaborn as sns
corr_matrix = df.corr() # Compute correlation matrix
plt.figure(figsize= (10,8)) # Plot the correlation heatmap
sns.heatmap(corr_matrix, annot= True, cmap= "coolwarm", fmt= ".2f")
plt.title("Correlation Between Factors and Crime Rate")
plt.subplots_adjust(bottom=0.200)
plt.show()

#-----------------------------------------------------------------------------

# Step3: Scatter Plot of Crime Rate vs Key Factors
factors = ["Ed", "Po1", "Po2", "LF", "U1", "U2", "Wealth", "Ineq"] # Compare with crime rate

plt.figure(figsize=(12,10))
for i, factor in enumerate(factors,1):
    plt.subplot(3,3,i)
    sns.scatterplot(x=df[factor],y=df["Crime"])
    plt.title(f"{factor} vs Crime Rate")
    plt.xlabel(factor)
    plt.ylabel("Crime")
    plt.subplots_adjust(bottom=0.158)
    plt.subplots_adjust(hspace=0.520)
    plt.subplots_adjust(wspace=0.302)
    plt.subplots_adjust(top=0.953)
#plt.tight_layout()
plt.show()

#---------------------------------------------------------------------------------

# Step4: Regressional Analysis
import statsmodels.api as sm
X = df[["Ed", "Po1", "Po2", "LF", "U1", "U2", "Wealth", "Ineq"]] # independent variable
Y = df["Crime"]
X = sm.add_constant(X) # Add constant required for statsmodel regression
model = sm.OLS(Y,X).fit() # first regression models
print(model.summary())
