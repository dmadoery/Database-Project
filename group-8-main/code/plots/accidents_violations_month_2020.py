import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mydata

# Generates png from accidents and violations in the year 2020 on a monthly scale.
try:
    width = 0.5
    # connect with the data base (enter own pwd)
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)

    # gets the data for speed violations with a specific query
    query = "select total as total_v, year, month from violations_perYear_monthly where year = 2020;"
    df = pd.read_sql(query, mydb)

    # gets the data for accidents with a specific query 
    query1 = "select total as total_a, year, month from accident_perYear_monthly where year = 2020;"
    df1 = pd.read_sql(query1, mydb)
    
    # plots the x axis with months and the first bar of accidents
    fig, ax = plt.subplots()
    fig1 = ax.bar(df['month'] - 0.35/2, df1['total_a'], color= 'steelblue', width=0.35)
    ax.set_xlabel('Month', fontsize= 16)
    ax.set_ylabel('Accidents', color ='steelblue', fontsize = 16)
    ax.bar_label(fig1, padding=2)
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])

    # plots the second bar of speed violations on the same x axis as above
    ax2 = ax.twinx()
    fig2 = ax2.bar(df['month'] + 0.35/2, df['total_v'], color = 'red', width= 0.35)
    ax2.set_ylabel('Speed Violations', color = 'red', fontsize = 16)
    ax2.bar_label(fig2, padding=2)

    ax.set_title('2020', fontsize= 24)
    
    # uncomment to get the plot
    # plt.show()

    # saves the figure created
    fig.set_size_inches((11, 5), forward=False)
    plt.savefig('rendered-images/accidents_violations/accidents_violations_2020_monthly.png', dpi=500)

    # close the connection
    mydb.close() 
except Exception as e:
    mydb.close()
    print(str(e))