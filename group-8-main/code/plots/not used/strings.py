import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def getString(text, q):
    text = str(text)
    if q == "allDays":
        string = "Select speedViolations from hourly_traffic_data d, meteoblue_weather w where weekday(d.date) = '" + text +"' and w.date = d.date"
        return string
    
    if q == "rainyDays":
        string = "SELECT speedViolations from hourly_traffic_data d, meteoblue_weather w where (w.precipitation > 0 or w.snowfall > 0) and  weekday(d.date) = '" + text + "' and w.date = d.date"
        return string

    if q == "noRain":
        string = "SELECT speedViolations from hourly_traffic_data d, meteoblue_weather w where (w.precipitation = 0 and w.snowfall = 0) and weekday(d.date) = '" + text + "' and w.date = d.date"
        return string