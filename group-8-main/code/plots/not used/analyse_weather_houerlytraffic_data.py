import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import querys
import strings
import mydata


#not used
try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwd=mydata.getPwd(),use_pure=True)
    AllDays = []
    RainDays = []
    NoRainDays = []
    X = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    query = querys.getQuery("allDays")

    for i in range(7):
        df = pd.read_sql(query[i], mydb)
        cursor = mydb.cursor()
        s = strings.getString(X[i], "allDays")
        cursor.execute(s)
        AllDays.append((cursor.fetchall()[0][0])/ np.arange(len(df)))
        # print(AllDays.append(df["speedViolations"].sum() / df["speedViolations"].size))

    query = querys.getQuery("rainyDays")

    for i in range(7):
        df = pd.read_sql(query[i], mydb)
        cursor = mydb.cursor()
        s = strings.getString(X[i], "rainyDays")
        cursor.execute(s)
        RainDays.append((cursor.fetchall()[0][0])/ np.arange(len(df)))
        # print(RainDays.append(df["speedViolations"].sum() / df["speedViolations"].size))

    query = querys.getQuery("noRain")

    for i in range(7):
        df = pd.read_sql(query[i], mydb)
        cursor = mydb.cursor()
        s = strings.getString(X[i], "noRain")
        cursor.execute(s)
        NoRainDays.append((cursor.fetchall()[0][0])/ np.arange(len(df)))
        # print(NoRainDays.append(df["speedViolations"].sum() / df["speedViolations"].size))


    
    
    
    X_axis = np.arange(len(X))
    
    plt.bar(X_axis - 0.2, AllDays, 0.2, label = 'AllDays')
    plt.bar(X_axis + 0.2, RainDays, 0.2, label = 'RainDays')
    plt.bar(X_axis , NoRainDays, 0.2, label = 'NoRainDays')
    
    plt.xticks(X_axis, X)
    plt.xlabel("Weekdays")
    plt.ylabel("Average Speedviolations")
    plt.title("Average SpeedViolations on Weekdays depending on weather")
    plt.legend()
    plt.show()


    # print(df.head())
    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))
