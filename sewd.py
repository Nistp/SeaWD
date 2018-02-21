import markdown
import argparse # we might want to replace this later.

import os, sys  # for creating folders and files

path = ... #  set path for the article folder

# TODO: accept cli args

# sewd --help
# sewd make <article-name>
# sewd publish <article-name>
# sewd ls
# sewd takedown <article-name> 


parser = argparse.ArgumentParser('sewd')
parser.add_argument('action', help="make / push / config") 
parser.add_argument('target', help="project folder name") 


def maker(projectname):
    print('making.. {projectname}')
    # TODO: validate projectname 
    # lower_case_acticle_name_with_underscohes
    os.chdir("path")  # set the path to the article folder
    if not os.path.exists('projectname') # check that folder doesn't exist yet
      os.mkdir('projectname') # create a folder
    os.chdir('projectname') # cd in it/do we need an exception for this?
    meta = open("meta.yaml", r+) # what goes in here?
    post = open("post.md", r+) # what goes in here?
    # seems like there isn't a command to just create a file and not open it
    # should we add exceptions to these two then?



def pusher(projectname):
    print('pushing.. {projectname}')
    pass


def configer():
    # TODO:
    # credentials, author's name,  
    # server to talk to, authentication
    # remote git?
    # 
    pass


# fugly pattern match dictionary
actions = {
    'make':maker,
    'push': pusher 
    'config': configer 
        }


# parse arguments, try to match to any known actions
args = parser.parse_args()
func = actions.get(args.action)

if func:
    func(args.target)
else:
    print('didnt match any valid actions')


