# -*- coding: utf-8 -*-
# filename: main.py
import web
from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "/root/swas.anqun.org.pem"
CherryPyWSGIServer.ssl_private_key = "/root/swas.anqun.org.key"

urls = (
    '/wx', 'Handle',
)

# class Handle(object):
#     def GET(self):
#         return "hello, this is handle view"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()