import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Car.csv")

# Keep only numerical columns
df_num = df.select_dtypes(include="number").dropna()

# Pair plot
sns.pairplot(df_num, diag_kind="kde")
plt.show()

# Correlation heatmap
sns.heatmap(df_num.corr(), annot=True, cmap="coolwarm", fmt=".2f", center=0)
plt.show()
