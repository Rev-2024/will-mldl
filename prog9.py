import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
# dataset
data = {
    'Price': [200000, 250000, 300000, 320000, 350000, 400000, 420000, 450000, 500000, 550000],
    'SqFt': [1500, 1600, 1800, 1900, 2000, 2100, 2200, 2400, 2600, 2800]
}
df = pd.DataFrame(data)
# Define the spline term for SqFt with knot at 2000
df['sqft_knot'] = np.maximum(0, df['SqFt'] - 2000)
# Define independent variables (including intercept)
X = sm.add_constant(df[['SqFt', 'sqft_knot']])
y = df['Price']
# Fit linear regression with spline
model = sm.OLS(y, X).fit()
# Print summary
print(model.summary())
# Plot the fitted spline regression
plt.scatter(df['SqFt'], df['Price'], color='blue', label='Data')
plt.plot(df['SqFt'], model.predict(X), color='red', label='Spline Fit')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.title('Spline Regression of Price on Square Footage')
plt.legend()
plt.show()
