#!/usr/bin/env python
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template



class MainHandler(webapp.RequestHandler):
    
    def get(self, color):
        if not color: 
            self.redirect("/black")
        template_values = {
            'color': color,
            'url': self.request.url,
            'path': self.request.host_url
        }
        
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    
def main():
    application = webapp.WSGIApplication([('/(.*)', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
