DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS tripInfo;

CREATE TABLE trip (
    trip_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    level VARCHAR(12),
    start_date DATE,
    location VARCHAR(20),
    length VARCHAR(15),
    level VARCHAR(15),
    leader VARCHAR(15),
    cost DECIMAL,
    description TEXT
) ENGINE=INNODB;

CREATE TABLE member (
    member_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    address VARCHAR(20),
    email VARCHAR(20),
    date_of_birth DATE,
    phone VARCHAR(12)
) ENGINE=INNODB;

CREATE TABLE tripInfo (
    member_ID INT NOT NULL,
    trip_ID INT NOT NULL,
    CONSTRAINT `fk_trip_constraint`
        FOREIGN KEY (trip_ID) REFERENCES trip(trip_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT `fk_member_constraint`
        FOREIGN KEY (member_ID) REFERENCES member(member_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE

) ENGINE=INNODB;
