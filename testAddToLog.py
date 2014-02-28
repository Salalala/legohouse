from logToDb import initConn as initConn
from logToDb import logAlarm as logAlarm

cur, conn = initConn()
logAlarm(cur, conn, 'door opened')
cur, conn = initConn()
logAlarm(cur, conn, 'safe opened')
cur, conn = initConn()
logAlarm(cur, conn, 'pressure plate triggered')
 
