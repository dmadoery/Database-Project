use group8;

create view weather_condition_view as
select wcid, date, hour, weatherIndicator from meteoblue_weather;

create table weather_condition select * from weather_condition_view;
alter table weather_condition add primary key (wcid);