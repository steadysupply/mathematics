from scipy.stats import poisson
from numpy import power, product
mu = 2
dist = poisson(mu)
for r in range(6):
    result = product([power(dist.cdf(6), 6), dist.cdf(r)])
    print("(F_6)^6 * F_{0} gives {1}".format(r, result))
