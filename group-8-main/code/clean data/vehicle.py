import pandas as pd
import numpy as np
from pathlib import Path  

""" 
roughly cleans vehicle transit dataset
"""

def clean():
    inpath = Path('data\\vehicle transit.csv')
    outpath = Path('output\\vehicle_density.csv')  

    df = pd.read_csv(inpath, sep=';')

    # rename columns, mostly change german to english description
    df.rename(columns = {'Fahrzeugklasse':'vehicleClass', 'Zeitstempel':'timestamp','timestamp_text': 'timestampText', 'Klassifizierungsindex':'classificationIndex'}, inplace = True)

    # generate date hour columns
    df['date'] = pd.to_datetime(df['timestamp'].str[:10])
    df['time'] = pd.to_datetime(df['timestamp'].str[:19])

    df['hour'] = df['time'].dt.hour
    a = df.groupby(['date', 'hour', 'vehicleClass']).size().reset_index(name='total') 
    a.insert(loc=0, column='vdid', value=np.arange(len(a)))


    outpath.parent.mkdir(parents=True, exist_ok=True)  
    a.to_csv(outpath, index=False)  
