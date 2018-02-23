import markdown
import argparse # we might want to replace this later.

import os, sys  # for creating folders and files

import lame

parser = argparse.ArgumentParser('sewd')
parser.add_argument('action', help="make / push / config") 
parser.add_argument('target', help="project folder name") 


def maker(projectname):
    print(f"making.. {projectname}")
    #os.chdir("path")  # set the path to the article folder
    #if not os.path.exists(projectname): # check that folder doesn't exist yet
    #    os.mkdir(projectname) # create a folder
    #os.chdir(projectname) # cd in it/do we need an exception for this?
    #meta = open("meta.yaml", r+) # what goes in here?
    #post = open("post.md", r+) # what goes in here?



def pusher(projectname):
    print('pushing.. {projectname}')
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



