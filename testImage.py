import os


os.system('raspistill -o image1.jpg')

localfile = 'image1.jpg'
remotehost = '193.191.187.55'
remotefile = '/var/www/img/image.jpg'

os.system('scp "%s" "%s:%s"' % (localfile, remotehost, remotefile) )
