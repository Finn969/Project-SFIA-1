BEGIN;

DROP TABLE IF EXISTS relations;

CREATE TABLE relations (
	eventID INT(3) AUTO_INCREMENT,
	generalID INT(3),
	battleID INT(3),
	PRIMARY KEY(eventID),
	FOREIGN KEY(generalID) REFERENCES commanderstable(ID),
	FOREIGN KEY(battleID) REFERENCES battlestable(ID)
);

DROP TABLE IF EXISTS generalstable;

CREATE TABLE generalstable (
	ID INT(3) NOT NULL AUTO_INCREMENT,
	firstname VARCHAR(50) DEFAULT = UNKNOWN,
	lastname VARCHAR(50) NOT NULL,
	nationality VARCHAR(50) DEFAULT = UNKNOWN,
	date_of_birth DATE NOT NULL,
	notes VARCHAR(50)
	PRIMARY KEY(ID)
);

DROP TABLE IF EXISTS battlestable;

CREATE TABLE battlestable (
	ID INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	location VARCHAR(50) NOT NULL,
	startdate DATE,
	enddate DATE NOT NULL,
	type VARCHAR(10) NOT NULL
);


	
COMMIT;
