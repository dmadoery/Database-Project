import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mydata

#Genearates all average traffic data per weekday. Every section generates a different traffic type 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Pedestrian
try:
    # connect with the data base (enter own pwd)
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    
    # gets the data for the traffic type with a specific query
    query = "select avg(avg_ped) as ped, weekday, avg(avg_temp) as temperature from avg_traffic_data group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    # plots the x axis with weekdays and an bar of the traffic type average
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['ped'], color = 'steelblue')

    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Pedestrians on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    # plots a scatter of the temperature average on the same x axis as above
    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    # saves the figure created
    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/ped/avg_ped_all.png', dpi=500)

    # uncomment to get the plot
    # plt.show()

    # close the connection
    mydb.close() 
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_ped) as ped, weekday, avg(avg_temp) as temperature from avg_traffic_data where avg_rain > 0 group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['ped'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Pedestrians on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/ped/avg_ped_rain.png', dpi=500)
    # plt.show()


    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_ped) as ped, weekday, avg(avg_temp) as temperature from avg_traffic_data where avg_rain = 0 group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['ped'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Pedestrians on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/ped/avg_ped_clear.png', dpi=500)
    # plt.show()


    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Bicycles
try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_cyc) as cycle, weekday, avg(avg_temp) as temperature from avg_traffic_data group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['cycle'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Cycles on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/cycle/avg_cycle_all.png', dpi=500)
    # plt.show()

    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_cyc) as cycle, weekday, avg(avg_temp) as temperature from avg_traffic_data where avg_rain > 0 group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['cycle'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Cycles on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/cycle/avg_cycle_rain.png', dpi=500)
    # plt.show()


    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_cyc) as cycle, weekday, avg(avg_temp) as temperature from avg_traffic_data where avg_rain = 0 group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['cycle'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Cycles on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/cycle/avg_cycle_clear.png', dpi=500)
    # plt.show()


    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Motorized Vehicles
try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_moto) as moto, weekday, avg(avg_temp) as temperature from avg_traffic_data group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['moto'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Motor Vehicles on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/moto/avg_moto_all.png', dpi=500)
    # plt.show()

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_moto) as moto, weekday, avg(avg_temp) as temperature from avg_traffic_data where avg_rain > 0 group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['moto'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Motor Vehicles on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/moto/avg_moto_rain.png', dpi=500)
    # plt.show()


    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_moto) as moto, weekday, avg(avg_temp) as temperature from avg_traffic_data where avg_rain = 0 group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['moto'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Average Motor Vehicles on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/moto/avg_moto_clear.png', dpi=500)
    # plt.show()


    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Speed Violations
try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_speedViolations) as speed, weekday, avg(avg_temp) as temperature from avg_traffic_data group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['speed'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Avg Amount Speed Violations on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/speed/avg_speed_all.png', dpi=500)
    # plt.show()

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_speedViolations) as speed, weekday, avg(avg_temp) as temperature from avg_traffic_data where avg_rain > 0 group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['speed'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Avg Amount Speed Violations on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/speed/avg_speed_rain.png', dpi=500)
    # plt.show()


    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select avg(avg_speedViolations) as speed, weekday, avg(avg_temp) as temperature from avg_traffic_data where avg_rain = 0 group by weekday;"  # all: without where clause, clear: where avg_rain = 0, Rain: where avg_rain > 0
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['weekday'], df['speed'], color = 'steelblue')
    ax.set_xlabel('Weekday', fontsize=16)
    ax.set_ylabel('Avg Amount Speed Violations on Weekdays', color ='steelblue', fontsize=16)
    ax.bar_label(fig1, padding=2)

    ax2 = ax.twinx()
    ax2.scatter(df['weekday'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=16)

    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/avg-traffic-data/speed/avg_speed_clear.png', dpi=500)
    # plt.show()


    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))