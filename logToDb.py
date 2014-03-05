# 2014.03.05 14:35:27 CET
import psycopg2
import datetime
import time

def initConn():
    try:
        conn = psycopg2.connect("dbname='legosecure' user='bram' host='193.191.187.55' password='DVO0HSruHaue'")
    except:
        print 'I am unable to connect to the database'
    cur = conn.cursor()
    return (cur, conn)



def logAlarm(cur, conn, trigger):
    if trigger is not None:
        query = "INSERT INTO legosecure.log(datetime, message) VALUES (now(), '"
        query += trigger
        query += "');"
        cur.execute(query)
        cur.execute('SELECT * from legosecure.log')
        conn.commit()
        cur.close()
        conn.close()



def getIdFromLastPicture(cur, conn):
    cur.execute('select * from legosecure.photo order by datetime desc limit 1;')
    row = cur.fetchone()
    print '\n Laatste entry in photo tabel:\n'
    print '',
    print row[0],
    print row[1],
    print row[2]
    cur.close()
    conn.close()
    return row[0]



def logPhoto(cur, conn, idFromNextPicture):
    imagePath = '/img/image' + str(idFromNextPicture) + '.jpg'
    print imagePath
    query = "INSERT INTO legosecure.photo(datetime, imageurl) VALUES (now(), '"
    query += imagePath
    query += "');"
    print query
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()



+++ okay decompyling logToDb.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.03.05 14:35:29 CET
