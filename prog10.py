import numpy as np
# Given Poisson regression coefficients
intercept = 2.5
coef_age = -0.03
coef_condition = 0.5
# Patient information
age = 60
condition = 1  # 1 if patient has chronic condition, 0 otherwise
# Calculate log(lambda)
log_lambda = intercept + coef_age * age + coef_condition * condition
# Convert to expected number of visits
expected_visits = np.exp(log_lambda)
print(f"Expected number of visits (with chronic condition): {expected_visits:.2f}")
# If patient does NOT have chronic condition
condition = 0
log_lambda_no_condition = intercept + coef_age * age + coef_condition * condition
expected_visits_no_condition = np.exp(log_lambda_no_condition)
print(f"Expected number of visits (without chronic condition): {expected_visits_no_condition:.2f}")
