CREATE DATABASE IF NOT EXISTS db;
use db;

CREATE TABLE IF NOT EXISTS students (
    StudentID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students(FirstName)
VALUES("John");