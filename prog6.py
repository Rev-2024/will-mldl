import numpy as np
from statsmodels.stats.proportion import proportions_ztest,proportion_confint
# Data
conversions = np.array([120, 150])   # sales (successes)
views = np.array([1000, 1200])       # total users (trials)
alpha = 0.05
# Perform two-proportion z-test
stat, p_value = proportions_ztest(conversions, views)
(L1,L2),(L3,L4)=proportion_confint(conversions,views,alpha)
print("Z-statistic:", stat)
print("p-value:", p_value)
print(L1,L2)
print(L3,L4)
# Conclusion at 5% significance level
if p_value < alpha:
    print("Reject the null hypothesis: Significant difference in conversion rates.")
else:
    print("Fail to reject the null hypothesis: No significant difference in conversion rates.")
