# Database Project HS2022: Group8
This repo consists of the code and documentation for the HS22 Database project "Impact of Weather on Traffic Intensity, Speed
Violations and Accidents in Basel" (Group8). In the following the necessary steps are provided to replicate the database.


### Cleaning datasets
1. Put datasets into a folder "data" at the root of project.
2. Execute python script clean.py with `py code/clean.py` from root folder of project.

### Import data into schema
1. Create the tables with `create.sql` in mysql workbench.
2. Open mysql command line client and establish connection.
3. Change local_infile variable to ON:
    ```
    show global variables like 'local_infile';
	if local_infile is OFF enter:
		  set global local_infile=true;
    ```
    You might have to replace true with `'ON'` such as
    ```
    show global variables like 'local_infile';
	if local_infile is OFF enter:
		  set global local_infile='ON';
    ```
4. Enter: mysql> `SHOW VARIABLES LIKE "secure_file_priv";`.
    
    Copy the path returned and store the datasets there.
5. Enter `use group8` in mysql commandline and then the following code to import the data (Note that you change the path and the name of the file!):

    #### Import of road_accidents
    ```
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/roadaccidents_cleaned.csv'
    into table road_accidents
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    (@a,@b,@c,@d,@e,@f,@g,@h,@i,@j,@k,@l,@m,@n,@o,@p,@q,@r,@s,@t,@u,@v,@w,@x,@y,@z,@aa,@ab,@ac,@ad,@ae,@af,@ag,@ah,@ai,@aj,@ak)
    SET geoPoint = IF(@a = '', NULL, @a),
    geoShape = IF(@b = '', NULL, @b),
    accidentID = IF(@c = '', NULL, @c),
    accidentDescription = IF(@d = '', NULL, @d),
    accidentDescriptionFr = IF(@e = '', NULL, @e),
    accidentDescriptionEn = IF(@f = '', NULL, @f),
    accidentSeverity = IF(@g = '', NULL, @g),
    accidentSeverityFr = IF(@h = '', NULL, @h),
    accidentSeverityEn = IF(@i = '', NULL, @i),
    pedestrianInvolvement = IF(@j = '', NULL, @j),
    bycicleInvolvement = IF(@k = '', NULL, @k),
    motocycleInvolvement = IF(@l = '', NULL, @l),
    streettypeDescription = IF(@m = '', NULL, @m),
    streettypeDescriptionFr = IF(@n = '', NULL, @n),
    streettypeDescriptionEn = IF(@o = '', NULL, @o),
    eastCoordinates = IF(@p = '', NULL, @p),
    northCoodrinates = IF(@q = '', NULL, @q),
    canton = IF(@r = '', NULL, @r),
    muncipalNumber = IF(@s = '', NULL, @s),
    accidentYear = IF(@t = '', NULL, @t),
    accidentMonth = IF(@u = '', NULL, @u),
    accidentMonth2 = IF(@v = '', NULL, @v),
    accidentMonthFr = IF(@w = '', NULL, @w),
    accidentMonthEn = IF(@x = '', NULL, @x),
    accidentDay = IF(@y = '', NULL, @y),
    accidentDayFr = IF(@z = '', NULL, @z),
    accidentDayEn = IF(@aa = '', NULL, @aa),
    accidentHour = IF(@ab = '', NULL, @ab),
    accidentDate = IF(@ac = '', NULL, @ac),
    accidentType = IF(@ad = '', NULL, @ad),
    accidentSeverityCategory = IF(@ae = '', NULL, @ae),
    streetType = IF(@af = '', NULL, @af),
    weekdayCode = IF(@ag = '', NULL, @ag),
    accidentHourNr = IF(@ah = '', NULL, @ah),
    aid = IF(@ai = '', NULL, @ai),
    latitude = IF(@aj = '', NULL, @aj),
    longitude = IF(@ak = '', NULL, @ak);
    ```

    #### Import of speed_monitoring 2020
    ```
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/speed2020_cleaned.csv'
    into table speed_monitoring
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    (@a,@b,@c,@d,@e,@f,@g,@h,@i,@j,@k,@l,@m,@n,@o,@p,@q,@r,@s,@t,@u,@v,@w,@x,@y,@z)
    SET timestamp = IF(@a = '', NULL, @a),
    measureID = IF(@b = '', NULL, @b),
    directionID = IF(@c = '', NULL, @c),
    speed = IF(@d = '', NULL, @d),
    time = IF(@e = '', NULL, @e),
    date = IF(@f = '', NULL, @f),
    dateAndTime = IF(@g = '', NULL, @g),
    measureBegin = IF(@h = '', NULL, @h),
    measureEnd = IF(@i = '', NULL, @i),
    zone = IF(@j = '', NULL, @j),
    location = IF(@k = '', NULL, @k),
    direction = IF(@l = '', NULL, @l),
    geoPoint = IF(@m = '', NULL, @m),
    violationRate = IF(@n = '', NULL, @n),
    speedV50 = IF(@o = '', NULL, @o),
    speedV85 = IF(@p = '', NULL, @p),
    street = IF(@q = '', NULL, @q),
    housNr = IF(@r = '', NULL, @r),
    vehicles = IF(@s = '', NULL, @s),
    vehicleLength = IF(@t = '', NULL, @t),
    metricsPerLocation = IF(@u = '', NULL, @u),
    svid = IF(@v = '', NULL, @v),
    hour = IF(@w = '', NULL, @w),
    violationDegree = IF(@x = '', NULL, @x),
    latitude = IF(@y = '', NULL, @y),
    longitude = IF(@z = '', NULL, @z);
    ```

    #### Import of speed_monitoring 2021
    ```
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/speed2021_cleaned.csv'
    into table speed_monitoring
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    (@a,@b,@c,@d,@e,@f,@g,@h,@i,@j,@k,@l,@m,@n,@o,@p,@q,@r,@s,@t,@u,@v,@w,@x,@y,@z)
    SET timestamp = IF(@a = '', NULL, @a),
    measureID = IF(@b = '', NULL, @b),
    directionID = IF(@c = '', NULL, @c),
    speed = IF(@d = '', NULL, @d),
    time = IF(@e = '', NULL, @e),
    date = IF(@f = '', NULL, @f),
    dateAndTime = IF(@g = '', NULL, @g),
    measureBegin = IF(@h = '', NULL, @h),
    measureEnd = IF(@i = '', NULL, @i),
    zone = IF(@j = '', NULL, @j),
    location = IF(@k = '', NULL, @k),
    direction = IF(@l = '', NULL, @l),
    geoPoint = IF(@m = '', NULL, @m),
    violationRate = IF(@n = '', NULL, @n),
    speedV50 = IF(@o = '', NULL, @o),
    speedV85 = IF(@p = '', NULL, @p),
    street = IF(@q = '', NULL, @q),
    housNr = IF(@r = '', NULL, @r),
    vehicles = IF(@s = '', NULL, @s),
    vehicleLength = IF(@t = '', NULL, @t),
    metricsPerLocation = IF(@u = '', NULL, @u),
    svid = IF(@v = '', NULL, @v),
    hour = IF(@w = '', NULL, @w),
    violationDegree = IF(@x = '', NULL, @x),
    latitude = IF(@y = '', NULL, @y),
    longitude = IF(@z = '', NULL, @z);
    ```

    #### Import of cycle_pedestrian_transit
    ```
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cycle_ped_cleaned.csv'
    into table cycle_pedestrian_transit
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    (@a,@b,@c,@d,@e,@f,@g,@h,@i,@j,@k,@l,@m,@n,@o,@p,@q,@r,@s,@t,@u,@v,@w,@x,@y,@z,@aa)
    SET zst_nr = IF(@a = '', NULL, @a),
    siteCode = IF(@b = '', NULL, @b),
    siteName = IF(@c = '', NULL, @c),
    dateTimeFrom = IF(@d = '', NULL, @d),
    dateTimeTo = IF(@e = '', NULL, @e),
    directionName = IF(@f = '', NULL, @f),
    laneCode = IF(@g = '', NULL, @g),
    laneName = IF(@h = '', NULL, @h),
    valuesApproved = IF(@i = '', NULL, @i),
    valuesEdited = IF(@j = '', NULL, @j),
    trafficType = IF(@k = '', NULL, @k),
    total = IF(@l = '', NULL, @l),
    year = IF(@m = '', NULL, @m),
    month = IF(@n = '', NULL, @n),
    day = IF(@o = '', NULL, @o),
    weekday = IF(@p = '', NULL, @p),
    hourFrom = IF(@q = '', NULL, @q),
    date = IF(@r = '', NULL, @r),
    timeFrom = IF(@s = '', NULL, @s),
    timeTo = IF(@t = '', NULL, @t),
    dayOfYear = IF(@u = '', NULL, @u),
    zst_id = IF(@v = '', NULL, @v),
    geoPoint = IF(@w = '', NULL, @w),
    cptid = IF(@x = '', NULL, @x),
    hour = IF(@y = '', NULL, @y),
    latitude = IF(@z = '', NULL, @z),
    longitude = IF(@aa = '', NULL, @aa);
    ```  

    #### Import of vehicle_transit
    ```
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/vehicle transit.csv'
    into table vehicle_transit
    fields terminated by ';'
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    (@a,@b,@c,@d)
    SET timestamp = IF(@a = '', NULL, @a),
    vehicleClass = IF(@b = '', NULL, @b),
    timestampText = IF(@c = '', NULL, @c),
    classificationIndex = IF(@d = '', NULL, @d);
    ```

    #### Import of vehicle_density
    ```
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/vehicle_density.csv'
    into table vehicle_density
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    (@a,@b,@c,@d,@e)
    SET vdid = IF(@a = '', NULL, @a),
    date = IF(@b = '', NULL, @b),
    hour = IF(@c = '', NULL, @c),
    vehicleClass = IF(@d = '', NULL, @d),
    total = IF(@e = '', NULL, @e);
    ```
    
    #### Import of meteoblue_weather
    ```
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/weather_withIndicator.csv'
    into table meteoblue_weather
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    (@a,@b,@c,@d,@e,@f,@g,@h,@i,@j,@k,@l,@m,@n)
    SET timestamp = IF(@a = '', NULL, @a),
    temperature = IF(@b = '', NULL, @b),
    sunshineDuration = IF(@c = '', NULL, @c),
    precipitation = IF(@d = '', NULL, @d),
    snowfall = IF(@e = '', NULL, @e),
    cloudcoverHigh = IF(@f = '', NULL, @f),
    cloudcoverMiddle = IF(@g = '', NULL, @g),
    cloudcoverLight = IF(@h = '', NULL, @h),
    windSpeed = IF(@i = '', NULL, @i),
    windDirection = IF(@j = '', NULL, @j),
    wcid = IF(@k = '', NULL, @k),
    date = IF(@l = '', NULL, @l),
    hour = IF(@m = '', NULL, @m),
    weatherIndicator = IF(@n = '', NULL, @n);
    ```

    #### Integration of data
    ```
    6. Execute queries in `road_accidents.sql`, `speed_violations.sql`, `traffic_density.sql` and `weather_indicator.sql`.
    7. Execute queries in `hourly_traffic_data.sql`.
    8. Execute queries in `local_traffic_data.sql`.
    9. Execute queries in `avg_traffic_data.sql`, `accident_peryear_monthly.sql`, `percentage_violation_year`, `alter tables.sql`.
    10. Execute queries in `primaryKey.sql`.
    ```
