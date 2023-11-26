create table avg_traffic_data select h.date as date, weekday(h.date) as weekday, avg(total0) as avg_ped, avg(total1) as avg_cyc, avg(totalMotorVehicle) as avg_moto, avg(speedViolations) as avg_speedViolations, avg(m.temperature) as avg_temp, avg(m.precipitation) as avg_rain, avg(m.snowfall) as avg_snowfall 
	from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.hour = m.hour and weekday(h.date) = 0 group by h.date;

insert into avg_traffic_data select h.date, weekday(h.date) as weekday, avg(total0) as avg_ped, avg(total1) as avg_cyc, avg(totalMotorVehicle) as avg_moto, avg(speedViolations) as avg_speedViolations, avg(m.temperature) as avg_temp, avg(m.precipitation) as avg_rain, avg(m.snowfall) as avg_snowfall 
	from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.hour = m.hour and weekday(h.date) = 1 group by h.date;
    
insert into avg_traffic_data select h.date, weekday(h.date) as weekday, avg(total0) as avg_ped, avg(total1) as avg_cyc, avg(totalMotorVehicle) as avg_moto, avg(speedViolations) as avg_speedViolations, avg(m.temperature) as avg_temp, avg(m.precipitation) as avg_rain, avg(m.snowfall) as avg_snowfall 
	from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.hour = m.hour and weekday(h.date) = 2 group by h.date;

insert into avg_traffic_data select h.date, weekday(h.date) as weekday, avg(total0) as avg_ped, avg(total1) as avg_cyc, avg(totalMotorVehicle) as avg_moto, avg(speedViolations) as avg_speedViolations, avg(m.temperature) as avg_temp, avg(m.precipitation) as avg_rain, avg(m.snowfall) as avg_snowfall 
	from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.hour = m.hour and weekday(h.date) = 3 group by h.date;

insert into avg_traffic_data select h.date, weekday(h.date) as weekday, avg(total0) as avg_ped, avg(total1) as avg_cyc, avg(totalMotorVehicle) as avg_moto, avg(speedViolations) as avg_speedViolations, avg(m.temperature) as avg_temp, avg(m.precipitation) as avg_rain, avg(m.snowfall) as avg_snowfall 
	from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.hour = m.hour and weekday(h.date) = 4 group by h.date;

insert into avg_traffic_data select h.date, weekday(h.date) as weekday, avg(total0) as avg_ped, avg(total1) as avg_cyc, avg(totalMotorVehicle) as avg_moto, avg(speedViolations) as avg_speedViolations, avg(m.temperature) as avg_temp, avg(m.precipitation) as avg_rain, avg(m.snowfall) as avg_snowfall 
	from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.hour = m.hour and weekday(h.date) = 5 group by h.date;

insert into avg_traffic_data select h.date, weekday(h.date) as weekday, avg(total0) as avg_ped, avg(total1) as avg_cyc, avg(totalMotorVehicle) as avg_moto, avg(speedViolations) as avg_speedViolations, avg(m.temperature) as avg_temp, avg(m.precipitation) as avg_rain, avg(m.snowfall) as avg_snowfall 
	from meteoblue_weather m, hourly_traffic_data h where m.date = h.date and h.hour = m.hour and weekday(h.date) = 6 group by h.date;
