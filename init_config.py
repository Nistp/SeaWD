import argparse
import os, sys
import toml




def get_default_folder_path(target_folder='projects'):
    root_folder = os.path.dirname(os.path.abspath(__file__))
    projects_path = os.path.join(root_folder, target_folder)
    if not os.path.exists(projects_path):
        print(f'default folder {target_folder} does not exist, creating it')
        os.mkdir(projects_path)
    return projects_path  


def get_projects_path():
    projects_path = conf.get('PROJECTS_FOLDER')
    if projects_path is None:
        print('`PROJECTS_FOLDER` was not specified. Getting default')
        return get_default_projects_path()
    return projects_path 


def read_toml_config(path_to_config):
    with open(path_to_config, 'r') as f:
        conf = toml.load(f) 
    return conf 


def write_toml_config(config, path_to_config):
    with open(path_to_config, 'w') as f:
        toml.dump(config, f)



def init_config(CONFPATH='.sewd.conf'):
    print(f'creating a new config file: {CONFPATH}')
    username = input('Enter your name:\n'),
    user = ''.join(username)
    print(f'[USER] - {user} accepted')
    print('[FTP] - edit .sewd.conf file to set up ftp login credentials')
    ftp_site = ''
    ftp_login = ''
    ftp_passwd = ''

    FTP = {'site': ftp_site, 'login':ftp_login, 'passwd':ftp_passwd}
    TWITTER = {
            'access_key': '', 
            'access_secret':'', 
            'consumer_key': '', 
            'consumer_secret':'', 
            }
    PROJECTS_FOLDER = get_default_folder_path(target_folder='projects')
    BUILD_FOLDER = get_default_folder_path(target_folder='public')
   
    config = {
        'USER': {'name': user},
        'FTP': FTP,
        'TWITTER': TWITTER,
        'BUILD_FOLDER': BUILD_FOLDER,
        'PROJECTS_FOLDER': PROJECTS_FOLDER
        }
    return config


# try to read CONFPATH 
# if not there - initialize it
# this init function is a bit dangerous.
def init_app(CONFPATH='.sewd.conf'):
    print(f'loading config from {CONFPATH}')
    if os.path.exists(CONFPATH):
        config = read_toml_config(CONFPATH) #if it exists
    else:
        print(f'{CONFPATH} does not exist yet.')
        config = init_config(CONFPATH)
        print('writing config file')
        write_toml_config(config=config, path_to_config=CONFPATH)
    try:
        pfolder = config.get('PROJECTS_FOLDER')
        assert os.path.exists(pfolder)
    except:
        print(f'the project folder {pfolder} is defined in config but I could not find it! :O')

    return config
