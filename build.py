import markdown
from jinja2 import Template 

def read_file(filename):
    with open(filename) as f:
        content=f.read()
    return content


def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def md_to_html(renderer, md_text):
    article = markdown.markdown(md_text)
    html = renderer.render(article=article) 
    return html


def build_article(project_name):
    print('building {project_name}')
    ''' 
    base_name = input_file.split('.')[0]
    output_file = f'{base_name}.html'
    # set up a template
    template = read_file('template.html')
    renderer = Template(template)

    # populate a template
    article = read_file(input_file)
    html = md_to_html(renderer, article)

    print(f'writing {output_file}') 
    print('TODO: proper build process') 
    
    write_file(
            filename=output_file,
            content = html
            )
    '''


def build_all():
    print('building all staged articles')
    # get a list of all staged projects
    # feed that list to index.html template
    # for each staged project
    #   make a subfolder in the build forlder
    #   feed markdown et al to article.html template
    pass

# resulting folder should be:
#| public
#|- index.html
#|- /article1
#   |-contents? 
#|- /article2


