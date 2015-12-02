__author__ = 'Erez Levanon'

import pandas as pd
from dateFuctions import *
from buildPickle import *

df = readPickle('newNY_min.p')

count = 0
for i, val in df.iterrows():
    for j in val['availability']:
        count += 1
print(count)

print('-----------------------------------------')

ndf = removeTooEarly(df, 1449014401)
ndf = removeTooLate(ndf, 1454976001)

count = 0
for i, val in ndf.iterrows():
    for j in val['availability']:
        count += 1
print(count)


printAllDates(ndf)