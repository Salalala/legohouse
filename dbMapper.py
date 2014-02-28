#!/usr/bin/python3.2


import psycopg2
import datetime
import time

def initConn():
	#Connect to an existing database
	try:
        	conn = psycopg2.connect("dbname='legosecure' user='bram' host='193.191.187.55' password='DVO0HSruHaue'");
	except:
        	print "I am unable to connect to the database"

	#Open a cursor to perform database operations
	cur = conn.cursor()
	return cur, conn

#Log the alarms to the db
def logAlarm(cur, conn, trigger):
	if trigger is not None:
		#Insert into log
		query= "INSERT INTO legosecure.log(datetime, message) VALUES (now(), '"
        	query+=trigger
        	query+="');"
		cur.execute(query)
		
		cur.execute("SELECT * from legosecure.log")
		#Make Persistent
		conn.commit()
		
		#Close communication with the database
		cur.close()
		conn.close()

#Get the id from the last picture submitted in the db
def getIdFromLastPicture(cur, conn):
	cur.execute("select * from legosecure.photo order by datetime desc limit 1;")
	row = cur.fetchone()
	
	#Close communication with the database
	cur.close()
	conn.close()
	#Return the id from the last picture submitted in the db
	return row[0]

#Log photos to the db
def logPhoto(cur, conn, idFromNextPicture):
	imagePath = "/img/image" +  str(idFromNextPicture) + ".jpg"
	query= "INSERT INTO legosecure.photo(datetime, imageurl) VALUES (now(), '"
	query+=imagePath
	query+="');"
	cur.execute(query)
	conn.commit()
	
	#Close communication with the database
	cur.close()	
	conn.close()
