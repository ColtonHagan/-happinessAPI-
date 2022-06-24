CREATE DATABASE IF NOT EXISTS db;
use db;

CREATE TABLE IF NOT EXISTS happiness (
    CountryId INT NOT NULL,
    HappinessIndex NUMERIC(4, 1) NOT NULL,
    PRIMARY KEY (CountryId)
);
 
INSERT INTO happiness VALUES
    (12345,102.7),
    (10023,99.3),
    (19634,100.0);