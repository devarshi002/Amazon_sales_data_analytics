import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon.csv")
df.info()
df.describe()
df.dropna(inplace=True)

# convert numeric columns to proper data types

#convert price and discount to numeric
df["discounted_price"] = df["discounted_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["actual_price"]=df["actual_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["discount_percentage"]=df["discount_percentage"].str.replace("%", "").astype(float)

#convert rating and rating_count to numeric
df["rating"]=pd.to_numeric(df["rating"], errors='coerce')
df["rating_count"]=pd.to_numeric(df["rating_count"], errors='coerce')

df.isnull().sum()  # Check missing values
df.fillna(0, inplace=True)  # Replace NaNs with 0 (or another strategy)



import matplotlib.pyplot as plt

top_categories = df["category"].value_counts().head(10)
plt.figure(figsize=(10,5))
top_categories.plot(kind="bar", color="skyblue")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.title("Top 10 Categories by Product Count")
plt.show()
