from scipy.stats import norm
mu = 0.002
dist = norm(mu, mu)
print(dist.pdf(1))
