from bottle import route, run
from sys import argv

@route('/')
def index():
    output = '<h1> Halló heimur! <h1>'
    output1 = '<h2><a href=/page1>Síða eitt</a></h2>'
    output2 = '<h2><a href=/page2>Síða tvo</a></h2>'
    output3 = '<h2><a href=/page3>Síða þrju</a></h2>'
    return output, output1, output2, output3

@route('/page1')
def page1():
    output = '<h2><a href =/>Aftur til index</a></h2>'
    output1 = '<h1>Þú ert á síðu eitt</h1>'
    return output, output1

@route('/page2')
def page2():
    output = '<h2><a href=/>Aftur til index</a><h2>'
    output1 = '<h1>Þú ert á síðu tvö</h1>'
    return output, output1

@route('/page3')
def page3():
    output = '<h2><a href=/>Aftur til index</a><h2>'
    output1 = '<h1>Þú ert á síðu þrjú</h1>'
    return output, output1

run(host='0.0.0.0', port=argv[1], debug=True)