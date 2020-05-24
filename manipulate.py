import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database = "autowisher" #enter your database name
)


mycursor = mydb.cursor()

def checkIfEventToday():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    sql = "select * from events where date='{}' and wishStatus='n'".format(date)
    mycursor.execute(sql)
    events = mycursor.fetchall()
    eventsToWish = []
    if len(events):
        for event in events:
            message = event[3]
            users = getUsersForEvent(event[0])
            eventsToWish.append([users,message,event[0]])
    return eventsToWish

def getUsersForEvent(eventId):
    sql = "select userId from eventMapper where eventId='{}'".format(eventId)
    mycursor.execute(sql)
    users = mycursor.fetchall()
    userIds = []
    if len(users):
        for user in users:
            userIds.append(user[0])
    contactNames = []
    for id in userIds:
        contactNames.append(getContactNameFromUserId(id))
    return contactNames

def getContactNameFromUserId(id):
    sql = "select contactName from users where id={}".format(id)
    mycursor.execute(sql)
    contacts = mycursor.fetchall()
    if len(contacts):
        return contacts[0][0]
    else:
        print("no such contact")

def updateStausToWished(eventId):
    sql = "update events set wishStatus='y' where id='{}'".format(eventId)
    mycursor.execute(sql)
    mydb.commit()

def updateStatusToNotWished():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    sql = "select id from events where date !='{}' and wishStatus='y'".format(date)
    mycursor.execute(sql)
    wished = mycursor.fetchall()
    for id in wished:
        sql = "update events set wishStatus='n' where id='{}'".format(id[0])
        mycursor.execute(sql)
        mydb.commit()

def checkIfBirthdayToday():
    date = datetime.datetime.now()
    day = date.strftime("%d")
    month = date.strftime("%m")
    sql = "select * from birthday where BirthdayDate={} and wishStatus='n' and birthdayMonth = {}".format(day,month)
    mycursor.execute(sql)
    birthdays = mycursor.fetchall()
    birthdaysToWish = []
    if len(birthdays):
        for birthday in birthdays:
            name = getContactNameFromUserId(birthday[4])
            message = birthday[5]
            birthdaysToWish.append([name,message])
    return birthdaysToWish

