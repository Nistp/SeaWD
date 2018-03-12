import markdown
from jinja2 import Environment, FileSystemLoader

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


def build_article(article):
    print(f'TODO: building {article.get("name")}')
    print(f'folder: {article.get("path")} ')


def build_all(articles):
    print('TODO: if build folder isnt there, make it')
    print('TODO: building landing page here')


    for article in articles:
        print(article['name'])
        build_article(article)
        
    # get a list of all staged projects
    # feed that list to index.html template
    # for each staged project
    #   make a subfolder in the build forlder
    #   feed markdown et al to article.html template
    pass


def simple_build(template, markdown, out):
    md = read_file(markdown)
    markup = md_to_html(md)
    env = Environment(
            loader = FileSystemLoader('templates')
            )
    template = env.get_template('template.html')
    rndr = template.render(article=markup)
    print(rndr)
    write_file(out, rndr)
    print('success!') 






# TODO: start working on the template
if __name__ == '__main__':
    t = 'template.html'
    m = 'sample.md'
    o = 'build/out.html'
    simple_build(t,m,o)
