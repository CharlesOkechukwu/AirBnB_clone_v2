-- Script to setup mysql for this project
-- DECLARE HBNB_MYSQL_DB VARCHAR(128);
-- DECLARE HBNB_MYSQL_USER  VARCHAR(128);
-- DECLARE HBNB_MYSQL_PWD VARCHAR(128);
-- DECLARE HBNB_MYSQL_HOST VARCHAR(128);
-- Assign a value to the variable
-- SET variable_name = value;
CREATE database IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
