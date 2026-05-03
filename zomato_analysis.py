import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r'C:\Users\musha\OneDrive\Desktop\zomato.csv', encoding='latin-1')

# Basic info
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
# Top 10 cities with most restaurants
city_counts = df['City'].value_counts().head(10)
plt.figure(figsize=(10,5))
plt.bar(city_counts.index, city_counts.values, color='orange')
plt.title('Top 10 Cities with Most Restaurants')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Rating Distribution
plt.figure(figsize=(8,5))
df['Rating text'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Restaurant Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Top 10 Cuisines
cuisine_counts = df['Cuisines'].value_counts().head(10)
plt.figure(figsize=(10,5))
cuisine_counts.plot(kind='barh', color='green')
plt.title('Top 10 Cuisines')
plt.xlabel('Count')
plt.tight_layout()
plt.show()
# Online Delivery Analysis
delivery = df['Has Online delivery'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(delivery.values, labels=delivery.index, autopct='%1.1f%%', colors=['lightgreen','salmon'])
plt.title('Online Delivery Available?')
plt.show()