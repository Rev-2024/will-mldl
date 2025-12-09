from scipy import stats
import math
# Given data
old_mean = 200        # mean calories of old recipe
sample_mean = 190     # mean calories of new recipe
sample_std = 15       # standard deviation of new recipe
n = 40                # sample size
alpha = 0.05          # significance level
# Calculate t-statistic
t_stat = (sample_mean - old_mean) / (sample_std / math.sqrt(n))
# Degrees of freedom
df = n - 1
# One-tailed p-value (testing if new mean < old mean)
p_value = stats.t.cdf(t_stat, df=df)
# Print results
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_value:.5f}")
# Conclusion
if p_value < alpha:
    print("Reject the null hypothesis: The new recipe has significantly fewer calories.")
else:
    print("Fail to reject the null hypothesis: No significant difference in calories.")
