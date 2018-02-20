import markdown
from jinja2 import Template 

def read_file(filename):
    with open(filename) as f:
        content=f.read()
    return content

template = read_file('template.html')
renderer = Template(template)

def parse_md(md_text):
    article = markdown.markdown(md_text)
    html = renderer.render(article=article) 
    return html





article = read_file('README.md')
html = parse_md(article)

print(html)



