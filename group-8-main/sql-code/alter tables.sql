ALTER table violations_peryear_monthly
ADD vpymid int NOT NULL auto_increment unique first;

ALTER table percentage_violation_year
ADD pvyid int NOT NULL auto_increment unique first;

ALTER table accident_peryear_monthly
ADD apymid int NOT NULL auto_increment unique first;

ALTER table avg_traffic_data
ADD atdid int NOT NULL auto_increment unique first;
