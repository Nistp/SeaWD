import markdown


def test_md():
    html = markdown.markdown('# hello world')
    assert html == '<h1>hello world</h1>'




