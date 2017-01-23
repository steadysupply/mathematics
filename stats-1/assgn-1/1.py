import math
import pandas as pd

DATA = [
    280, 155, 329, 140, 307,
    116, 202, 262, 130, 131,
    187, 187, 292, 83, 207,
    197, 134, 294, 163, 217
]

def main():
    series = pd.Series(DATA)
    mean = sum(DATA) / len(DATA)
    variance = sum([math.pow(sample - mean, 2) for sample in DATA]) / (len(DATA) - 1)

    print(mean)
    print(variance)

if __name__ == '__main__':
    main()
