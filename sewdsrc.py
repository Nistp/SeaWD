#The source for the sewdapi, so it actually is more of an API
#Hiding implementation details is a good thing too, typically
import os, sys

def maker(projectname):
    print('making.. {projectname}')
    # TODO: validate projectname 
    # lower_case_acticle_name_with_underscohes
    os.chdir(path)  # set the path to the article folder
    if not os.path.exists(projectname) # check that folder doesn't exist yet
      os.mkdir(projectname) # create a folder
      os.chdir(projectname) # cd in it/do we need an exception for this?
    ##meta = open("meta.yaml", r+) # what goes in here?
    ##post = open("post.md", r+) # what goes in here?
       testfile = open("testfile.txt", r+)
    
def pusher(projectname):
    print('pushing.. {projectname}')
    


def configer():
    # TODO:
    # credentials, author's name,  
    # server to talk to, authentication
    # remote git?
    # testing of the method
    print("This is the configuration method!")

