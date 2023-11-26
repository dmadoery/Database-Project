import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mydata

# Generates png from accidents and violations total form the years 2017-2021.
try:
    # connect with the data base (enter own pwd)
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)

    # gets the data for speed violations with a specific query
    query = "Select *, count(svid) as total_v from local_traffic_data where year(date) <= 2021"
    df = pd.read_sql(query, mydb)

    # gets the data for accidents with a specific query
    query1 = "select count(aid) as total_a from local_traffic_data where accidentYear >= 2017"
    df1 = pd.read_sql(query1, mydb)
    
    # plots the x axis 1 value and the first bar of accidents
    fig, ax = plt.subplots()
    fig1 = ax.bar(1 - 0.5, df1['total_a'], color = 'steelblue')
    ax.set_xlabel('2017 - 2021')
    ax.set_ylabel('Accidents', color ='steelblue', fontsize = 16)
    ax.bar_label(fig1, padding=2)
    ax.set_xticks([])

    # plots the second bar with speed violations on the same x axis as above
    ax2 = ax.twinx()
    fig2 = ax2.bar(1 + 0.5, df['total_v'], color = 'red')
    ax2.set_ylabel('Speed Violations', color = 'red', fontsize = 16)
    ax2.bar_label(fig2, padding=2)

    # uncomment to get the plot
    # plt.show()
    
    fig.set_size_inches((8.5, 5), forward=False)
    plt.savefig('rendered-images/accidents_violations/accidents_violations_2017-2021.png', dpi=500)
    
    # close the connection
    mydb.close() 
except Exception as e:
    mydb.close()
    print(str(e))