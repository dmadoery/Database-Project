import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def getQuery(text):
    if text == "allDays":

        query = []
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Monday' and weekday(d.date) = 'Monday';")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Tuesday' and weekday(d.date) =  'Tuesday';")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Wednesday' and weekday(d.date) =  'Wednesday';")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Thursday' and weekday(d.date) =  'Thursday';")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Friday' and weekday(d.date) = 'Friday';")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Saturday' and weekday(d.date) = 'Saturday';")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Sunday' and weekday(d.date) = 'Sunday';")

        return query
    
    if text == "rainyDays":
       
        query = []
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Monday' and weekday(d.date) = 'Monday' and precipitation > 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Tuesday' and weekday(d.date) = 'Tuesday' and precipitation > 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Wednesday' and weekday(d.date) = 'Wednesday' and precipitation > 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Thursday' and weekday(d.date) = 'Thursday' and precipitation > 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Friday' and weekday(d.date) = 'Friday' and precipitation > 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Saturday' and weekday(d.date) = 'Saturday' and precipitation > 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Sunday' and weekday(d.date) = 'Sunday' and precipitation > 0;")

        return query
    
    if text == "noRain":
        
        query = []
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Monday' and weekday(d.date) = 'Monday' and w.precipitation = 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Tuesday' and weekday(d.date) = 'Tuesday' and w.precipitation = 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Wednesday' and weekday(d.date) = 'Wednesday' and w.precipitation = 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Thursday' and weekday(d.date) = 'Thursday' and w.precipitation = 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Friday' and weekday(d.date) = 'Friday' and w.precipitation = 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Saturday' and weekday(d.date) = 'Saturday' and w.precipitation = 0;")
        query.append("Select d.speedViolations, w.temperature, w.precipitation from hourly_traffic_data d, meteoblue_weather w where Date(w.date) <= '2022-10-20' and Date(w.date) >= '2022-02-01' and  weekday(w.date) = 'Sunday' and weekday(d.date) = 'Sunday' and w.precipitation = 0;")

        return query