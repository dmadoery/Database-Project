import pandas as pd
import numpy as np
from pathlib import Path 

""" 
roughly cleans weather dataset
"""

def clean():
   inpath = Path('data\Basel Wetter 2 meteoblue.csv')
   outpath = Path('output\weather_withIndicator.csv')  
   # dani = Path('C:\Repos\database-project\data\\Basel Wetter 2 meteoblue.csv')

   df = pd.read_csv(inpath, sep=';')

   # rename columns, mostly change german to english description
   df.rename(columns={'timestamp':'timestamp','Basel Temperature [2 m elevation corrected]':'temperature',
   'Basel Sunshine Duration':'sunshineDuration','Basel Precipitation Total':'precipitation', 'Basel Snowfall Amount':'snowfall',
   'Basel Cloud Cover High [high cld lay]':'cloudCoverHigh', 'Basel Cloud Cover Medium [mid cld lay]':'cloudCoverMedium',
      'Basel Cloud Cover Low [low cld lay]':'cloudCoverLow', 'Basel Wind Speed [10 m]':'windSpeed', 
      'Basel Wind Direction [10 m]':'windDirection'}, inplace = True)

   # add identifier
   df['wcid'] =  np.arange(len(df))

   # normalize date attribute
   df['date'] = pd.to_datetime(pd.to_datetime(df['timestamp']).dt.date)
   df['hour'] = pd.to_datetime(df['timestamp']).dt.hour

   # create weather indicator
   df['weatherIndicator'] = df['temperature'] + (df['sunshineDuration'])/60 - 2*(df['snowfall']) - df['precipitation']

   outpath.parent.mkdir(parents=True, exist_ok=True)  
   df.to_csv(outpath, index=False) 
