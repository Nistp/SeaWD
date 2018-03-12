#!/usr/bin/env python
import argparse
import readline
import cmd

import argcomplete
from argcomplete.completers import ChoicesCompleter

# 


#TODO: demo autocompletion < e.g. from the list of articles
#TODO: brainstorm more useful commands

#https://docs.python.org/3/library/os.html

# alternatively 
#sewd switch on <article-name> 
#sewd switch off <article-name> 
#autocomplete based on the pre-made list of projects

# within each project folder
# sewd info
# 

def make_new_article(args):
    print(f'test {args.article}')

def work_on_article(args):
    print(f'test {args.article}')

def list_projects(args):
    if args.status:
        print(f'showing only {args.status} articles')
    else:
        print('showing all articles')


parser = argparse.ArgumentParser('sewd')
parser.add_argument('--version', action='version', version='0.1')

subparsers = parser.add_subparsers()

make_parser = subparsers.add_parser('make', help="make a new article")
make_parser.add_argument('article', help="article name")
make_parser.set_defaults(func=make_new_article)

# choices --> all avaliable projects. i would love to tab-complete them =(
edit_parser = subparsers.add_parser('edit', help="edit an existing article")
edit_parser.add_argument('article',  choices=( 'first-choice', 'second-choice' ), help="article name")
edit_parser.set_defaults(func=work_on_article)
#edit_parser.completer = ChoicesCompleter(( 'first-choice', 'second-choice' ))

list_parser = subparsers.add_parser('list', help="make a new article")
list_parser.add_argument('--status', help="show only pub / dev projects") # not ideal
list_parser.set_defaults(func=list_projects)

argcomplete.autocomplete(parser)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)



#todo
def tests():
    #sewd make <article-name>
    #sewd edit <article-name>
    #sewd publish <article-name>

    # sewd list 
    # sewd list --status=dev # todo: sewd list dev

    pass # tests pass, lol
