import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data from your file (modify this to your actual file path)
df = pd.read_csv('C:/Users/sondr/Downloads/skostr_hoyde.csv')

# Display the first few rows of the data to understand its structure
print(df.head())

# Assuming the CSV contains two columns, 'X' (independent variable) and 'Y' (dependent variable)
X = df[['skostr']]  # Replace 'X' with the actual column name
Y = df['hoyde']    # Replace 'Y' with the actual column name

# Create a linear regression model
model = LinearRegression()
model.fit(X, Y)

# Make predictions
Y_pred = model.predict(X)

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X.squeeze(), y=Y, color="blue", label="Actual Data")
plt.plot(X, Y_pred, color='red', label="Regression Line")
plt.title('Regression Analysis')
plt.xlabel('Skostørrelse (X)')
plt.ylabel('Høyde (Y)')
plt.legend()
plt.show()

# Print the regression coefficients
print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")
