from scipy.stats import poisson
from numpy import power

mu = 2
dist = poisson(mu)
known_feasibile_stock_level = 7


def probabilities(stock):
    'Return probabilities for remaining stock levels'
    return [(stock - x, dist.pmf(x)) for x in range(0, stock)]

initial_probabilities = [
    (known_feasibile_stock_level - x, dist.cdf(x))
    for x in range(0, known_feasibile_stock_level)
]

def day(stock_probabilities, feasibility):
    import ipdb;ipdb.set_trace()
    feasible_probabilities = []
    for today_stock, today_probability in stock_probabilities:
        for tomorrow_stock, tomorrow_probability in probabilities(today_stock):
            if today_probability * tomorrow_probability > feasibility:
                feasible_probabilities.append(
                    (tomorrow_stock, tomorrow_probability)
                )
    return feasible_probabilities

day(initial_probabilities, 0.95)
