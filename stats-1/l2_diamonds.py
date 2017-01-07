import csv
import utils
import pandas

import matplotlib
from matplotlib import pyplot

matplotlib.style.use('ggplot')
diamonds = pandas.read_csv('diamonds.csv')
# write plot
(
    diamonds['price']
        .plot(kind='hist', title='Diamond prices')
        .figure.savefig('diamonds.svg')
)
