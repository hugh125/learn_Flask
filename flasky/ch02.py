# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
app = Flask(__name__)

'''
@app.route('/')
def index():
    return 'Hello, Flask!'
'''
@app.route('/')
def index():
    return '<h1>Bad Request</h1>'#, 400
    user_agent = request.heder.get('User-Agent')
    return '<p>Your brower is %s</p>'% user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' %name



if __name__ == '__main__':
    app.run(debug=True)
# -*- coding: utf-8 -*-

#from 02ch_2_2_hello import app
from flask import Flask
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!')
    response.set_cookie('answer', '42')
    return response

from flask import redirect
@app.route('/redirect')
def my_redirect():
    return redirect("http://www.example.com")

from flask import abort
@app.route('/user/<id>')
def get_user(id):
    user = ""#load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello,%s</h1>' %user.name

#from flask.ext.script import Manage

if __name__ == '__main__':
    app.run(debug=True)

