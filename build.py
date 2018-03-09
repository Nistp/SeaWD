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
    print('i should be aware of BUILD_FOLDER and project folder')
    print('assume build folder exists')
    print('article_temolate')

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


def build_all(projects):
    print('building all staged articles')
    print('if build folder isnt there, make it')
    for project, payload in project.keys():
        print(project)
        build_article(project)
        
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


# TODO: start working on the template
if __name__ == '__main__':
    t = 'templates/template.html'
    t = 'projects/sample.md'
    o = 'build/out.html'
    simple_build(t,m,o)
