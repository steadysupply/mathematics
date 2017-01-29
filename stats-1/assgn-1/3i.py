from scipy.stats import binom
n, p = 3000, 0.002
dist = binom(n, p)
print(dist.pmf(1))
