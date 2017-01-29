import math
import pandas as pd

DATA = [
    280, 155, 329, 140, 307,
    116, 202, 262, 130, 131,
    187, 187, 292, 83, 207,
    197, 134, 294, 163, 217
]

series = pd.Series(DATA)
print("Sample mean: {0}".format(series.mean()))
print("Sample variance: {0}".format(series.var()))

