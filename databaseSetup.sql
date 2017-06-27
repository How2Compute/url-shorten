/* create the short_url database */
CREATE DATABASE url_short;

/* Use \c url_short to connect to that database
   Create the urls table TODO make id auto increment & a primary key */
CREATE TABLE urls(id INT PRIMARY KEY, short_code CHAR(50), full_url CHAR(256))

/* Insert a test record */
INSERT INTO urls (id, short_code, full_url) VALUES (1, 'TEST', 'https://google.com');

/* Done! */
