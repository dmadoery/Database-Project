create Table accident_perYear_monthly select count(aid) as total, accidentYear as year, accidentMonth as month from local_traffic_data where accidentYear = 2017 group by accidentMonth order by accidentMonth;
create Table violations_perYear_monthly select count(svid) as total, year(date) as year, month(date) as month from local_traffic_data where year(date) = 2017 group by month(date) order by month(date);

Insert into accident_perYear_monthly select count(aid) as total, accidentYear as year, accidentMonth as month from local_traffic_data where accidentYear = 2018 group by accidentMonth order by accidentMonth;
Insert into violations_perYear_monthly select count(svid) as total, year(date) as year, month(date) as month from local_traffic_data where year(date) = 2018 group by month(date) order by month(date);

Insert into accident_perYear_monthly select count(aid) as total, accidentYear as year, accidentMonth as month from local_traffic_data where accidentYear = 2019 group by accidentMonth order by accidentMonth;
Insert into violations_perYear_monthly select count(svid) as total, year(date) as year, month(date) as month from local_traffic_data where year(date) = 2019 group by month(date) order by month(date);

Insert into accident_perYear_monthly select count(aid) as total, accidentYear as year, accidentMonth as month from local_traffic_data where accidentYear = 2020 group by accidentMonth order by accidentMonth;
Insert into violations_perYear_monthly select count(svid) as total, year(date) as year, month(date) as month from local_traffic_data where year(date) = 2020 group by month(date) order by month(date);

Insert into accident_perYear_monthly select count(aid) as total, accidentYear as year, accidentMonth as month from local_traffic_data where accidentYear = 2021 group by accidentMonth order by accidentMonth;
Insert into violations_perYear_monthly select count(svid) as total, year(date) as year, month(date) as month from local_traffic_data where year(date) = 2021 group by month(date) order by month(date);
