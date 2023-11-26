from pathlib import Path
import pandas as pd
import numpy as np
import time

""" 
roughly cleans speed violations 2021 dataset
"""

def clean():
    inpath = Path('data\\100097-speed-2021.csv')
    outpath = Path('output\speed2021_cleaned.csv')  

    t1=time.time()

    print("Reading csv...")
    df = pd.read_csv(inpath, sep=';', dtype={'Hausnummer':'object'})

    print("Renaming columns...")
    df.rename(columns={'Timestamp':'timestamp', 'Messung-ID':'measureID', 'Richtung ID':'directionID', 
    'Geschwindigkeit':'speed', 'Zeit':'time', 'Datum':'date', 'Datum und Zeit':'dateAndTime', 
    'Messbeginn':'measureStart', 'Messende':'measureEnd', 'Zone':'zone', 'Ort':'location', 
    'Richtung':'direction', 'Geopunkt':'geoPoint', 'Übertretungsquote':'violationRate', 
    'Geschwindigkeit V50':'speedV50', 'Geschwindigkeit V85':'speedV85', 'Strasse':'street',
    'Hausnummer':'houseNr', 'Fahrzeuge':'vehicles', 'Fahrzeuglänge':'vehicleLength',
    'Kennzahlen pro Mess-Standort':'metricsPerLocation'}, inplace = True)

    print("Creating svid...")
    df['svid'] = np.arange(12*10**6, 12*10**6 + len(df), 1)
    print("Creating date...")
    df['date'] = pd.to_datetime(pd.to_datetime(df['timestamp'].str[:19]).dt.date)
    print("Creating hour...")
    df['hour'] = pd.to_datetime(df['timestamp'].str[:19]).dt.hour
    print("Creating violationDegree...")
    df['violationDegree'] = (100/df['zone'] * df['speed']) - 100
    print("Creating coordinates...")
    df[['latitude','longitude']] = df['geoPoint'].str.split(pat=',', expand=True)

    print("Writing file...")
    outpath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(outpath, index=False)

    t2= time.time()
    print("total time:", t2-t1)

    # print(df.columns)
    # print(df.loc[122])
    # print(df.head())