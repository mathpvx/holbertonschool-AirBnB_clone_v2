-- Script that prepares a MySQL server for the project

-- create the database making sure it doesnt already exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user with a defined password making sure it doesnt already exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- gives all privileges to user on the database
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- gives select privileges on performance_schema db to user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';