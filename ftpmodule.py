from ftplib import FTP
import os, sys

from init_config import init_app
config = init_app('.sewd.conf')

print(config)

ftpconfig = config['FTP']

print(ftpconfig)


ftp_site = ftpconfig['site']
ftp_login = ftpconfig['login']
ftp_passwd = ftpconfig['passwd']

#look up and go into the build folder
build_folder = config.get('BUILD_FOLDER')

os.chdir(build_folder)
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
	
	

