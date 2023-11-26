import roadaccident
import cycle_pedestrian_transit
import speed20
import speed21
import vehicle
import weather
import time

# execute from root directory with "py code/clean.py"
""" This script roughly cleans all chosen datasets. Make sure the datasets are in the /data folder. Time to run script is roughly around 10min. """

t1 = time.time()

print('Starting cleaning. Approximate runtime: 10min')
print('Cleaning vehicle database...')
vehicle.clean()
print('Cleaning weather database...')
weather.clean()
print('Cleaning roadaccident database...')
roadaccident.clean()
print('Cleaning cycle ped database...')
cycle_pedestrian_transit.clean()
print('Cleaning speed20 database...')
speed20.clean()
print('Cleaning speed21 database...')
speed21.clean()



t2 = time.time()
print('Execution time:', t2 - t1)

