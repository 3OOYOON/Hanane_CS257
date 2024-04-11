DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time varchar(max),
  mag float,
  magType char,
  place char,
  locationSource char,
  magSource char
);
