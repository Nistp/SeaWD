from ftplib import FTP
import os, sys
#from init_config import * #change to a more sensible access to ftp data

project_name = 'test_project'
ftp_site = config.get('ftp_site')
ftp_login = config.get('ftp_login')
ftp_passwd = config.get('ftp_passwd')

#look up and go into the build folder
pfolder = 'C:/Users/Nikolay/Documents/Python Scripts/test_proj'	#config.get('PROJECTS_FOLDER')
os.chdir(pfolder)
os.chdir(project_name)
files = os.listdir()
#look up remote ftp and make a build folder and change into it 
print("Logging into host")
ftpseawd = FTP(host=ftp_site, user=ftp_login, passwd=ftp_passwd)
ftpseawd.cwd('content')
folderName = project_name
if folderName in ftpseawd.nlst():
	print(f'{project_name} directroy already exists')
	ftpseawd.cwd(project_name)
else:
	ftpseawd.mkd(project_name)
	ftpseawd.cwd(project_name)
#transfer files from local to remote
for filename in files:
	ftpseawd.storbinary(f"STOR {filename}", open(f'{filename}', 'rb'))
	
	

