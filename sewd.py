import markdown
import argparse # we might want to replace this later.

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
    # check that folder doesn't exist yet
    # create a folder
    # cd in it
    # create a meta.yaml file
    # create a post.md file
    # attempt to open it if config knows which editor to use



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


