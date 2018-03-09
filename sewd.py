import argparse # we might want to replace this later.

import os, sys  # for creating folders and files

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
    else: 
        os.mkdir(project_name)
        os.chdir(project_name) 

        with open(f'{project_name}.md', 'w') as f:
            f.write('# ArticleName') 

        write_toml_config({'name': project_name, 'todo': 'timestamp author status etc'},'.meta')
    print('TODO: open file in editor of choice')
    print('TODO: make a sane meta file')


def pusher(project_name):
    print('pushing.. {project_name}')
    pass

def builder(target):
    if target == 'all':
        projects = list_projects(None) # todo refactor this
        build_all(projects)
    else:
        build_article(target)


# we probably want to pre-build it eagerly and cache in some file for tab completion
def list_projects(target):
    print('TODO: keep track of what is published / in progress, etc')
    total = {}
    with os.scandir(config.get('PROJECTS_FOLDER')) as it:
        for item in it:
            if item.is_dir():
                print(f'{item.name} \t in progress \t ({item.path})')
                meta = read_toml_config(f'{item.path}/.meta')
                obj = {
                        item.name: {
                            'path': item.path,
                            'meta': meta
                            }
                        } 

                total.update(obj)
    print(total)
    return total


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



