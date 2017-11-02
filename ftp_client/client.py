from ftplib import FTP
import sys

serv_ip = sys.stdin.readline()
serv_port = sys.stdin.readline()
serv_port = serv_port[:-1]

ftp = FTP('')
ftp.connect(serv_ip[:-1],int(serv_port))
ftp.login()
ftp.cwd('/phodu/Downloads/') #replace with your directory
print(ftp.retrlines('LIST'))

def uploadFile(filename):
 filename2 = 'upload' #replace with your file in your home folder
 uploadpath = filename[:-1]
 ftp.storbinary('STOR '+filename2, open(uploadpath, 'rb'))
 ftp.quit()

def downloadFile(filename):
 filename2 = 'download'
 localfile = open(filename2, 'wb')
 ftp.retrbinary('RETR ' + filename[:-1], localfile.write, 1024)
 ftp.quit()
 localfile.close()

filename = sys.stdin.readline()
downloadFile(filename)

upfilename = sys.stdin.readline()
uploadFile(upfilename)
