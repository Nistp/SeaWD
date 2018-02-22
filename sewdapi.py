import markdown
import argparse # we might want to replace this later.

import os, sys  # for creating folders and files

path = 'Documents/Python_Env/Seawd_Blog'  #  set path for the article folder

# TODO: accept cli args

# sewd --help
# sewd make <article-name>
# sewd publish <article-name>
# sewd ls
# sewd takedown <article-name> 


parser = argparse.ArgumentParser(prog='SewdAPI')
##parser.add_argument('--make' , help="Make the target") 
##parser.add_argument('--push', help="Push the article on Git")
##parser.add_argument('--config', help="Config of smth")
parser.add_argument('action', help = "make / push / config")

# We could add subparses to make this look neater instead

# seems like there isn't a command to just create a file and not open it
# should we add exceptions to these two then?

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
    #if make

    #elif push

    #elif config
else:
    print('didnt match any valid actions')
