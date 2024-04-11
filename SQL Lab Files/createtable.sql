DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time text,
  mag float,
  magType char,
  place char,
  locationSource char,
  magSource char
);
