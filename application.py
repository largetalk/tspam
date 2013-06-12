import tornado.ioloop
import tornado.web
import tornado.template
import os, sys
from banned import init_banned_tree, replace_banned

class ReplaceBannedHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(loader.load('replace.tpl').generate())

    def post(self):
        pass



project_path = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(project_path, 'static')
template_path = os.path.join(project_path, 'templates')
loader = tornado.template.Loader(template_path)

application = tornado.web.Application([
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
    (r"/replace", ReplaceBannedHandler),
    ])

if __name__ == "__main__":
    init_banned_tree()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
