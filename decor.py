
# TODO: use decorators as means to register 
#   user defined routines and run them from the framework

def hooked(f):

    def wrapper(*args, **kwargs):
        print('before')
        f(*args, **kwargs)
        print('after')

    return wrapper


@hooked
def myfunction(l,r,u='nah'):
    print(f'{l}, {r}, {u}')


myfunction(l='1',r='e', u='fff')
myfunction(l='1',r='e')

