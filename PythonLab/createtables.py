DROP TABLE IF EXISTS USA City State Population;
CREATE TABLE USA Cities And State Population (
  City text,
  State text,
  Population int,
  Latitude decimal,
  Longitude decimal
);

DROP TABLE IF EXISTS USA State Population;
CREATE TABLE USA State Population (
  Code text,
  State text,
  Population int,
);
