import matplotlib.pyplot as plt
import math


def likelihood_from_gaussian(mu, sigma, x):
    return 1 / (sigma * (2 * math.pi)**0.5) * math.exp(-1 * (x - mu)**2 / (2 * sigma**2))


def get_posterior(prior_a, mu_a, sigma_a, prior_b, mu_b, sigma_b, x):
    left = likelihood_from_gaussian(mu_a, sigma_a, x)
    right = likelihood_from_gaussian(mu_b, sigma_b, x)
    return (left * prior_a) / (left * prior_a + right * prior_b)


# Q2.1
prior_p, prior_b = 0.25, 0.75
mu_p, mu_b = 50, 0
sigma_p, sigma_b = 12, 12
x = 25
# print(get_posterior(prior_p, mu_p, sigma_p, prior_b, mu_b, sigma_b, x))

# Q2.1 Challenge
vot = [-25, 0, 25, 50, 75]
posteriors = []
for x in vot:
    posteriors.append(get_posterior(prior_p, mu_p, sigma_p, prior_b, mu_b, sigma_b, x))
# print(posteriors)

# plt.plot(vot, posteriors)
# plt.xlabel('VOT')
# plt.ylabel('Posteriors')
# plt.title('Posteriors for VOTs')
# plt.show()

# Q2.1 for fun
# posteriors = []
# for x in range(-100, 110, 10):
#     posteriors.append(get_posterior(prior_p, mu_p, sigma_p, prior_b, mu_b, sigma_b, x))
# print(posteriors)
#
# plt.plot(range(-100, 110, 10), posteriors)
# plt.show()

# Q2.2
prior_p, prior_b = 0.25, 0.75
mu_p, mu_b = 50, 0
sigma_p, sigma_b = 12, 8
x = 25
# print(get_posterior(prior_p, mu_p, sigma_p, prior_b, mu_b, sigma_b, x))

# Q2.2 Challenge
vot = [-25, 0, 25, 50, 75]
posteriors = []
for x in vot:
    posteriors.append(get_posterior(prior_p, mu_p, sigma_p, prior_b, mu_b, sigma_b, x))
# print(posteriors)

# plt.plot(vot, posteriors)
# plt.xlabel('VOT')
# plt.ylabel('Posteriors')
# plt.title('Posteriors for VOTs with Different Variances')
# plt.show()

# Q2.3
prior_p, prior_b = 0.25, 0.75
mu_p, mu_b = 50, 0
sigma_p, sigma_b = 12, 8
x = -200
# print(get_posterior(prior_p, mu_p, sigma_p, prior_b, mu_b, sigma_b, x))

# Q2.3 Challenge
vot = [-50, -100, -150, -200]
posteriors = []
for x in vot:
    posteriors.append(get_posterior(prior_p, mu_p, sigma_p, prior_b, mu_b, sigma_b, x))
# print(posteriors)
#
# plt.plot(vot, posteriors)
# plt.xlabel('VOT')
# plt.ylabel('Posteriors')
# plt.title('Posteriors for very low VOTs')
# plt.show()
