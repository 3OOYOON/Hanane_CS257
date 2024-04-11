DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time timestamp,
  magnitude real,
  magType text,
  place text,
  locationSource text,
  magSource text
);
