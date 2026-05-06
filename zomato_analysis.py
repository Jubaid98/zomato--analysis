import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data/zomato.csv', encoding='latin-1')

# Basic Info
print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nFirst 5 rows:")
print(df.head())

# Graph 1 - Top 10 Cities
city_counts = df['City'].value_counts().head(10)
plt.figure(figsize=(10,5))
plt.bar(city_counts.index, city_counts.values, color='orange')
plt.title('Top 10 Cities with Most Restaurants')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/top_cities.png')
plt.show()

# Graph 2 - Rating Distribution
plt.figure(figsize=(8,5))
df['Rating text'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Restaurant Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/ratings.png')
plt.show()

# Graph 3 - Top 10 Cuisines
cuisine_counts = df['Cuisines'].value_counts().head(10)
plt.figure(figsize=(10,5))
cuisine_counts.plot(kind='barh', color='green')
plt.title('Top 10 Cuisines')
plt.tight_layout()
plt.savefig('outputs/top_cuisines.png')
plt.show()

# Graph 4 - Online Delivery
plt.figure(figsize=(6,4))
df['Has Online delivery'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Online Delivery Available')
plt.savefig('outputs/online_delivery.png')
plt.show()

# Conclusions
print("\n===== ZOMATO ANALYSIS CONCLUSIONS =====")
print(f"Total Restaurants: {len(df)}")
print(f"Total Cities: {df['City'].nunique()}")
print(f"Top City: {df['City'].value_counts().index[0]}")