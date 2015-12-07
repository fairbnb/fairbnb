from buildPickle import *
from dateFuctions import *
from graphBuilder import *
from sys import argv

BIG_DF = './static/data/newNY.p'
WORK_DF = './static/data/newNY_min.p'



def userQuery(start_date, end_date):
    # filter Data frame
    df = readPickle(WORK_DF)
    df = removeTooEarly(df, start_date)
    df = removeTooLate(df, end_date + 14*DAY)
    df = clearNotAvailables(df)

    my_graph = buildGraph(df, start_date, end_date)
    result = nx.dijkstra_path(my_graph, source='start', target='end')
    printResultPath(result, my_graph)


if __name__ == '__main__':
    if len(argv) == 3:
        start = int(argv[1])
        end = int(argv[2])
    else:
        start = 1449496184 + DAY
        end = start + 40*DAY
    userQuery(start, end)

