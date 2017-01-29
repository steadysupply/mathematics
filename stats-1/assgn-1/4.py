from scipy.stats import poisson
from numpy import power
mu = 2
dist = poisson(mu)
Fr7 = 0
r = 2
while Fr7 < 0.95:                # <-
    r = r + 1                    #   this is a loop
    Fr7 = power(dist.cdf(r), 7)  # <-
print("F_{0} gives {1}".format(r, Fr7))
