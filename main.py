import bottle
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import DictLoader
from wheezy.template.loader import FileLoader
from wheezy.template.ext.code import CodeExtension

from bottle import(
        run,
        route,
        mako_view as view, #THIS IS SO THAT @view uses mako
        request,
        hook,
        static_file,
        redirect
        )

from bottle import mako_template as template_b #use mako template

template = """\
@require(name)
Hello, @name"""

engine_dict = Engine(
    loader=DictLoader({'x': template}),
    extensions=[CoreExtension()]
)

template_w = engine_dict.get_template('x')

searchpath = ['./static/templates-wheezy']
#searchpath = ['./views']
engine = Engine(
    loader=FileLoader(searchpath),
    extensions=[CoreExtension(),CodeExtension()]
)

templateChild = engine.get_template('child.html')
template_famille = engine.get_template('famille.html')

@route("/")
def working():
    return "Site en maintenance"

@route('/img/<filename>')
def send_static(filename):
    return static_file(filename, root='static/img')

@route('/css/<filename>')
def send_static(filename):
    return static_file(filename, root='static/css')

@route('/famille')
def display_famille():
    return template_famille.render("")

@route('/wheezy')
def display_wheezy():
    return templateChild.render("")


run(host='www.diodev.fr', port=80, reloader=True, debug=True, interval=0.5)
