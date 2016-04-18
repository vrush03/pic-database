--database

drop database pictureapp;
create database pictureapp;

--User table

use pictureapp;

CREATE TABLE `User` (
`UserId` BIGINT NULL AUTO_INCREMENT,
`UserName` VARCHAR(255) NULL,
`Useremail` VARCHAR(255) NULL,
`UserPassword` VARCHAR(255) NULL,
`img` LONGBLOB  NULL,
PRIMARY KEY (`UserId`));

INSERT INTO User Values (0,"Vrushank","somwthing@gmail.com","adefewef","/home/vrushank/Downloads/DSC_0068.jpg");
INSERT INTO User Values (1,"Vrushank","skjdde","sjkefhhwe","/home/vrushank/Desktop/Picture-Database/static/images");
