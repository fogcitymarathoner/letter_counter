__author__ = 'marc'
import cherrypy
import tenjin
import json
from tenjin.helpers import *
from lib.functions import letter_counts
class Root(object):
    @cherrypy.expose
    def index(self, q=None):
        engine = tenjin.Engine(path=['views'], layout='_layout.pyhtml')
        ## context data

        if q is None or q == '':
            context = {
                'title': 'Letter Counter',
                'q': q,
                'letters': []
            }
        else:

            context = {
                'title': 'Letter Counter',
                'q': q,
                'letters': letter_counts(q)
            }
        ## render template with context data
        html = engine.render('index.pyhtml', context)
        return html

if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_port': 8084,
        'tools.proxy.on': True,
        'tools.proxy.base': 'http://fogtest.com/letter_counter',
        'tools.encode.encoding': "utf-8",
    })
    cherrypy.quickstart(Root(), '/letter_counter')