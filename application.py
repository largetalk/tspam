import tornado.ioloop
import tornado.web
import tornado.template
import os, sys
from json import loads as json_decode
from banned import init_banned_tree, replace_banned
from acspam import inspector


class ReplaceBannedHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.arguments = None
        content_type = self.request.headers.get("Content-Type", "")
        if content_type.startswith("application/json"):
            self.arguments = json_decode(self.request.body)

    def get(self):
        self.write(loader.load('replace.tpl').generate())

    def post(self):
        if self.arguments and 'input' in self.arguments:
            self.write(replace_banned(self.arguments['input']))
        else:
            self.write('something wrong')

class AcReplaceBannedHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.arguments = None
        content_type = self.request.headers.get("Content-Type", "")
        if content_type.startswith("application/json"):
            self.arguments = json_decode(self.request.body)

    def post(self):
        if self.arguments and 'input' in self.arguments:
            self.write(inspector.replace(self.arguments['input']))
        else:
            self.write('something wrong')


DEBUG=True
project_path = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(project_path, 'static')
template_path = os.path.join(project_path, 'templates')
loader = tornado.template.Loader(template_path)

application = tornado.web.Application([
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
    (r"/replace", ReplaceBannedHandler),
    (r"/ac_replace", AcReplaceBannedHandler),
    ], debug=DEBUG)

if __name__ == "__main__":
    init_banned_tree()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
