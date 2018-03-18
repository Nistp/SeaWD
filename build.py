import markdown
from jinja2 import Environment, FileSystemLoader

import os, shutil


def read_file(filename):
    with open(filename) as f:
        content=f.read()
    return content

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def md_to_html(md_text):
    html = markdown.markdown(md_text)
    return html

# might want to do build_folder IO outside of this func
def build_article(article, template, build_folder):
    print(f'building {article.get("name")}\nfolder: {article.get("path")} ')
    print(article)
    path_to_md = os.path.join(article.get('path'), f'{article.get("name")}.md')
    # assert that's the case or explicitly require path to md
    markdown = read_file(path_to_md)
    markup = md_to_html(markdown)
    html = template.render(article=markup)
    # determine the build name
    output_path = os.path.join(build_folder, f'{article.get("name")}.html') 
    write_file(filename=output_path, content=html) 
    print(f'maybe success, check {output_path}')



    # get a list of all staged projects
    # feed that list to index.html template
    # for each staged project
    #   make a subfolder in the build forlder
    #   feed markdown et al to article.html template
def build_all(articles, config, build_folder=None):
    print('TODO: make clean')
    print('TODO: if build folder isnt there, make it')
    if not build_folder:
        build_folder = config.get('BUILD_FOLDER')

    env = Environment(
            loader = FileSystemLoader('templates')
            )

    print('TODO: building landing page here')
    index_template = env.get_template('index.html')
    html = index_template.render(articles=articles)
    output_path = os.path.join(build_folder, 'index.html') 
    write_file(filename=output_path, content=html) 

    print('building projects')
    template = env.get_template('template.html')

    for article in articles:
        # TODO: make a dir and put everything there, 
        # otherwise projects will overwrite each others resources.
        build_article(article, template, build_folder)
        print(article['path'])
        with os.scandir(article['path']) as it:
            resources = [(item.name, item.path) for item in it if item.name not in ['.meta', f"{article.get('name')}.md"]]
        
        print(resources)
        print('about to change these')
        for name, path in resources:
            print(f"name is {name}, path is {path}. I copy it in {build_folder}")
            shutil.copy2(src=path, dst=os.path.join(build_folder, name)) #see if preserves date modified, permissions


def simple_build(template, markdown, out):
    md = read_file(markdown)
    markup = md_to_html(md)
    rndr = template.render(article=markup)
    print(rndr)
    write_file(out, rndr)
    print('success!') 

