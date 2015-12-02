import time

def printTime(unix):
    mytime = time.gmtime(unix)
    return time.strftime("%a, %d %m %Y", mytime)