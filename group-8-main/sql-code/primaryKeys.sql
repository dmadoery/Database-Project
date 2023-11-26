use group8;

alter table accident_peryear_monthly
add primary key (apymid);

alter table avg_traffic_data
add primary key (atdid);

alter table cycle_sum
add primary key (csid);

alter table ped_sum
add primary key (psid);

alter table percentage_violation_year
add primary key (pvyid);

alter table violations_peryear_monthly
add primary key (vpymid);