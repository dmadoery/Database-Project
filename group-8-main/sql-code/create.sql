drop database if exists group8;
create database group8;
use group8;

Set names utf8;
set character_set_client = utf8mb4;

drop table if exists meteoblue_weather, vehicle_transit, vehicle_density, cycle_pedestrian_transit, speed_monitoring, road_accidents;

create table meteoblue_weather (
	timestamp varchar(20),
	temperature double,
	sunshineDuration int,
	precipitation int, 
	snowfall int,
	cloudcoverHigh int,
	cloudcoverMiddle int,
	cloudcoverLight int,
	windSpeed double,
	windDirection double,
    wcid int PRIMARY KEY,
    date varchar(20),
    hour int,
    weatherIndicator double
);

create table vehicle_transit (
	timestamp varchar(30),
    vehicleClass varchar(30),
    timestampText varchar(50) PRIMARY KEY,
    classificationIndex int
);

create table vehicle_density (
	vdid int PRIMARY KEY,
    date varchar(20),
    hour int,
    vehicleClass varchar(25),
    total int
);

create table cycle_pedestrian_transit (
	zst_nr int,
    siteCode int,
    siteName varchar(50),
    dateTimeFrom varchar(50),
    dateTimeTo varchar(50),
    directionName varchar(50),
    laneCode int,
    laneName varchar(50), 
    valuesApproved int,
    valuesEdited int,
    trafficType varchar(30),
    total int,
    year int,
    month int,
    day int,
    weekday int,
    hourFrom int,
    date varchar(30),
    timeFrom varchar (10),
    timeTo varchar(10),
    dayOfYear int,
    zst_id int,
    geoPoint varchar(100),
    cptid int PRIMARY KEY,
    hour int,
    latitude varchar(50),
    longitude varchar(50)
);

create table speed_monitoring (
	timestamp varchar(80),
    measureID int,
    directionID int,
    speed double,
    time varchar(50),
    date varchar(50),
    dateAndTime varchar(80),
    measureBegin varchar(50),
    measureEnd varchar(50),
    zone int,
    location varchar(80),
    direction varchar(100),
    geoPoint varchar(100),
    violationRate double,
    speedV50 double,
    speedV85 double,
    street varchar(100),
    housNr varchar(80),
    vehicles double,
    vehicleLength double,
    metricsPerLocation varchar(200),
    svid int PRIMARY KEY,
    hour int,
    violationDegree double,
    latitude varchar(50),
    longitude varchar(50)
);

create table road_accidents (
	geoPoint varchar(100),
    geoShape varchar(200),
    accidentID varchar(100),
    accidentDescription varchar(200),
    accidentDescriptionFr varchar(200),
    accidentDescriptionEn varchar(200),
    accidentSeverity varchar(50),
    accidentSeverityFr varchar(50),
    accidentSeverityEn varchar(50),
    pedestrianInvolvement varchar(10),
    bycicleInvolvement varchar(10),
    motocycleInvolvement varchar(10),
	streettypeDescription varchar(100),
    streettypeDescriptionFr varchar(100),
    streettypeDescriptionEn varchar(100),
    eastCoordinates int,
    northCoodrinates int,
    canton varchar(5),
    muncipalNumber int,
    accidentYear int,
    accidentMonth int,
    accidentMonth2 varchar(30),
    accidentMonthFr varchar(30),
    accidentMonthEn varchar(30),
    accidentDay varchar(20),
	accidentDayFr varchar(20),
    accidentDayEn varchar(20),
    accidentHour varchar(20),
    accidentDate varchar(20),
    accidentType varchar(20),
    accidentSeverityCategory varchar(20),
    streetType varchar(100),
    weekdayCode varchar(20),
    accidentHourNr int,
    aid int PRIMARY KEY,
    latitude varchar(50),
    longitude varchar(50)
);