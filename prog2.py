import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('customer_satisfaction.csv')

# Preview the data
print(df.head())
print(df['Satisfaction'].value_counts())
print(df['RepeatPurchase'].value_counts())
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Satisfaction', hue='RepeatPurchase', palette='Set2')

plt.title('Repeat Purchases by Satisfaction Level')
plt.xlabel('Customer Satisfaction')
plt.ylabel('Number of Customers')
plt.legend(title='Repeat Purchase')
plt.show()
### Create a crosstab
##ct = pd.crosstab(df['Satisfaction'], df['RepeatPurchase'])
##
### Plot stacked bar chart
##ct.plot(kind='bar', stacked=True, color=['salmon', 'lightgreen'], figsize=(8, 5))
##
##plt.title('Stacked Bar Chart: Satisfaction vs Repeat Purchase')
##plt.xlabel('Customer Satisfaction')
##plt.ylabel('Number of Customers')
##plt.legend(title='Repeat Purchase')
##plt.show()##

