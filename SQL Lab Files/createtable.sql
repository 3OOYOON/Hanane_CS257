DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate date,
  quaketime timestamp,
  mag float,
  magType char,
  magSource char,
  locationSource char,
  location char,
  place char,
);
