import pandas as pd

# Load dataset
df = pd.read_csv("housing_dataset_large.csv")

# Features (inputs)
X = df[['Bedrooms','Bathrooms','Size_sqft','Parking_space','Condition']]

# Target (output)
y = df['Price_INR']

# Import and train Linear Regression model
from sklearn.linear_model import LinearRegression
le = LinearRegression()
le.fit(X, y)

# Get user inputs
print("Enter the details of the house:")
bedrooms = int(input("Number of bedrooms:"))
bathrooms = int(input("Number of bathrooms:"))
size_sqft = int(input("Size in sqft:"))
parking_space = int(input("Parking space (1 for yes 0 for no):"))
condition = int(input("Condition (1-5):"))

# Make prediction
features = [[bedrooms, bathrooms, size_sqft, parking_space, condition]]
price = le.predict(features)[0]

print("INR", price)
le.score(X, y) * 100
