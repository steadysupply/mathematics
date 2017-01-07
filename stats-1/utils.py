import numpy
from rpy2.robjects import pandas2ri
from rpy2.robjects import r

import operator

def avg(*series):
    return operator.add(*series) / len(series)

def r_dataset(name):
    r.data(name)
    return pandas2ri.ri2py(r[name])

def iqr(series):
    return numpy.subtract(*series.quantile([.75, .25]))
