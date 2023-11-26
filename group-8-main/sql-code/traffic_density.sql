use group8;
create view ped_sum_view AS
Select cptid as psid, date, hour, trafficType, SUM(total) as total From cycle_pedestrian_transit
where trafficType = 'Fussgänger'
group by date,hour, trafficType;

create table ped_sum select * from ped_sum_view;

create view cycle_sum_view as
select cptid as csid, date, hour, trafficType, sum(total) as total from cycle_pedestrian_transit
where trafficType = 'Velo'
group by date, hour, trafficType;

create table cycle_sum select * from cycle_sum_view;

create view cycle_ped_sum_view as 
select ps.psid as cpsid, ps.date, ps.hour, ps.trafficType as trafficType0, ps.total as total0, cs.trafficType as trafficType1, cs.total as total1 from ped_sum ps , cycle_sum cs
where ps.date = cs.date and ps.hour = cs.hour
group by ps.date, ps.hour;

create view motorVehicles_sum_view AS
Select date, hour, SUM(total) as total from vehicle_density
group by date, hour;

create view traffic_density_view AS
Select cp.cpsid as tdid, cp.date, cp.hour, cp.trafficType0, cp.total0, cp.trafficType1, cp.total1, v.total as totalMotorVehicle
from cycle_ped_sum_view cp, motorVehicles_sum_view v
where cp.date = v.date and cp.hour = v.hour;

create table traffic_density select * from traffic_density_view;
alter table traffic_density add primary key (tdid);