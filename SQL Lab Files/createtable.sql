DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time timestamp,
  mag float,
  magType char,
  place char,
  locationSource char,
  magSource char
);
