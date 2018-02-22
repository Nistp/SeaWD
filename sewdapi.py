#import markdown
import argparse # we might want to replace this later.
import sewdsrc

parser = argparse.ArgumentParser(prog='SewdAPI')
parser.add_argument("--make" , help="Make the target") 
parser.add_argument("--push", help="Push the article on Git")
parser.add_argument("--config", help="Config of smth")
#parser.add_argument('action', help = "make / push / config")
args = parser.parse_args()

path = 'Documents/Python_Env/Seawd_Blog'  #  set path for the article folder

# TODO: accept cli args

# sewd --help
# sewd make <article-name>
# sewd publish <article-name>
# sewd ls
# sewd takedown <article-name> 




# We could add subparses to make this look neater instead

# seems like there isn't a command to just create a file and not open it
# should we add exceptions to these two then?

# fugly pattern match dictionary
actions = {
    'make':maker,
    'push': pusher, 
    'config': configer 
        }


# parse arguments, try to match to any known actions

#func = actions.get(args.action)
 
#if func:
    #func(args.target)

if args.make:
    projectname = str.input("Please enter project/article name!")
    maker(projectname)
elif args.push:
    projectname = str.input("Which article would you like to push?")
    push(projectname)
elif args.config:
    config()

else:
    print('Didnt match any valid actions')

