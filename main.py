import bottle
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import DictLoader

from bottle import(
        run,
        route,
        mako_view as view, #THIS IS SO THAT @view uses mako
        request,
        hook,
        static_file,
        redirect
        )

from bottle import mako_template as template #use mako template

template = """\
@require(name)
Hello, @name"""

engine = Engine(
    loader=DictLoader({'x': template}),
    extensions=[CoreExtension()]
)
template_w = engine.get_template('x')



@route("/main")
@view("mainpage.tpl")
def main_page():
    return 

@route("/")
def working():
    return "Site en maintenance"

@route("/example1")
def html_example1(name="WOW"):
    return template("<h1>Hello ${name}</h1>", name=name)

@route("/example2")
@view("example2.tpl")
def html_exampl2(name="WOW"):
    #example2.tpl contains html and mako template code like: <h1>${name}</h1>
    return {"name" : name}

@route('/hello/<name>')
def index(name):
    return template('<b>Hello Mako ${name}</b>!', name=name)

@route('/img/<filename>')
def send_static(filename):
    return static_file(filename, root='static/img')

@route('/css/<filename>')
def send_static(filename):
    return static_file(filename, root='static/css')

@route('/photos')
def display_photos():
    return template_w.render({'name': 'John'})



run(host='www.diodev.fr', port=80, reloader=True, debug=True)
