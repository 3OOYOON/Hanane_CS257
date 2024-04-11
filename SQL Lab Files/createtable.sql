DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time text,
  mag decimal,
  magType text,
  place text,
  locationSource text,
  magSource text
);
