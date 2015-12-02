__author__ = 'Erez Levanon'

from buildPickle import buildDB
import pandas as pd
from dateFuctions import printTime

df = pd.DataFrame(pd.read_pickle("NY_min.p"))

mystart = 1449014401
myend = 1454371201

for i in df['availability']:
    for j in i:
        start = j['start']
        end = j['end']
        if not (end < mystart or start > myend):
            print(printTime(j['start']) + " to " + printTime(j['end']))
