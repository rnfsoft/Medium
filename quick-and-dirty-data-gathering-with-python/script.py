# https://towardsdatascience.com/quick-and-dirty-data-gathering-with-python-9d3d4b8cba13
import json
import os
import re

import folium
import pandas as pd
import requests
from shapely.geometry import Point  # pip install D:/Shapely‑1.6.4.post1‑cp36‑cp36m‑win_amd64.whl downloaded from https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely
from shapely.geometry.polygon import Polygon

def fileName(file_name):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)


def processResponse(r):
    #parse out each store's info
    stores = re.findall(r'"storeNumber":.*?"slug"', r)
    storeInfo = []
    for store in stores:
        #parse out info about each store
        storeInfo.append(list(re.findall(r'"storeNumber":"(.*?)".*?"name":"(.*?)".*?"latitude":(.*?),.*?"longitude":(.*?)}.*?"city":"(.*?)".*?"countrySubdivisionCode":"(.*?)".*?"postalCode":"(.*?)"', store)[0]))
    return storeInfo

with open(fileName('laZips.txt'), 'r') as f:
    laZips = [z.replace('\n', '') for z in f.readlines()]

    allStores = []

    for idx, z in enumerate(laZips):
        r = requests.get('https://www.starbucks.com/store-locator?place='+z)

        if r.status_code != 200:
            raise SystemExit
        
        storeInfoList = processResponse(r.text)

        for storeInfo in storeInfoList:
            storeInfo[6] = storeInfo[6][:5]
        
        allStores += storeInfoList

    print(allStores)

    seenStoreIds=[]
    laStores=[]
    for store in allStores:
        if store[0] in seenStoreIds:
            continue
        else:
            laStores.append(store)
            seenStoreIds.append(store[0])

    with open(fileName('laMap.json'), 'r') as f:
        laArea = json.load(f)
    laPolygon = Polygon(laArea['features'][0]['geometry']['coordinates'][0][0])

    keepLAStores=[]
    for store in laStores:
        point = Point(float(store[3]), float(store[2])) #  (long, lat) format instead of (lat, long)
        if laPolygon.contains(point):
            keepLAStores.append(store)   

    dfSbux = pd.DataFrame(columns=['id', 'strLocation', 'latitude', 'longitude', 'city', 'state', 'zip'])

    for i, col in enumerate(dfSbux.columns):
        dfSbux[col] = [item[i] for item in keepLAStores]

    dfSbux.latitude = dfSbux.latitude.apply(lambda x: float(x))
    dfSbux.longitude = dfSbux.longitude.apply(lambda x: float(x))

    dfSbux.to_csv(fileName('starbucksInLACounty.csv'), index=False)

    laMap = folium.Map(location=[34.0522, -118.2437], tiles="Stamen Toner", zoom_start=10)
    for i, row in dfSbux.iterrows():
        folium.CircleMarker((row.latitude, row.longitude), radius=3, weight=2, fill_color='red', fill_opacity=.9).add_to(laMap)
    folium.GeoJson(laArea).add_to(laMap)
    laMap.save(fileName('starbucksInLACounty.html'))