import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
# Simulating a skewed salary distribution (lognormal for right skewness)
np.random.seed(42)
population_salaries = np.random.lognormal(mean=11, sigma=0.5, size=10000)  # Population
# Parameters for sampling
num_samples = 1000 # Only 10 samples
sample_size = 30   # Each sample has 50 engineers
sample_means = []  # Store mean salary of each sample
# Drawing random samples and computing sample means
for _ in range(num_samples):
    sample = np.random.choice(population_salaries, sample_size, replace=False)
    sample_means.append(np.mean(sample))
    #plt.hist(sample,bins=10)
    #plt.show()
#Plot histogram of sample means
plt.hist(sample_means, bins=20, density=True, color='yellow', edgecolor='black', alpha=0.6,
         label='Sample Means')
# KDE curve (smooth boundary line)
kde = gaussian_kde(sample_means)
x_vals = np.linspace(min(sample_means), max(sample_means), 200)
plt.plot(x_vals, kde(x_vals), color='green', linewidth=2, label='KDE Curve')
# Vertical lines: mean of sample means & population mean
plt.axvline(np.mean(sample_means), color='purple', linestyle='--', label='Mean of Sample Means')
#plt.axvline(np.mean(population_salaries), color='green', linestyle='--', label='Population Mean')

plt.title('Distribution of Sample Means (10 samples, n=50)')
plt.xlabel('Sample Mean Salary')
plt.ylabel('Density')
plt.legend()
plt.show()
