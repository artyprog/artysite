import bottle
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import DictLoader
from wheezy.template.loader import FileLoader
from wheezy.template.ext.code import CodeExtension

from beaker.middleware import SessionMiddleware
import json
import crypt
import spwd
import pwd

from bottle import(
        run,
        route,
        request,
        hook,
        static_file,
        redirect,
        response,
        ServerAdapter,
        default_app
        )


class SSLCherryPyServer(ServerAdapter):
    def run(self, handler):
        from cherrypy import wsgiserver
        from cherrypy.wsgiserver.ssl_pyopenssl import pyOpenSSLAdapter
        server = wsgiserver.CherryPyWSGIServer((self.host, self.port), handler)
        server.ssl_adapter = pyOpenSSLAdapter('cacert.pem', 'privkey.pem')
        try:
            server.start()
        finally:
            server.stop()


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

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.da{a_dir': './data',
    'session.auto': True
}

#run(host='www.diodev.fr', port=8888, reloader=True, debug=False, interval=0.5)



app = default_app()
myapp = SessionMiddleware(app, session_opts)
run(app=myapp, host='www.diodev.fr', port=443, server=SSLCherryPyServer)
