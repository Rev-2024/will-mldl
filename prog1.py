import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load dataset manually from a CSV file
df = pd.read_csv('Housing.csv')  # Replace with your actual file path

# Inspect column names to find the price column
print("Available columns:", df.columns)

# Assuming the price column is named 'Price' or 'SalePrice'
price_column = 'price' if 'price' in df.columns else 'SalePrice'

# Calculate IQR
Q1 = df[price_column].quantile(0.25)
Q3 = df[price_column].quantile(0.75)
IQR = Q3 - Q1

# Display results
print(f"Q1 (25th percentile): ${Q1:,.2f}")
print(f"Q3 (75th percentile): ${Q3:,.2f}")
print(f"IQR (Interquartile Range): ${IQR:,.2f}")

# Create a boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df[price_column], color='skyblue')

# Add title and labels
plt.title('Boxplot of Housing Prices')
plt.xlabel('Price')

# Show plot
plt.show()
