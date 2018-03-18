#!/usr/bin/env python
import argparse 

import os, sys, subprocess, subprocess # note sys is unused
import shutil
from build import build_all, build_article # parsing utils and whatnot TODO: rename

from init_config import init_app, write_toml_config, read_toml_config # this is init application 


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
        return
 
    os.mkdir(project_name)
    os.chdir(project_name) 
    
    meta = {
           'title': project_name,
           'description': 'todo',
           'status': 'DRAFT'
        }

    write_toml_config(meta,'.meta')

    with open(f'{project_name}.md', 'w') as f:
        f.write('# ArticleName') 
   

    abspath = os.path.join(os.getcwd(), f"{project_name}.md")
    editor = config.get('USER').get('editor')
    subprocess.run([editor , abspath]) 
    print('goodbye')



def launch_editor(project_name):
    print(f"opening.. {project_name}")
    try:
        root = config.get('PROJECTS_FOLDER')
        project_folder = os.path.join(root, project_name) 
        os.chdir(project_folder)
    except:
        print(f'I cant get inside {project_folder}')
        return

    if os.path.exists(f"{project_name}.md"):
        abspath = os.path.join(os.getcwd(), f"{project_name}.md")
        editor = config.get('USER').get('editor')
        subprocess.run([editor , abspath]) 
    else:
        print(f'default {project_name}.md not found')
        # maybe attempt to read meta to see if project name was redefined
        #meta = read_toml_config('.meta')

    print('goodbye')



def pusher(project_name):
    print('pushing.. {project_name}')
    pass

def builder(target):
    if target == 'all':
        projects = list_projects(None) # todo refactor this
        build_all(projects, config)
    else:
        print('todo: ')
        #build_article(target)


# we probably want to pre-build it eagerly and cache in some file for tab completion
def list_projects(target, status='everything'):
    print('TODO: keep track of what is published / in progress, etc')


    with os.scandir(config.get('PROJECTS_FOLDER')) as it:
        items = [(item.name, item.path) for item in it if item.is_dir()]
    
    articles = [] 
    for name, path in items:
        metafilepath = os.path.join(path, '.meta')
        try:
            meta = read_toml_config(metafilepath)
            meta.update({
                'name': name, # name is like id
                'path' : path, #todo: date modified
                    }) 

            articles.append(meta)
        except:
            print(f'skipping {name} at {path}, no meta file')

    if status in ['DRAFT','STAGED','PUBLISHED','MODIFIED']: # todo better filter
        print(f'applying filter {status}')
        filtered = list(filter(lambda article: article.status == status, articles))
        articles = filtered

    for article in articles:
        print(f"{article.get('name')} \t {article.get('status')}")

    return articles



def purge_everything(target):
    if target=='all':
        if os.path.exists(CONFPATH):
            print(f'purging config at {CONFPATH}')
            os.remove(CONFPATH)
     
    if os.path.exists(config.get('PROJECTS_FOLDER')):
        print(f'purging config at {config.get("PROJECTS_FOLDER")}')
        shutil.rmtree(config.get('PROJECTS_FOLDER'))



#### 
parser = argparse.ArgumentParser('sewd')
parser.add_argument('action', help='make / push / parse ') 
parser.add_argument('target', help='project folder name') 

CONFPATH='.sewd.conf'
config = init_app(CONFPATH)

# TODO: look at argparse_practice
actions = {
    'make': maker,
    'edit': launch_editor,
    'push': pusher,
    'build': builder,
    'list': list_projects,
    'purge': purge_everything
        }


# parse arguments, try to match to any known actions
args = parser.parse_args()
func = actions.get(args.action)
target = args.target

if func:
    func(target)
else:
    print('didnt match any valid actions')



