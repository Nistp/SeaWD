import neocities
import os, sys

#import config

#path to the project folder/article folder
path = ...

#once in the right public folder, we can create a neocities object
sewdtest = neocities.NeoCities(neocities_user, neocities_pwd)

print('Deploying...')

#for file in the folder; -- have to pass a tuple of name to be displayed on server and name of the file locally
sewdtest.upload(('{filename}', '{filename}'))