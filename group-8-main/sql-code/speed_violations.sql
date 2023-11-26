use group8;

create view speed_monitoringWithLevel_view as
select svid, date, hour, violationDegree, 
case when violationDegree <= 0 then 0 when violationDegree > 0 and violationDegree <= 20 then 1 
when violationDegree > 20 and violationDegree <= 50 then 2 else 3 end as violationLevel,
 latitude, longitude from speed_monitoring;
 
create view speed_violations_view as
select svid, date, hour, violationDegree, violationLevel, latitude, longitude from speed_monitoringWithLevel_view
where violationLevel > 0;


create table speed_violations select * from speed_violations_view;
alter table speed_violations add primary key (svid);

create view speed_violations_total_view as
select svid as svtid, date, hour, count(hour) as amount, sum(violationDegree)/count(hour) as violationDegreeAverage  from speed_violations
group by date, hour;

create table speed_violations_total select * from speed_violations_total_view;
alter table speed_violations_total add primary key (svtid);
