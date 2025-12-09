#Import libraries
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# Step 1: Load dataset
df=pd.read_csv("Salary_Data.csv")
#print(df)
# Step 2: Add a simulated 'Education' categorical variable
# We'll assign education levels based on experience range (just for illustration)
conditions = [
    (df['Experience']< 5),
    (df['Experience'].between(5, 10)),
    (df['Experience']> 10)
]
choices = ["Bachelor's", "Master's","PhD"]
df['Education'] = np.select(conditions, choices, default="Unknown")
df['Salary_Normalized'] = (df['Salary'] - df['Salary'].mean()) / df['Salary'].std()
# Step 3: Fit multiple linear regression model
model = smf.ols("Salary_Normalized ~ C(Education) + Experience", data=df).fit()

# Step 4: Show results
print(model.summary())

# Step 5: Interpret coefficients
print("\n--- Interpretation ---")
print("1️⃣ Intercept → Estimated salary for Bachelor's (baseline) with 0 years of experience.")
print("2️⃣ C(Education)[T.Master's] → Average salary differences between Bachelor's and High School (holding experience constant).")
print("3️⃣ C(Education)[T.PhD] → Average salary difference between Master's and High School (holding experience constant).")
print("4️⃣ YearsExperience → Estimated increase in salary per additional year of experience, regardless of education.")
