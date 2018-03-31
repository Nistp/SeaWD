
# TODO: use decorators as means to register 
#   user defined routines and run them from the framework


# Mock up of how I see this
# we expose checkpoint decorators to the user (TODO come up with better terminology)
# so that he can inject his own behavior (e.g. add categories to the article object and later use it in the template)
# all decorated functions get called by the framework in predefined places
# in code, we just do a lookup and run all functions that were "registered", in order in which they were defined in the user_decor file. (TODO come up with better names,seriously...)
# 

registry = {
    'checkpoint1': [],
    'checkpoint2': [],
    }

def main_function():
    # initialize config and whatnot
    global_object = {'potato' : 'tomato'}


    print('Framework: im about to call all functions that were\n \
    "registered" on checkpoint 1 of projects lifetime.\n \
    example of such checkpoint - "new_project_created" ')
    for func in registry['checkpoint1']:
        func(global_object)

    print('Framework: about to call all code bound to checkpoint 2\n \
    example - "project_built_for_preview" ')
    for func in registry['checkpoint2']:
        func(global_object)

    print('Framework: done with step2')
    print('Framework: state of the system is now:')
    print(global_object)

def checkpoint1(f):
    def wrapper(*args, **kwargs):
        print(f'\nFramework: checkpoint1. calling {f.__name__}')
        f(*args, **kwargs)
        print('Framework: done with this checkpoint1 handler\n')
    registry['checkpoint1'].append(wrapper)
    print(f'Framework: registered {f.__name__} on checkpoint1')
    #return wrapper


def checkpoint2(f):
    def wrapper(*args, **kwargs):
        print(f'\nFramework: checkpoint2. calling {f.__name__}')
        f(*args, **kwargs)
        print('Framework: done with this checkpoint2 handler\n')
    registry['checkpoint2'].append(wrapper)
    print(f'Framework: registered {f.__name__} on checkpoint2')




