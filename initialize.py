import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database = "autowisher" #enter your database name
)


mycursor = mydb.cursor()


sql = "Create table users (id int(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,name varchar(50) not null,contactName varchar(50) not null)"
mycursor.execute(sql)


sql = "Create table birthday(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,birthdayMonth int NOT NULL,birthdayDate int NOT NULL,wishStatus varchar(2) not null,userId int(4) unique,message varchar(500) not null,FOREIGN KEY (`userId`) REFERENCES `users`(`id`))"
mycursor.execute(sql)

sql = "Create table events (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,eventName varchar(30) not null,date DATE not null,message Varchar(70) not null,wishStatus varchar(2) not null)"
mycursor.execute(sql)

sql = "Create table eventMapper (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,eventId int not null,userId int not null,FOREIGN KEY (`userId`) REFERENCES `users`(`id`),FOREIGN KEY (`eventId`) REFERENCES `events`(`id`))"
mycursor.execute(sql)
