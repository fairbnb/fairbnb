__author__ = 'Erez Levanon'

import urllib.parse
import urllib.request
import json
import pandas as pd
import numpy

def buildDB(lat = '40.758895', long = '-73.9829423',dbName = "temp.p"):

    moreResults = 1;

    results = []
    count = 0;
    page = 1;

    url = 'https://zilyo.p.mashape.com/search'
    xmashkey = 'bFjnXwZZp5msh3AIkSIt8PDpsny3p18fuWtjsnDVIL0eN8gh27'
    accept = 'application/json'
    headers = { 'X-Mashape-Key' : xmashkey , 'Accept' : accept}
    values = {'latitude' : str(lat),
              'longitude' : str(long),
              'maxdistance':'80',
              'page':str(page),
              'resultsperpage':'50',
              'provider': 'airbnb'
              }

    data = urllib.parse.urlencode(values)
    url = url + "?" + data;
    data = data.encode('ascii')
    req = urllib.request.Request(url , headers=headers)
    with urllib.request.urlopen(req) as response:
        batch = json.loads(response.read().decode('utf-8'))
        df = pd.DataFrame(batch['result'])
    try:
        while moreResults != 0:
            page += 1;

            url = 'https://zilyo.p.mashape.com/search'
            xmashkey = 'bFjnXwZZp5msh3AIkSIt8PDpsny3p18fuWtjsnDVIL0eN8gh27'
            accept = 'application/json'
            headers = { 'X-Mashape-Key' : xmashkey , 'Accept' : accept}
            values = {'latitude' : str(lat),
              'longitude' : str(long),
              'maxdistance':'80',
              'page':str(page),
              'resultsperpage':'50',
              'provider': 'airbnb'
            }

            data = urllib.parse.urlencode(values)
            url = url + "?" + data;
            data = data.encode('ascii')
            req = urllib.request.Request(url , headers=headers)
            with urllib.request.urlopen(req) as response:
                batch = json.loads(response.read().decode('utf-8'))
                moreResults =  len(batch['result'])
                count+=moreResults
                print(count)
                df = pd.concat([df, pd.DataFrame(batch['result'])])
    finally:
        print(df.info())
        df.to_pickle(dbName)


def cleanDataFrame(path, newPath):
    df = pd.DataFrame(pd.read_pickle(path))
    df.reset_index(inplace=1)
    toDelete = ['attr', 'priceRange', 'photos', 'location', 'provider', 'amenities', 'reviews', 'latLng', 'itemStatus']
    for i in toDelete:
        df.pop(i)
    df.to_pickle(newPath)
    return df

def removeTooEarly(df, date):
    res = df.copy(deep=1)
    for j, row in res.iterrows():
        availability = row['availability']
        toPop = []
        for i in range(len(availability)):
            if row['availability'][i]['end'] < date:
                toPop.append(i)
        toPop.reverse()
        for k in toPop:
            availability.pop(k)
    return res

def removeTooLate(df, date):
    res = df.copy(deep=1)
    for j, row in res.iterrows():
        availability = row['availability']
        toPop = []
        for i in range(len(availability)):
            if row['availability'][i]['end'] > date:
                toPop.append(i)
        toPop.reverse()
        for k in toPop:
            availability.pop(k)
    return res


def readPickle(path):
    return pd.DataFrame(pd.read_pickle(path))