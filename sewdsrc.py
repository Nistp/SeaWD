#The source for the sewdapi, so it actually is more of an API
#Hiding implementation details is a good thing too, typically

def maker(projectname):
    print('making.. {projectname}')
    # TODO: validate projectname 
    # lower_case_acticle_name_with_underscohes
    os.chdir("path")  # set the path to the article folder
    if not os.path.exists('projectname') # check that folder doesn't exist yet
      os.mkdir('projectname') # create a folder
    os.chdir('projectname') # cd in it/do we need an exception for this?
    ##meta = open("meta.yaml", r+) # what goes in here?
    ##post = open("post.md", r+) # what goes in here?

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

