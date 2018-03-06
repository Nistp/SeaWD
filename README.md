# sewdlog

> what?

yet another blog

> why?

dunno.

## Requirements, constraints

- easy cli workflow
- easy deploy to hosting, CDNs
- lightweight foundation, no bloat
- web standards, mobile first
- not having js on the client should not matter
- BONUS: make it run in command line browsers :D 


## WIP:

- python parkdown
    - md -> html

- Jinja2
    - decorates html with a light theme 

- linode / centos / apache (for now) 
    - serves static pages, no way

- cli (building with argparse for now)
    - facilitates local workflow
    - pushes projects to De Webs!

- git
    - versions / backs up blogposts



## How should it look
- Posts are written in md /mmd
- work on your stuff locally
- back up with git (if you so configure)
- push to hosting with one command
- perhaps monitor how often your articles get accessed

> would be nice to spam everyone on fb / linkedin / twitter every time you release a blog post (c) he who doesn't do social media 




### Project structure?

`sewd push <article-name>` 

<article_name> is a folder that contains all relevant resources

```
../myarticle
├── chart.js
├── image1.png
├── image2.png
├── meta.yaml
└── myarticle.md
```




## Development 

To create this thing:

```
vitrualenv-3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Tests

to test run `pytest`

*not that we have a real test suite*

## TO-DO:
1: meta file inside each project that tells whether it's staged for publication or notftp deploy module to shared hosting
2:html / css in template.html
3:function that builds all staged projects and a landing page and puts it all into the build folder
4: twitter thing
5: editor of choice setting in config, so that when you say you wanna work on a project, it opens your editor from within that folder. (vim / emacs / atom / notepad / whatever )
6: git - same thing, every project folder should be git initialized if git is in config
