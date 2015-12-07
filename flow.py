from buildPickle import *
from dateFuctions import *
from graphBuilder import *

BIG_DF = 'newNY.p'
WORK_DF = 'newNY_min.p'


def userQuery(start_date, end_date):
    # filter Data frame
    df = readPickle(WORK_DF)
    df = removeTooEarly(df, start_date)
    df = removeTooLate(df, end_date + 14*DAY)
    df = clearNotAvailables(df)

    my_graph = buildGraph(df, start_date, end_date)
    result = nx.dijkstra_path(my_graph, source='start', target='end')
    printResultPath(result, my_graph)


start = 1449335766
end = 1454198401
userQuery(start + DAY, end)