import numpy as np
import pandas as pd

import utils

name = pd.Series(['John', 'Anne', 'Terry', 'Fred', 'Maria'])
exam1 = pd.Series([92, 54, 98, 62, 79])
exam2 = pd.Series([82, 96, 60, 55, 72])

df = pd.DataFrame({
    'Name': name,
    'Exam 1 Mark': exam1,
    'Exam 2 Mark': exam2,
    'Average': utils.avg(exam1, exam2),
})

df['Grade'] = pd.cut(
    df['Average'],
    bins=(0, 49, 69, 84, 100),
    labels=('D', 'C', 'B', 'A'),
)

print(df.sort_values('Average', ascending=False))
