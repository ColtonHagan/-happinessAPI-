CREATE DATABASE NOT EXISTS happiness;
use happiness;

CREATE TABLE IF NOT EXISTS happiness (
    `country_id` INT NOT NULL,
    `happiness_index` NUMERIC(4, 1) NOT NULL,
    PRIMARY KEY (country_id)
);
 
INSERT INTO happiness VALUES
    (10001,96.8),
    (10003,101.1),
    (10005,100.6),
    (1001,99.8),
    (1003,100.8);