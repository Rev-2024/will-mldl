import scipy.stats as stats
import math
# Given data
sample_mean = 8
sample_std = 2
n = 20
mu_0 = 0  # hypothesized population mean
# Calculate t-statistic
t_stat = (sample_mean - mu_0) / (sample_std / math.sqrt(n))
# Degrees of freedom
df = n - 1
# Critical t-value for 95% confidence (two-tailed)
t_critical = stats.t.ppf(1 - 0.025, df)
# Output results
print(f"t-statistic: {t_stat:.4f}")
print(f"t-critical (±): ±{t_critical:.4f}")
# Decision
if abs(t_stat) > t_critical:
    print("Reject the null hypothesis: The drug has a significant effect on heart rate.")
else:
    print("Fail to reject the null hypothesis: No significant effect detected.")
