DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time text,
  mag double precision,
  magType text,
  place text,
  locationSource text,
  magSource text
);
