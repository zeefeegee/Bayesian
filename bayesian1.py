import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Define the prior: Uniform distribution between 1.65m and 1.8m
mu_values = np.linspace(1.65, 1.8, 50)  # 50 possible values for μ
prior = np.ones_like(mu_values) / len(mu_values)  # Uniform distribution

# Observed data: height = 1.7m
observed_height = 1.7
sigma = 0.1  # Assumed fixed standard deviation

# Compute likelihood: Normal PDF for each μ value
likelihood = stats.norm(mu_values, sigma).pdf(observed_height)

# Compute unnormalized posterior: prior * likelihood
unnormalized_posterior = prior * likelihood

# Normalize posterior (to ensure total probability sums to 1)
posterior = unnormalized_posterior / np.sum(unnormalized_posterior)

# Plot results
plt.figure(figsize=(10, 5))

plt.plot(mu_values, prior, label="Prior", linestyle="dashed")
plt.plot(mu_values, likelihood / np.sum(likelihood), label="Likelihood", linestyle="dotted")
plt.plot(mu_values, posterior, label="Posterior", linewidth=2)

plt.xlabel("Mean Height (μ)")
plt.ylabel("Probability Density")
plt.title("Bayesian Inference: Prior, Likelihood, and Posterior")
plt.legend()
plt.grid()
plt.show()