create table percentage_violation_year select t1.year, vio, vioDegree, noVio, noVioDegree from (
((select year, vio, vioDegree from (select year(date) as year, count(svid) as vio, avg(violationDegree) as vioDegree from speed_monitoring where year(date) = 2017 group by violationDegree > 0) as test where vioDegree > 0) t1
Inner Join 
(select year, noVio, noVioDegree from (select year(date) as year, count(svid) as noVio, avg(violationDegree) as noVioDegree from speed_monitoring where year(date) = 2017 group by violationDegree <= 0) as test2 where novioDegree <= 0) t2
on (t1.year = t2.year)));

insert into percentage_violation_year select t1.year, vio, vioDegree, noVio, noVioDegree from (
((select year, vio, vioDegree from (select year(date) as year, count(svid) as vio, avg(violationDegree) as vioDegree from speed_monitoring where year(date) = 2018 group by violationDegree > 0) as test where vioDegree > 0) t1
Inner Join 
(select year, noVio, noVioDegree from (select year(date) as year, count(svid) as noVio, avg(violationDegree) as noVioDegree from speed_monitoring where year(date) = 2018 group by violationDegree <= 0) as test2 where novioDegree <= 0) t2
on (t1.year = t2.year)));
insert into percentage_violation_year select t1.year, vio, vioDegree, noVio, noVioDegree from (
((select year, vio, vioDegree from (select year(date) as year, count(svid) as vio, avg(violationDegree) as vioDegree from speed_monitoring where year(date) = 2019 group by violationDegree > 0) as test where vioDegree > 0) t1
Inner Join 
(select year, noVio, noVioDegree from (select year(date) as year, count(svid) as noVio, avg(violationDegree) as noVioDegree from speed_monitoring where year(date) = 2019 group by violationDegree <= 0) as test2 where novioDegree <= 0) t2
on (t1.year = t2.year)));
insert into percentage_violation_year select t1.year, vio, vioDegree, noVio, noVioDegree from (
((select year, vio, vioDegree from (select year(date) as year, count(svid) as vio, avg(violationDegree) as vioDegree from speed_monitoring where year(date) = 2020 group by violationDegree > 0) as test where vioDegree > 0) t1
Inner Join 
(select year, noVio, noVioDegree from (select year(date) as year, count(svid) as noVio, avg(violationDegree) as noVioDegree from speed_monitoring where year(date) = 2020 group by violationDegree <= 0) as test2 where novioDegree <= 0) t2
on (t1.year = t2.year)));
insert into percentage_violation_year select t1.year, vio, vioDegree, noVio, noVioDegree from (
((select year, vio, vioDegree from (select year(date) as year, count(svid) as vio, avg(violationDegree) as vioDegree from speed_monitoring where year(date) = 2021 group by violationDegree > 0) as test where vioDegree > 0) t1
Inner Join 
(select year, noVio, noVioDegree from (select year(date) as year, count(svid) as noVio, avg(violationDegree) as noVioDegree from speed_monitoring where year(date) = 2021 group by violationDegree <= 0) as test2 where novioDegree <= 0) t2
on (t1.year = t2.year)));
