# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("./sample_data/USA_Housing.csv") 

# Get the first 10 rows
print(df.head(10))

# Plot histogram of Price
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of House Prices")
plt.show()

# Plot histogram of Area Population
sns.histplot(df["Area Population"], kde=True)
plt.title("Distribution of Area Population")
plt.show()

# Scatter plot of Price vs. Area Population with hue and style
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Area Population", y="Price", hue="Avg. Area Number of Rooms", style="Avg. Area Number of Bedrooms", palette="coolwarm")
plt.title("House Price vs. Area Population")
plt.xlabel("Area Population")
plt.ylabel("Price")
plt.show()

# Pairplot with hue
sns.pairplot(df, hue="Avg. Area Number of Bedrooms", palette="coolwarm")
plt.show()