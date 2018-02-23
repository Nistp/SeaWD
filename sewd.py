import argparse # we might want to replace this later.

import os, sys  # for creating folders and files

import lame # parsing utils and whatnot TODO: rename

parser = argparse.ArgumentParser('sewd')
parser.add_argument('action', help='make / push / config') 
parser.add_argument('target', help='project folder name') 


def maker(project_name):
    print(f'making.. {project_name}')
    print(f'path to file is {os.path.abspath(__file__)}')
    root_folder = os.path.dirname(os.path.abspath(__file__)) 
    all_projects_folder = os.path.join(root_folder, 'projects')
    assert os.path.exists(all_projects_folder)
    os.chdir(all_projects_folder)   

    if os.path.exists(project_name):
        print('project already exists')
    else: 
        os.mkdir(project_name)
        os.chdir(project_name) 

        with open(f'{project_name}.md', 'w') as f:
            f.write('# test') 

    print('TODO: open file in editor of choice')


def pusher(project_name):
    print('pushing.. {project_name}')
    pass


def configer():
    pass


actions = {
    'make':maker,
    'push': pusher,
    'config': configer,
    'parse': lame.build_article
        }


# parse arguments, try to match to any known actions
args = parser.parse_args()
func = actions.get(args.action)

if func:
    func(args.target)
else:
    print('didnt match any valid actions')



