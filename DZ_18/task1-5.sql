CREATE DATABASE my_first_db;

CREATE TABLE student (
	id int,
    name varchar(255)
);

CREATE TABLE employee (
	id int PRIMARY KEY,
    name varchar(255),
    salary int(6)
);

ALTER TABLE student
ADD PRIMARY KEY (id);

INSERT INTO student
VALUES (01, 'John');

INSERT INTO employee
VALUES (01, 'John', 10000);