set global transaction isolation level read committed;
begin;
CREATE TABLE images (
	uid INT not null  AUTO_INCREMENT, 
	imagename VARCHAR(100), 
	uploadname VARCHAR(100), 
	comments VARCHAR(100), 
	uploadtime DATETIME, 
	uploaduser VARCHAR(100), 
	published_topics VARCHAR(100), 
	subscribed_topics VARCHAR(100), 
	advertised_services VARCHAR(100), 
	advertised_actions VARCHAR(100), 
	primary key(uid)
);
CREATE TABLE services (
	uid INT not null  AUTO_INCREMENT,
	serviceid VARCHAR(100), 
	createdtime VARCHAR(100), 
	imagename VARCHAR(100), 
	uploadname VARCHAR(100), 
	username VARCHAR(100), 
	firstcreatetime DATETIME, 
	PRIMARY KEY (uid)
);
CREATE TABLE users (
	uid INT not null  AUTO_INCREMENT,
	firstname VARCHAR(100), 
	lastname VARCHAR(100), 
	email VARCHAR(120), 
	passwdhash VARCHAR(100), 
	PRIMARY KEY (uid), 
	UNIQUE (email)
);
CREATE TABLE serverip (
	uid INT not null  AUTO_INCREMENT,
	serverip VARCHAR(100), 
	PRIMARY KEY (uid)
);
INSERT INTO serverip VALUES(1,'192.168.4.104');
COMMIT;
