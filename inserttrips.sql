DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS tripInfo;

CREATE TABLE trip (
    trip_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    level VARCHAR(30),
    start_date DATE,
    location VARCHAR(30),
    length VARCHAR(30),
    leader VARCHAR(30),
    cost DECIMAL,
    description TEXT
) ENGINE=INNODB;

CREATE TABLE member (
    member_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    address VARCHAR(50),
    email VARCHAR(40),
    DoB DATE,
    phone VARCHAR(20)
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

INSERT INTO trip (trip_ID, name, start_date, length, cost, location, level, leader, description) VALUES
("1", "Scuba Steve's Reef Adventure","2023-03-10","7 Days","2000","Key Largo FL","Expert","Captain Jack","Explore coral reefs, shipwrecks, and other underwater environments that are not accessible to snorkelers or swimmers!"),
("2","Crazy Rapids Rafting","2023-04-07","7 Days","750","Hartford TN","Intermediate","Ethan Reynolds","Navigate rapids and choppy waters on a raft or kayak, and feel the thrill of the rushing water all around you!"),
("3","Old Knobstone Trail Hike","2023-04-22","1 Day","20","Deam Lake IN","Novice","Ava Rodriguez","An adventure that allows individuals to explore nature and enjoy the great outdoors!"),
("4","Colorado Ski Trip","2023-04-27","5 Days","850","Vail CO","Intermediate","Lucas Patel","A unique and exciting winter vacation experience, combining outdoor adventure with cozy accommodations and memorable après-ski activities.!"),
("5","White River Kayaking","2023-05-06","2 Days","100","Noblesville IN","Novice","Sophia Nguyen","Explore the natural beauty of their surroundings and enjoy a relaxing day on the water!"),
("6","Rock Climbing","2023-05-06","2 Days","100","Noblesville IN","Intermediate","Liam Stevenson","Scale cliffs and mountains with specialized equipment and test your strength, endurance, and problem-solving skills!");

INSERT INTO member (member_ID, name, DoB, email, address, phone) VALUES
("1", "Jody Whatley ","1971-10-26","jdwhat@iu.edu","1585 S Rogers Bloomington","(812)325-8841"),
("2", "Chris Jackson","1973-02-02","cjackson@aol.com","211 N Washington St Bloomington","(812)327-9816"),
("3", "Kit Lexington","1974-05-05","kitlex@gmail.com","350 W Main Spencer","(812)450-0573"),
("4", "Pat Riley","1979-06-16","patriley@gmail.com","3581 N Meridian Indianpolis","(812)988-7550"),
("5", "Skylar Channing","1993-09-15","skylar@channing.com","2095 N College Indianpolis","(812)540-8034"),
("6", "Sophie Martinez","1995-04-23","sophie.martinez93@gmail.com","123 Main Street Bloomington","(812)357-9251");

INSERT INTO tripInfo (member_ID, trip_ID) VALUES
("1", "1"),
("2", "1"),
("3", "1"),
("4", "1"),
("1", "2"),
("4", "2"),
("6", "2"),
("1", "3"),
("2", "2"),
("5", "2");



DROP TABLE trip;

DROP TABLE member;

DROP TABLE tripInfo;