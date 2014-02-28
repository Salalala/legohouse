import os
from dbMapper import initConn as initConn
from dbMapper import getIdFromLastPicture as getIdFromLastPicture
from dbMapper import logPhoto as logPhoto

#Make connection
cur, con = initConn()

#Determine id for next picture
id = getIdFromLastPicture(cur, con)
idFromNextPicture = int(id) + 1

#Make imagename that the next picture needs to have
imageName = "image" + str(idFromNextPicture) + ".jpg"
#Determine path for the image locally on the pi
imagePath = "/etc/scripts/img/" + imageName
#Make picture
os.system('raspistill -o "%s"' % (imagePath) )
print(imagePath)
#Define remote host and remote file location for scp
remotehost = '193.191.187.55'
remotefile = '/var/www/img/'+ imageName

#Copy image from pi to webserver
os.system('scp "%s" "%s:%s"' % (imagePath, remotehost, remotefile) )

#Log this picture to the db
cur, con = initConn()
logPhoto(cur, con, idFromNextPicture)

