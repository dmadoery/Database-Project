use group8;

create table local_traffic_data (
    aid int,
    accidentDay varchar(50),
    accidentMonth int,
    accidentYear int,
    latitude varchar(50),
    longitude varchar(50),
    svid int,
    date varchar(50),
    hour int,
    violationLevel int,
    violationDegree double
);

insert into local_traffic_data (svid,date,hour,violationLevel,violationDegree, latitude, longitude)
select svid,date,hour,violationLevel,violationDegree, latitude, longitude from speed_violations;

insert into local_traffic_data (aid,accidentDay, accidentMonth, accidentYear, latitude, longitude)
select aid, accidentDay, accidentMonth, accidentYear, latitude, longitude from road_accidents;
