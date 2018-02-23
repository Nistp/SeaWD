import markdown
import argparse # we might want to replace this later.

import os, sys  # for creating folders and files

import lame

parser = argparse.ArgumentParser('sewd')
parser.add_argument('action', help='make / push / config') 
parser.add_argument('target', help='project folder name') 


def maker(project_name):
    print(f'making.. {project_name}')
    print(f'__file__ is {__file__}')
    print(f'path to file is {os.path.abspath(__file__)}')
    print('now how your path is different from my path')
    root_folder = os.path.dirname((os.path.abspath(__file__))) # can be made grapes again
    os.chdir(root_folder)   
    print('TODO: make amd use all_projects foolder path from yaml config')

    if os.path.exists(project_name):
        print('project exists, moving there..')
    else: 
        os.mkdir(project_name)
    os.chdir(project_name) # these might need to be relative, with os.path.join()

    with open(f'{project_name}.md', 'w') as f:
       f.write('# test') 
    


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



