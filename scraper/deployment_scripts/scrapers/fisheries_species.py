from bs4 import BeautifulSoup
import pandas as pd
import requests as req
import datetime as dt


def run_fisheries_collector():
    # Output: 2016 - Current species fisheries data
    # Set the columns for the dataframe
    columns = [
        "SpeciesCode",
        "Name",
        "ReportedCommCatch_kg",
        "TACC_kg",
        "CustAllow_kg",
        "RecAllow_kg",
        "TargetFishery",
        "BycatchFishery",
        "InQMS",
        "Year"
    ]
    # Get the current year to run though - back to 2016
    year = dt.datetime.now().year
    data = []
    for i in range(2016,year+1):
        rq = req.get("https://fs.fish.govt.nz/Page.aspx?pk=6&tk=97&ey={}".format(i))
        html = BeautifulSoup(rq.content)
        for row in html.select("tr.ItemRow"):
            # Includes year
            data.append([d.text.replace("\n","").replace(",","") for d in row.select("td")] + [i])
    df = pd.DataFrame(data=data,columns=columns)
    # Save ouput
    df.to_csv("scraper/data/raw/fisheries/species/{}-{}-{}.csv".format(dt.datetime.now().year,dt.datetime.now().month,dt.datetime.now().day))