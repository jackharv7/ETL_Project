from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import matplotlib as plt

years = []
for x in range(20):
    years.append(2000 + x)

url = "https://www.basketball-reference.com/friv/standings.fcgi?month=2&day=13&year=1992&lg_id=NBA"

stats = {}
for year in years:
    stats[year] = {
        "stats": pd.read_html(f"https://www.basketball-reference.com/friv/standings.fcgi?month=2&day=13&year={year}&lg_id=NBA")
    }

for year in years:
    stats[year]["stats"][0] = stats[year]["stats"][0].rename(columns={"Eastern Conference":"Team Name"})
    stats[year]["stats"][1] = stats[year]["stats"][1].rename(columns={"Western Conference":"Team Name"})

data = {}
for year in years:
    data[year] = {
        'w/l' : stats[year]["stats"][0][['Team Name','W/L%']].dropna(),
        'w/l1' : stats[year]["stats"][1][['Team Name','W/L%']].dropna()
    }
win_pct = {}
for year in years:
    win_pct[year] = {
        'all': pd.concat([data[year]['w/l'],data[year]['w/l1']])
    }
for year in years:
    win_pct[year]['all']['Team Name'] = win_pct[year]['all']["Team Name"].apply(lambda x: x.replace('*', ''))

data2 = pd.merge(win_pct[2000]['all'], win_pct[2001]['all'], on='Team Name', how="outer")
data2 = pd.merge(data2, win_pct[2002]['all'], on='Team Name', how="outer")
data2 = pd.merge(data2, win_pct[2003]['all'], on='Team Name', how="outer")
data2 = pd.merge(data2, win_pct[2004]['all'], on='Team Name', how="outer")
data2 = pd.merge(data2, win_pct[2005]['all'], on='Team Name', how="outer")
data2 = pd.merge(data2, win_pct[2006]['all'], on='Team Name', how="outer")
data2 = pd.merge(data2, win_pct[2007]['all'], on='Team Name', how="outer")
data2 = pd.merge(data2, win_pct[2008]['all'], on='Team Name', how="outer")
data2 = pd.merge(data2, win_pct[2009]['all'], on='Team Name', how="outer")

data2.columns = ['Team Name', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009']
    
data3 = pd.merge(win_pct[2010]['all'], win_pct[2011]['all'], on='Team Name', how="outer")
data3 = pd.merge(data3, win_pct[2012]['all'], on='Team Name', how="outer")
data3 = pd.merge(data3, win_pct[2013]['all'], on='Team Name', how="outer")
data3 = pd.merge(data3, win_pct[2014]['all'], on='Team Name', how="outer")
data3 = pd.merge(data3, win_pct[2015]['all'], on='Team Name', how="outer")
data3 = pd.merge(data3, win_pct[2016]['all'], on='Team Name', how="outer")
data3 = pd.merge(data3, win_pct[2017]['all'], on='Team Name', how="outer")
data3 = pd.merge(data3, win_pct[2018]['all'], on='Team Name', how="outer")
data3 = pd.merge(data3, win_pct[2019]['all'], on='Team Name', how="outer")

data3.columns = ['Team Name', '2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018', '2019']

full = pd.merge(data2, data3, on='Team Name', how="outer")

full_data = full.replace({"New Jersey Nets": "Brooklyn/NJ Nets","Brooklyn Nets": "Brooklyn/NJ Nets", "New Orleans Hornets": "New Orleans Hornets/Pelicans", "New Orleans Pelicans": "New Orleans Hornets/Pelicans", "New Orleans/Oklahoma City Hornets":"New Orleans Hornets/Pelicans", "Charlotte Bobcats":"Charlotte Hornets/Bobcats", "Charlotte Hornets":"Charlotte Hornets/Bobcats", "Memphis Grizzlies": "Memphis Grizzlies", "Vancouver Grizzlies": "Memphis Grizzlies", "Seattle SuperSonics":"Oklahoma City Thunder(SS)", "Oklahoma City Thunder": "Oklahoma City Thunder(SS)"})

full_data = full_data.groupby("Team Name").mean().reset_index()
full_data['20 Yr Avg'] = full_data.mean(axis=1).round(3)

url = "https://geojango.com/pages/list-of-nba-teams"
data = pd.read_html(url)
nba_info = pd.DataFrame(data[0])
nba_states = [i.split(',', 1)[1] for i in nba_info['Arena Location']]
nba_states[-1] = 'Washington, D.C'

full_data['State'] = nba_states

full_data.to_csv(r'nba.csv')