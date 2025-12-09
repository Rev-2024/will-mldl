from scipy import stats
import numpy as np
# Given data
mean_A = 1000
std_A = 100
n_A = 30

mean_B = 950
std_B = 120
n_B = 30

# Step 1: Generate random samples (based on given statistics)
# Assuming sales follow a normal distribution
np.random.seed(42)  # for reproducibility
store_A = np.random.normal(mean_A, std_A, n_A)
store_B = np.random.normal(mean_B, std_B, n_B)

# Step 2: Perform two-sample t-test (Welch’s test, unequal variances)
t_stat, p_value = stats.ttest_ind(store_A, store_B, equal_var=False)

# Step 3: Display results
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_value:.4f}")

# Step 4: Conclusion
alpha = 0.05
if p_value < alpha:
    print("✅ Reject the null hypothesis: Significant difference between the two stores’ sales.")
else:
    print("❌ Fail to reject the null hypothesis: No significant difference between the two stores’ sales.")
