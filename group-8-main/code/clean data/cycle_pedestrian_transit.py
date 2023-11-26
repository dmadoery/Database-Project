from pathlib import Path
import pandas as pd
import numpy as np

""" 
roughly cleans cycle pedestrian transit dataset
"""

def clean():
    inpath = Path('data\\100013-cycle-ped.csv')
    outpath = Path('output\cycle_ped_cleaned.csv')  

    df = pd.read_csv(inpath, sep=';')

    # rename columns, mostly change german to english description
    df.rename(columns={'ZST_NR':'zst_nr','SiteCode':'siteCode','SiteName':'SiteName','DateTimeFrom':'dateTimeFrom','DateTimeTo':'dateTimeTo',
    'DirectionName':'directionName','LaneCode':'laneCode','LaneName':'laneName','ValuesApproved':'valuesApproved','ValuesEdited':'valuesEdited',
    'TrafficType':'trafficType','Total':'total','Year':'year','Month':'month','Day':'day','Weekday':'weekday','HourFrom':'hourFrom','Date':'date',
    'TimeFrom':'timeFrom','TimeTo':'timeTo','DayOfYear':'dayOfYear','Zst_id':'zst_id','Geo Point':'geoPoint'}, inplace = True)

    # add identifier
    df['cptid'] = np.arange(len(df))
    # normalize date attribute
    df['date'] = pd.to_datetime(df['dateTimeFrom'].str[:10]).dt.date
    # add hour attribute
    df['hour'] = pd.to_datetime(df['dateTimeFrom'].str[:19]).dt.hour
    # split geo point into latitude and longitude columns
    df[['latitude','longitude']] = df['geoPoint'].str.split(pat=',', expand=True)

    outpath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(outpath, index=False)
