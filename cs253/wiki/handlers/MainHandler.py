import webapp2
from lib import utils
from lib.db.User import User
import logging

class MainHandler(webapp2.RequestHandler):
    
    params = {} ## params contains key-value pairs used by jinja2 templates to render all html
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    
    def render_str(self, template, **params):
        params['user'] = self.user
        return utils.render_str(template, **params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
    
    def render_json(self, d):
        json_txt = json.dumps(d)
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.write(json_txt)
    
    def set_secure_cookie(self, name, val):
        cookie_val = utils.make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))
    
    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and utils.check_secure_val(cookie_val)
    
    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))
        self.make_logged_in_header()
    
    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
    
    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
        
        if self.request.url.endswith('.json'):
            self.format = 'json'
        else:
            self.format = 'html'
            
        if self.user:
            self.make_logged_in_header()
        else:
            self.make_logged_out_header()

    def make_logged_out_header(self):
        logging.error("make_logged_out_header()")
        page = self.request.path
        history_link = '/_history' + page
        self.params['history'] = '<a href="%s">hisotry</a>' % history_link
        self.params['auth'] = '<a href="/login">login</a>|<a href="/signup">signup</a>'
        
    def make_logged_in_header(self):
        logging.error("make_logged_in_header()")
        page = self.request.path
        history_link = '/_history' + page
        self.params['edit'] = '<a href="_edit%s">edit</a>' % page
        self.params['history'] = '<a href="%s">history</a>' % history_link
        self.params['auth'] = self.user.username + '(<a href="logout">logout</a>)'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        