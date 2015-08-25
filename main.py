import bottle

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


@route("/")
@view("mainpage.tpl")
def main_page():
    return 

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


@route('/css/<filename>')
def send_static(filename):
    return static_file(filename, root='static/css')


run(host='diodev.fr', port=8088, debug=True)
