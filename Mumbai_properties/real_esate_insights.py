import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("c://Users//hp//OneDrive//Deskstop//Mumbai_properties//Mumbai1.csv")

print("First few rows of the dataset:")
print(df.head())

df.rename(columns={'Price per sq ft.': 'price_per_sqft'}, inplace=True)

df.dropna(subset=['price_per_sqft', 'Location', 'No. of Bedrooms'], inplace=True)

df['price_per_sqft'] = pd.to_numeric(df['price_per_sqft'], errors='coerce')
df['No. of Bedrooms'] = pd.to_numeric(df['No. of Bedrooms'], errors='coerce')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

df.dropna(subset=['price_per_sqft', 'Price', 'No. of Bedrooms'], inplace=True)

avg_price_location = df.groupby('Location')['price_per_sqft'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_price_location.values, y=avg_price_location.index)
plt.title("Top 10 Locations by Average Price per sq ft")
plt.xlabel("Average Price per sq ft (INR)")
plt.ylabel("Location")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['price_per_sqft'], bins=30, kde=True)
plt.title("Price per sq ft Distribution")
plt.xlabel("Price per sq ft (INR)")
plt.ylabel("Number of Properties")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='No. of Bedrooms', y='price_per_sqft', data=df)
plt.title("Bedrooms vs Price per sq ft")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Price per sq ft (INR)")
plt.tight_layout()
plt.show()

numeric_df = df.select_dtypes(include='number')  
numeric_df = numeric_df.dropna(axis=1, how='all') 

if not numeric_df.empty and numeric_df.shape[1] > 1:
    plt.figure(figsize=(6, 5))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()
else:
    print("Not enough valid numeric data for correlation heatmap.")

df['price_per_sqft'] = df['Price'] / df['Area']
df['BHK_Category'] = df['No. of Bedrooms'].apply(lambda x: '1BHK' if x == 1 else ('2BHK' if x == 2 else ('3BHK' if x == 3 else '4+BHK')))
print(df['Price'].unique()[:20])

