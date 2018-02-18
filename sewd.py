import markdown
import argparse

# TODO: accept cli args

# sewd --help
# sewd make <article-name>
# sewd publish <article-name>
# sewd ls
# sewd takedown <article-name> 


parser = argparse.ArgumentParser('sewd')
parser.add_argument('action', help="make / push") 
parser.add_argument('target', help="project folder name") 



def maker(projectname):
    print('making.. {projectname}')
    pass

def pusher(projectname):
    print('pushing.. {projectname}')
    pass


# fugly pattern match dictionary
dispatch = {
    'make':maker,
    'push': pusher 
        }


args = parser.parse_args()


dispatch[args.action](args.target)



