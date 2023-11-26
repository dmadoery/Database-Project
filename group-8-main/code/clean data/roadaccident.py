from pathlib import Path
import pandas as pd
import numpy as np

""" 
roughly cleans road accident dataset
"""

def clean():
      inpath = Path('data\\roadaccidents.csv')
      outpath = Path('output\\roadaccidents_cleaned.csv')  

      df = pd.read_csv(inpath, sep=';')

      # rename columns, mostly change german to english description
      df.rename(columns={'Geo Point':'geoPoint', 'Geo Shape':'geoShape', 
      'Eindeutiger Identifikator des Unfalls':'accidentID', 'Beschreibung zum Unfalltyp':'accidentDescription',
      'Beschreibung zum Unfalltyp (fr)':'accidentDescription(fr)', 
      'Beschreibung zum Unfalltyp (en)':'accidentDescription(en)', 
      'Beschreibung der Unfallschwerekategorie':'acciedentSeverity', 
      'Beschreibung der Unfallschwerekategorie (fr)':'acciedentSeverity(fr)', 
      'Beschreibung der Unfallschwerekategorie (en)':'acciedentSeverity(en)',
      'Unfall mit Fussgängerbeteiligung':'pedestrianInvilvement', 
      'Unfall mit Fahrradbeteiligung':'bicycleInvolvement',
      'Unfall mit Motorradbeteiligung': 'motorcycleInvolvement',
      'Beschreibung der Strassenart':'streetTypeDescription', 
      'Beschreibung der Strassenart (fr)':'streetTypeDescription(fr)',
      'Beschreibung der Strassenart (en)':'streetTypeDescription(en)', 
      'Unfallort Ost-Koordinaten':'eastCoordinates', 'Unfallort Nord-Koordinaten':'northCoordinates', 
      'Kanton':'canton', 'Gemeindenummer':'muncipalNumber', 'Unfalljahr':'accidentYear',
            'Unfallmonat':'accidentMonth', 'Unfallmonat.1':'accidentMonth2', 'Unfallmonat (fr)': 'accidenMonth(fr)', 
            'Unfallmonat (en)':'accidenMonth(en)','Wochentag':'weekday','Wochentag (fr)':'weekday(fr)',
            'Wochentag (en)':'weekday(en)', 'Unfallstunde':'accidentHour', 'Unfalldatum':'accidentDate',
            'Unfalltyp':'accidentType','Unfallschwerekategorie':'accidentSeverityCategory',
            'Strassenart':'streetType','Code des Wochentags':'weekdayCode',
            'Unfallstunde.1':'accidentHour'}, inplace = True)

      # add identifier
      df['aid'] = np.arange(len(df))
      # split geo point into latitude and longitude columns
      df[['latitude','longitude']] = df['geoPoint'].str.split(pat=',', expand=True)

      outpath.parent.mkdir(parents=True, exist_ok=True)
      df.to_csv(outpath, index=False)
