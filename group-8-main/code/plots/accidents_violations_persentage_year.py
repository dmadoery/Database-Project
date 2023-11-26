import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mydata

# Generates png from accidents and violations in from the year 2017-2021.
try:
    width = 0.35
    # connect with the data base (enter own pwd)
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)

    # gets the data for speed violations with a specific query
    query = "select * from persentage_violation_year;"
    df = pd.read_sql(query, mydb)

    # gets the data for accidents with a specific query
    query1 = "select count(aid) as total_a, accidentYear from local_traffic_data where accidentYear >= 2017 group by accidentYear order by accidentYear;"
    df1 = pd.read_sql(query1, mydb)
    
    # plots the x axis with years and the first bar of accidents
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['year']- width/2, df1['total_a'], width = 0.35, color = 'steelblue')
    ax.set_xlabel('Year')
    ax.set_ylabel('Accidents', color ='steelblue', fontsize = 16)
    ax.bar_label(fig1, padding=2)
    ax.set_xticks([2017,2018,2019,2020,2021])

    # plots the second bar with speed violations in percentange on the same x axis as above
    ax2 = ax.twinx()
    fig2 = ax2.bar(df['year'] + width/2, 100/(df['vio'] + df['noVio'])*df['vio'], width = 0.35, color = 'red')
    ax2.set_ylabel('Speed Violations in %', color = 'red', fontsize = 16)
    ax2.bar_label(fig2, padding=2)

    # uncomment to get the plot
    # plt.show()
    
    # saves the figure created
    fig.set_size_inches((11, 5), forward=False)
    plt.savefig('rendered-images/accidents_violations/accidents_violations_perYear_percentage.png', dpi=500)

    # close the connection
    mydb.close() 
except Exception as e:
    mydb.close()
    print(str(e))