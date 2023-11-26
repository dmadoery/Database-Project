import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import querys
import strings
import warnings
import mydata

warnings.filterwarnings('ignore')


#not used


try:
    mydb = connection.connect(host="localhost", database = 'group8',user="root", passwdpasswd=mydata.getPwd(),use_pure=True)
    AllDays = []
    RainDays = []
    NoRainDays = []
    X = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for i in range(7):
        s = strings.getString(i, "allDays")
        df = pd.read_sql(s, mydb)
        AllDays.append(df["totalMotorVehicle"].mean())

    for i in range(7):
        s = strings.getString(i, "rainyDays")
        df = pd.read_sql(s, mydb)
        RainDays.append(df["totalMotorVehicle"].mean())
    
    for i in range(7):
        s = strings.getString(i, "noRain")
        df = pd.read_sql(s, mydb)
        NoRainDays.append(df["totalMotorVehicle"].mean())

    print(AllDays, RainDays, NoRainDays)

    X_axis = np.arange(len(X))

    
    plt.bar(X_axis - 0.2, AllDays, 0.2, label = 'AllDays')
    plt.bar(X_axis + 0.2, RainDays, 0.2, label = 'RainDays')
    plt.bar(X_axis , NoRainDays, 0.2, label = 'NoRainDays')
    
    plt.xticks(X_axis, X)
    plt.xlabel("Weekdays")
    plt.ylabel("Average MotorVehicle")
    plt.title("Average MotorVehicle on Weekdays depending on weather")
    plt.legend()
    plt.show()


    # print(df.head())
    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))