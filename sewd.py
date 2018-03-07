import argparse # we might want to replace this later.

import os, sys  # for creating folders and files

from build import build_all, build_article # parsing utils and whatnot TODO: rename

from init_config import init_app # this is init application 


def maker(project_name):
    print(f"making.. {project_name}")
    try:
        pfolder = config.get('PROJECTS_FOLDER')
        os.chdir(pfolder)
    except:
        print(f'I cant get inside {pfolder}')
        return

    if os.path.exists(project_name):
        print('project already exists')
    else: 
        os.mkdir(project_name)
        os.chdir(project_name) 

        with open(f'{project_name}.md', 'w') as f:
            f.write('# ArticleName') 

    print('TODO: open file in editor of choice')


def pusher(project_name):
    print('pushing.. {project_name}')
    pass

def builder(target):
    if target == 'all':
        build_all()
    else:
        build_article(target)

def list_projects(target):
    if target == 'all':
        print('showing all')
    print('TODO: keep track of what is published / in progress, etc')
    with os.scandir(config.get('PROJECTS_FOLDER')) as it:
        for item in it:
            if item.is_dir():
                print(item)
    
    




parser = argparse.ArgumentParser('sewd')
parser.add_argument('action', help='make / push / parse ') 
parser.add_argument('target', help='project folder name') 


config = init_app()

actions = {
    'make':maker,
    'push': pusher,
    'build': builder,
    'list': list_projects
        }


# parse arguments, try to match to any known actions
args = parser.parse_args()
func = actions.get(args.action)
target = args.target

if func:
    func(target)
else:
    print('didnt match any valid actions')



