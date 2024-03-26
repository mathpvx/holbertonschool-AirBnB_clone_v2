-- Script that prepares a MySQL server for the project

-- creates the database and make sure it doesnt exist yet 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creates the user with passwords and makes sures it doesnt exist yet 
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- gives all privileges to user on the database 
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- gives select privileges on performance_schema database to user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';