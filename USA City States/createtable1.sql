<<<<<<< HEAD:USA City States/createtable.sql
DROP TABLE IF EXISTS USA City State Population;
CREATE TABLE USA City State Population (
  city text,
  state text,
  population int,
  longitude decimal,
  latitude decimal
=======
DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate date,
  quaketime time with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  id text,
  place text,
  quaketype text
>>>>>>> a34246e6e86b8e9e8e15351769f6855a706867e7:USA City States/createtable1.sql
);
