# Predict Crime rate using a machine learning model(Linear Regression)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# Step1: Load the dataset and Prpare features
file_path = "uscrime.csv"
df = pd.read_csv(file_path)
print(df)

# Select independent variable
X = df[["Ed", "Po1", "Po2", "LF", "U1", "U2", "Wealth", "Ineq"]]
Y = df["Crime"] # Targe(crime rate)

# Split data into training(80%) and testing(20%)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Scale the feature for better performance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

#--------------------------------------------------------------------------

# Step2: Train and Evaluate the Linear Regression Model
# Train the model
lr_model = LinearRegression()
lr_model.fit(X_train_scaled,y_train)

# Make Prediction 
y_pred = lr_model.predict(X_test_scaled)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Display the output
print("Linear Regression Results:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

#-------------------------------------------------------------------

# Step3: Visualizing Predictions
# Scatter plot for Actual vs. Predicted Crime Rates
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color="blue", alpha=0.7)
plt.plot(y_test, y_test, color="red", linestyle="--")  # Perfect Prediction Line
plt.xlabel("Actual Crime Rate")
plt.ylabel("Predicted Crime Rate")
plt.title("Actual vs. Predicted Crime Rates (Linear Regression)")
plt.grid(True)
plt.show()

#---------------------------------------------------------------------

# Step5: Feature Importance (Bar Chart)
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Prepare features and target
X = df[["Ed", "Po1", "Po2", "LF", "U1", "U2", "Wealth", "Ineq"]]
y = df["Crime"]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_scaled, y)

# Feature Importance
importance = pd.DataFrame({"Feature": X.columns, "Coefficient": model.coef_})
importance = importance.sort_values(by="Coefficient", ascending=False)

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(x="Coefficient", y="Feature", data=importance, palette="coolwarm")
plt.title("Factor Importance in Predicting Crime Rate")
plt.xlabel("Impact on Crime Rate")
plt.ylabel("Socioeconomic Factor")
plt.show()






