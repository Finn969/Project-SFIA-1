CREATE TABLE battlestable2 (
  ID INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL DEFAULT 'UNKNOWN',
  location VARCHAR(50) NOT NULL,
  startdate DATE,
  enddate DATE NOT NULL,
  type VARCHAR(10) NOT NULL,
  war VARCHAR(50) NOT NULL DEFAULT 'UNKNOWN',
  result VARCHAR(50) NOT NULL DEFAULT 'Decisive',
  winnerID INT(3),
  loserID INT(3),
  notes VARCHAR(1000) DEFAULT NULL,
  FOREIGN KEY(winnerID) REFERENCES armiestable(armyID),
  FOREIGN KEY(loserID) REFERENCES armiestable(armyID)
);

CREATE TABLE armiestable (
    armyID INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    strength INT(100) DEFAULT NULL,
    country VARCHAR(50),
    commanderf VARCHAR(50),
    commanders VARCHAR(50),
    FOREIGN KEY(country) REFERENCES commanderstable(nationality),
    FOREIGN KEY(commanderf) REFERENCES commanderstable(firstname),
    FOREIGN KEY(commanders) REFERENCES commanderstable(lastname)     
);

