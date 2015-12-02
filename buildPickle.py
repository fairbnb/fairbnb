__author__ = 'Erez Levanon'

import urllib.parse
import urllib.request
import json
import pandas as pd
import numpy

def buildDB(lat = '40.758895', long = '-73.9829423', stime = '1449014401', etime = '1454371201' ,dbName = "temp.p"):

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
              'etimestamp': str(etime),
              'maxdistance':'80',
              'page':str(page),
              'resultsperpage':'50',
              'stimestamp':str(stime),
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
            values = {'latitude' : '40.758895',
                      'longitude' : '-73.9829423',
                      'etimestamp': '1454371201',
                      'maxdistance':'80',
                      'page':str(page),
                      'resultsperpage':'50',
                      'stimestamp':'1449014401',
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