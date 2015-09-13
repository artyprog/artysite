import bottle
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import DictLoader
from wheezy.template.loader import FileLoader
from wheezy.template.ext.code import CodeExtension

from bottle import(
        run,
        route,
        request,
        hook,
        static_file,
        redirect
        )


searchpath = ['./static/templates-wheezy']

engine = Engine(
    loader=FileLoader(searchpath),
    extensions=[CoreExtension(),CodeExtension()]
)

templateChild = engine.get_template('child.html')
template_famille = engine.get_template('famille.html')
template_photo = engine.get_template('photo.html')

@route("/")
def working():
    return "Site en maintenance"

@route('/img/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='static/img')

@route('/css/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='static/css')

@route('/js/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='static/js')

@route('/jsfgal/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='static/fgalery/js')

@route('/cssfgal/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='static/fgalery/css')

@route('/imgfgal/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='static/fgalery/imgs')

@route('/jsonfgal/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='static/fgalery/json')


@route('/albums/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='static/albums')  

@route('/famille')
def display_famille():
    return template_famille.render("")

@route('/photo') 
def display_photos():
    return template_photo.render("")

@route('/wheezy')
def display_wheezy():
    return templateChild.render("")

run(host='www.diodev.fr', port=8888, reloader=True, debug=True, interval=0.5)
