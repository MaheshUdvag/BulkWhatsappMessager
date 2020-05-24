import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database = "autowisher"
)


mycursor = mydb.cursor()

def addUser():
  name = input("Enter name ")
  contactName = input("Enter contactName as per whatsapp ")
  sql = "insert into users(name,ContactName) VALUES (%s, %s)"
  val = (name, contactName)
  try:
    mycursor.execute(sql, val)
    mydb.commit()
  except mysql.connector.Error as err:
    print(err.msg)

def getUserIdByContactName(contactName):
  sql = "Select id from users where contactName ='{}'".format(contactName)
  mycursor.execute(sql)
  users = mycursor.fetchall()
  if len(users):
    return users[0][0]
  else: 
    return 0

def getNameByUserId(userId):
  sql = "Select name from users where id={}".format(userId)
  mycursor.execute(sql)
  users = mycursor.fetchall()
  if len(users):
    return users[0][0]
  else:
    return 0

def addBirthdayForUser():
  contactName = input("enter contact name ")
  userId = getUserIdByContactName(contactName)
  name =  getNameByUserId(userId)
  if userId == 0 or name == 0:
    print("invaild details")
    return
  birthdayMonth = input("enter the month of birth (eg-4 for April) ")
  birthdayDate = input("Enter the day of birth (eg-12 for 12th) ")
  bdayMessage = "Wish you a very happy birthday " +name
  print("Default message: "+bdayMessage)
  custom = input("Do you want to add a custom message y/n ")
  if custom == 'y' or custom =="Y":
    bdayMessage = input("Enter your message ")
  sql = "insert into birthday(birthdayMonth,birthdayDate,wishStatus,userId,message) VALUES (%s,%s,%s,%s,%s)"
  val = (birthdayMonth,birthdayDate,'n',userId,bdayMessage)
  try:
    mycursor.execute(sql, val)
    mydb.commit()
  except mysql.connector.Error as err:
    print(err.msg)

def getEventIdByName(eventName):
  sql = "Select id from events where eventName={}".format(eventName)
  mycursor.execute(sql)
  id = mycursor.fetchall()
  if len(id):
    return id[0][0]
  else:
    return 0

def addEvent():
  showEvents()
  eventName = input("enter event name  ")
  date = input("enter date of event format YYYY-MM-DD  ")
  message = input("Enter message to be sent  ")
  sql = "insert into events(eventName,date,message,wishStatus) VALUES (%s,%s,%s,%s)"
  val = (eventName,date,message,'n')
  mycursor.execute(sql, val)
  mydb.commit()
  print("added event successfully")

def addAllUsersToAnEvent():
  showEvents()
  eventId = int(input("enter eventId"))
  if checkIfEventExist(eventId):
    sql = "select id from users"
    mycursor.execute(sql)
    users = mycursor.fetchall()
    for user in users:
      if checkIfUserNotInEvent(user[0],eventId):
        continue
      sql = "insert into eventMapper(eventId,userId) VALUES (%s,%s)"
      val = (eventId,user[0])
      try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("added successfully")
      except mysql.connector.Error as err:
        print("user already exist")

def checkIfUserNotInEvent(userId,eventId):
  sql = "select * from eventMapper where eventId={} and userId={}".format(eventId,userId)
  mycursor.execute(sql)
  users = mycursor.fetchall()
  if len(users):
    return True
  return False

def showEvents():
  sql = "select id,eventName,date from events"
  mycursor.execute(sql)
  events = mycursor.fetchall()
  if len(events) == 0:
    print("No events")
    return
  print("Events existing ")
  for event in events:
    print(str(event[0])+" "+event[1])

def checkIfEventExist(eventId):
  sql = "Select * from events where id={}".format(eventId)
  mycursor.execute(sql)
  events = mycursor.fetchall()
  if len(events) == 0:
    return False
  return True

def checkIfUserInEvent(userId,eventId):
  sql = "select * from eventMapper where eventId = {} and userId = {}".format(eventId,userId)
  mycursor.execute(sql)
  check = mycursor.fetchall()
  if len(check)==0:
    return True
  return False

def AddUserToEvent():
  contactName = input("enter contact name ")
  userId = getUserIdByContactName(contactName)
  name =  getNameByUserId(userId)
  if userId == 0 or name == 0:
    print("invaild details")
    return
  showEvents()
  eventId = input("Enter eventId ")
  if checkIfUserInEvent(userId,eventId) and checkIfEventExist(eventId):
    sql = "insert into eventMapper(eventId,userId) VALUES (%s,%s)"
    val = (eventId,userId)
    try:
      mycursor.execute(sql, val)
      mydb.commit()
      print("added successfully")
    except mysql.connector.Error as err:
      print("\nuser already exist")
  else:
    print("user already exists")

def showUsers():
  sql = "select name from users"
  mycursor.execute(sql)
  users = mycursor.fetchall()
  if len(users):
    print("  name ")
    for user in users:
      print("  "+user[0])


ch='y'
while ch=='y' or ch=='Y':
  print("1. Add event")
  print("2. Add birthday")
  print("3. Add user")
  print("4. Add user to an event")
  print("5. show users")
  print("6. Add all users to an event")
  choice = int(input("Enter a choice number "))
  print("\n")
  if choice == 1:
    addEvent()
  elif choice == 2:
    addBirthdayForUser()
  elif choice == 3:
    addUser()
  elif choice == 4:
    AddUserToEvent()
  elif choice ==5:
    showUsers()
  elif choice == 6:
    addAllUsersToAnEvent()
  print("\n")
  ch=input("to continue press y else press enter to exit ")

