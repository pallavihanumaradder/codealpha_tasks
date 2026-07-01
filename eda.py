import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("books_dataset.csv")

# 2. Clean the data (Remove the '£' currency symbol)
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# 3. Calculate metrics
print("--- Statistical Summary of Book Prices ---")
print(df['Price'].describe())

# 4. Generate a visualization chart
plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], kde=True, color='skyblue')
plt.title('Distribution of Scraped Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Count')

# 5. Save the chart image
plt.savefig('price_distribution.png')
print("\nTask 2 Complete! Chart saved as 'price_distribution.png'")
