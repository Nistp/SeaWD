Flas-ked blog by Seawd
..
More to add on later


Alright, what do we need:

- Static pages served by apache
    - landing page (contains links to all posts)
    - apache config

- flask page manager (seawd-api) 
    - takes GET / POST requests from seawd-cli
    - possibly re-renders landing page
    - instructs apache what to serve 

- command line utility
    - talks to seawd API (via curl maybe) 

- git integration

## Flask App example

`GET /articles` returns a list of all posts

`POST /articles` takes an article and puts it online


## Requirements, workflow:

- Posts are written in md /mmd
- you write posts locally, possibly all posts are versioned by git
- when you're ready to publish, run something like

> `seawd publish article-name`

_article-name_ is probably a folder that contains all relevant resources


../myarticle

├── chart.js

├── image1.png

├── image2.png

├── meta.yaml

└── myarticle.md


- Meta file will have author / date created / date published etc. it is created and managed by seawd-cli




## Tests

to test run `pytest`



## dependencies 

flask markdown pytest pygments pyCLI maybe.. etc.

eventually run
pip freeze > requirements.txt

To recreate this thing:

```
vitrualenv-3 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Thoughts

Keeping all articles under git is a good idea regargless, and there is no need to reinvent it. At most what we need is a thin layer on top of it to make things nicer.

- one folder -> one article -> one .git
- Creating a new article is roughly the same as `git init .`
- We can abstract away git add/commit/push.

We could make a shadow branch for automatically.

Alternative to this whole git thing is rsync. But it would merely syncronize folders. what if you want to rollback?

So now you have remote .git folders and a flask app that keeps track of them.

## How does it look
- work on your stuff locally.
- sync it with remote repo.
- notify app to publish / take down something
- perhaps monitor how often your articles get accessed.


