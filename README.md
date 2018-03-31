...project redesign is nigh...

## Requirements, Constraints

- easy cli workflow
- easy deploy to hosting, CDNs
- lightweight foundation, no bloat
- web standards, mobile first
- extensible (to an extent)

- config file is in TOML
- all projects are git versioned
- pipeline hooks are exposed as decorators
- plugins? TODO
- templates are exposed and modifiable


## How should it look
- Write posts in md /mmd
- Work on your stuff locally
- Back up with git 
- Push to hosting with one command
- [WIP] monitor how often your articles get accessed

## WIP:
- python markdown (TODO: support dialects)
- Jinja2 (TODO: take a look at Chameleon)
- argparse & cli tooling (TODO: autocomplete)
- git (TODO: git init all projects)
- neocities (TODO: polish deploy, API)


## TODO: (TODO: update TODO)
- meta file inside each project that tells whether it's staged for publication or not
- ftp deploy module to shared hosting
- html / css in template.html
- function that builds all staged projects and a landing page and puts it all into the build folder
- twitter thing
- editor of choice setting in config, so that when you say you wanna work on a project, it opens your editor from within that folder. (vim / emacs / atom / notepad / whatever )
- git - same thing, every project folder should be git initialized if git is in config


## Research TODO

Well, the denial phase is over and now that we're invested enough in this little project... **time to do our homework**

### static site projects
- katana
- jekyll
- gatsby

### What we need to scout:
- folder tree structure and naming conventions
- build process
- configuration and deployment


### Project structure?

```
../myarticle
├── chart.js
├── image1.png
├── image2.png
├── .meta.toml
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
*not that we have a real test suite* __yet__

