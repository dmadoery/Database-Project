use group8;

create view hourly_traffic_data_view as
select sv.svtid as htdid, sv.date, sv.hour, sv.amount as speedViolations, sv.violationDegreeAverage, td.trafficType0, td.total0, td.trafficType1, 
td.total1, td.totalMotorVehicle, wc.weatherIndicator
from weather_condition_view wc, speed_violations_total sv, traffic_density td
where sv.date = wc.date and sv.date = td.date and sv.hour = wc.hour and sv.hour = td.hour;

create table hourly_traffic_data select * from hourly_traffic_data_view;
alter table hourly_traffic_data add primary key (htdid);