import pandas as pd
import pandas as pd
import requests as req
import datetime as dt
import json
import os

def api_call(url_base,i):
    json_req = req.get(url_base.format(i))
    dfs = []
    if json_req.status_code == 200:
        jsonstr = json.loads(json_req.content)
        for dict_ in jsonstr["features"]: 
            dfs.append(pd.DataFrame(dict_["attributes"], index=[0]))
    return pd.concat(dfs)


def collect_mpi_data():
    # main function for running the api over the 200+ species and seasons
    url_base = "https://maps.mpi.govt.nz/wss/service/ags-relay/arcgis1/guest/arcgis/rest/services/MARINE/MARINE_Species_SPN/MapServer/{}/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    dfs = []
    for i in range(1,1000):
        try:
            dfs.append(api_call(url_base,i))
        except:
            print("Failed at request number {}. Exiting process".format(i))
            break
    pd.concat(dfs).to_csv("{}/myfishfinder/data/raw/mpiopendata/{}-{}-{}.csv".format(os.path.dirname(os.getcwd()),dt.datetime.now().year,dt.datetime.now().month,dt.datetime.now().day))
