import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mydata

# This file generates for every traffic type 8 different days on hourly scale with the temperature and rain or snow if there is any.
#####################################################################################################################################################################################################################################################################
# Bicycles
try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total1 as Cycles, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-02' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Cycles'], color = 'steelblue')
    ax.set_title("Sample 1: 2022-02-02 (Wednesday, Fasnacht)", fontsize=25)
    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Cycles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/cycle/2022-02-02-cyc.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total1 as Cycles, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-11' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Cycles'], color = 'steelblue')
    ax.set_title("Sample 2: 2022-02-11 (Friday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Cycles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['snowfall'], color = 'orange')
    ax3.set_ylabel('', color = 'orange')
    ax3.tick_params(axis='y', colors = 'orange')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/cycle/2022-02-11-cyc.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))



try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total1 as Cycles, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-14' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Cycles'], color = 'steelblue')
    ax.set_title("Sample 3: 2022-02-14 (Monday)", fontsize=25)
    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Cycles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/cycle/2022-02-14-cyc.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total1 as Cycles, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-04-01' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Cycles'], color = 'steelblue')
    ax.set_title("Sample 4: 2022-04-01 (Friday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Cycles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/cycle/2022-04-01-cyc.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total1 as Cycles, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-04-09' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Cycles'], color = 'steelblue')
    ax.set_title("Sample 5: 2022-04-09 (Saturday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Cycles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['snowfall'], color = 'orange')
    ax3.set_ylabel('', color = 'orange')
    ax3.tick_params(axis='y', colors = 'orange')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/cycle/2022-04-09-cyc.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total1 as Cycles, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-06-20' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Cycles'], color = 'steelblue')
    ax.set_title("Sample 6: 2022-07-19 (Monday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Cycles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/cycle/2022-06-20-cyc.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total1 as Cycles, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-07-17' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Cycles'], color = 'steelblue')
    ax.set_title("Sample 7: 2022-07-17 (Sunday)", fontsize=25)


    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Cycles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/cycle/2022-07-19-cyc.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total1 as Cycles, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-08-17' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Cycles'], color = 'steelblue')
    ax.set_title("Sample 8: 2022-08-17 (Wednesday)", fontsize=25)

    
    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Cycles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/cycle/2022-08-17-cyc.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

################################################################################################################################################################################################################################################
# Motorized Vehicles
try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select totalMotorVehicle as Motos, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-02' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Motos'], color = 'steelblue')
    ax.set_title("Sample 1: 2022-02-02 (Wednesday, Fasnacht)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Motor Vehicles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/moto/2022-02-02-moto.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select totalMotorVehicle as Motos, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-11' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Motos'], color = 'steelblue')
    ax.set_title("Sample 2: 2022-02-11 (Friday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Motor Vehicles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['snowfall'], color = 'orange')
    ax3.set_ylabel('', color = 'orange')
    ax3.tick_params(axis='y', colors = 'orange')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/moto/2022-02-11-moto.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))



try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select totalMotorVehicle as Motos, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-14' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Motos'], color = 'steelblue')
    ax.set_title("Sample 3: 2022-02-14 (Monday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Motor Vehicles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/moto/2022-02-14-moto.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select totalMotorVehicle as Motos, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-04-01' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Motos'], color = 'steelblue')
    ax.set_title("Sample 4: 2022-04-01 (Friday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Motor Vehicles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/moto/2022-04-01-moto.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select totalMotorVehicle as Motos, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-04-09' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Motos'], color = 'steelblue')
    ax.set_title("Sample 5: 2022-04-09 (Saturday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Motor Vehicles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red')
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['snowfall'], color = 'orange')
    ax3.set_ylabel('', color = 'orange', fontsize=18)
    ax3.tick_params(axis='y', colors = 'orange')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/moto/2022-04-09-moto.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select totalMotorVehicle as Motos, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-06-20' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Motos'], color = 'steelblue')
    ax.set_title("Sample 6: 2022-07-19 (Monday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Motor Vehicles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/moto/2022-06-20-moto.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select totalMotorVehicle as Motos, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-07-17' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Motos'], color = 'steelblue')
    ax.set_title("Sample 7: 2022-07-17 (Sunday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Motor Vehicles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/moto/2022-07-19-moto.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select totalMotorVehicle as Motos, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-08-17' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['Motos'], color = 'steelblue')
    ax.set_title("Sample 8: 2022-08-17 (Wednesday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Motor Vehicles', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red')
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green', fontsize=18)
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/moto/2022-08-17-moto.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

################################################################################################################################################################################################################################################
#Pedestrian
try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total0 as ped, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-02' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['ped'], color = 'steelblue')
    ax.set_title("Sample 1: 2022-02-02 (Wednesday, Fasnacht)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Pedestrians', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/ped/2022-02-02-ped.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total0 as ped, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-11' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['ped'], color = 'steelblue')
    ax.set_title("Sample 2: 2022-02-11 (Friday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Pedestrians', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['snowfall'], color = 'orange')
    ax3.set_ylabel('', color = 'orange')
    ax3.tick_params(axis='y', colors = 'orange')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/ped/2022-02-11-ped.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))



try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total0 as ped, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-14' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['ped'], color = 'steelblue')
    ax.set_title("Sample 3: 2022-02-14 (Monday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Pedestrians', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/ped/2022-02-14-ped.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total0 as ped, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-04-01' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['ped'], color = 'steelblue')
    ax.set_title("Sample 4: 2022-04-01 (Friday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Pedestrians', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/ped/2022-04-01-ped.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total0 as ped, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-04-09' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['ped'], color = 'steelblue')
    ax.set_title("Sample 5: 2022-04-09 (Saturday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Pedestrians', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['snowfall'], color = 'orange')
    ax3.set_ylabel('', color = 'orange')
    ax3.tick_params(axis='y', colors = 'orange')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/ped/2022-04-09-ped.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total0 as ped, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-06-20' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['ped'], color = 'steelblue')
    ax.set_title("Sample 6: 2022-07-19 (Monday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Pedestrians', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/ped/2022-06-20-ped.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total0 as ped, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-07-17' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['ped'], color = 'steelblue')
    ax.set_title("Sample 7: 2022-07-17 (Sunday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Pedestrians', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/ped/2022-07-19-ped.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select total0 as ped, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-08-17' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['ped'], color = 'steelblue')
    ax.set_title("Sample 8: 2022-08-17 (Wednesday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Total Pedestrians', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/ped/2022-08-17-ped.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


################################################################################################################################################################################################################################################
#Speed Violations
try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select speedViolations as speed, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-02' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['speed'], color = 'steelblue')
    ax.set_title("Sample 1: 2022-02-02 (Wednesday, Fasnacht)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Speed Violations', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/speed/2022-02-02-speed.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select speedViolations as speed, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-11' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['speed'], color = 'steelblue')
    ax.set_title("Sample 2: 2022-02-11 (Friday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Speed Violations', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['snowfall'], color = 'orange')
    ax3.set_ylabel('', color = 'orange')
    ax3.tick_params(axis='y', colors = 'orange')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/speed/2022-02-11-speed.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))



try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select speedViolations as speed, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-02-14' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['speed'], color = 'steelblue')
    ax.set_title("Sample 3: 2022-02-14 (Monday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Speed Violations', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/speed/2022-02-14-speed.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select speedViolations as speed, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-04-01' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['speed'], color = 'steelblue')
    ax.set_title("Sample 4: 2022-04-01 (Friday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Speed Violations', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/speed/2022-04-01-speed.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select speedViolations as speed, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-04-09' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['speed'], color = 'steelblue')
    ax.set_title("Sample 5: 2022-04-09 (Saturday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Speed Violations', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['snowfall'], color = 'orange')
    ax3.set_ylabel('', color = 'orange')
    ax3.tick_params(axis='y', colors = 'orange')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/speed/2022-04-09-speed.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select speedViolations as speed, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-06-20' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['speed'], color = 'steelblue')
    ax.set_title("Sample 6: 2022-07-19 (Monday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Speed Violations', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/speed/2022-06-20-speed.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select speedViolations as speed, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-07-17' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['speed'], color = 'steelblue')
    ax.set_title("Sample 7: 2022-07-17 (Sunday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Speed Violations', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    # ax3 = ax.twinx()
    # ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    # ax3.set_ylabel('', color = 'green')
    # ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/speed/2022-07-19-speed.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))

try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    query = "select speedViolations as speed, m.temperature, m.precipitation, h.date, h.hour, m.snowfall from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.date = '2022-08-17' and h.hour = m.hour order by h.date, h.hour;"
    df = pd.read_sql(query, mydb)
    
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['hour'], df['speed'], color = 'steelblue')
    ax.set_title("Sample 8: 2022-08-17 (Wednesday)", fontsize=25)

    ax.set_xlabel('Hour', fontsize=18)
    ax.set_ylabel('Speed Violations', color = 'steelblue', fontsize=18)
    ax.tick_params(axis='y', colors = 'steelblue')
    ax.bar_label(fig1, padding=4)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['temperature'], color = 'red')
    ax2.set_ylabel('Temperature', color = 'red', fontsize=18)
    ax2.tick_params(axis='y', colors = 'red')

    ax3 = ax.twinx()
    ax3.scatter(df['hour'], df['precipitation'], color = 'green')
    ax3.set_ylabel('', color = 'green')
    ax3.tick_params(axis='y', colors = 'green')

    # plt.show()
    fig.set_size_inches((15.3, 9), forward=False)
    plt.savefig('rendered-images/speed/2022-08-17-speed.png', dpi=300)

    mydb.close() # close the connection
except Exception as e:
    mydb.close()
    print(str(e))