import markdown
import argparse

parser = argparse.ArgumentParser('sewd')
parser.add_argument('init', help="create a new article folder") 
parser.add_argument('list', help="list local projects") 
parser.add_argument('edit', help="edit a project") 
parser.add_argument('push', help="upload an article") 

args = parser.parse_args()

print(args)

# TODO: accept cli args

# sewd --help
# sewd make <article-name>
# sewd publish <article-name>
# sewd ls
# sewd takedown <article-name> 

