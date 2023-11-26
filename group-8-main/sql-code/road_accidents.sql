use group8;
create view road_acciedents_view as
Select aid, accidentDay, accidentMonth, accidentYear, latitude, longitude
from road_accidents;

create view road_accidents_month_view as
select accidentMonth, accidentYear, count(accidentMonth) as amount  from road_accidents
group by accidentMonth, accidentYear;

create view road_accidents_onWeekdaysPerYear_view as
select accidentDay, accidentYear, count(accidentDay) as amount 	from road_accidents
group by accidentDay, accidentYear;
