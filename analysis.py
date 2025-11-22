import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sales.csv")
print(df.head())

# Basic info
print(df.info())
print(df.describe())

# Group by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print(sales_by_product)

# Plot bar chart
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
