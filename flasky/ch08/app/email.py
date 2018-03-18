# -*- coding:utf-8 -*-

from flask import Flask, render_template
from threading import Thread
import os
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

from flask_mail import Mail, Message
mail = Mail(app)

def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(to, subject, template, **kwargs):
	pass
	# msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
	# msg.vody = render_template(template + '.txt', **kwargs)
	# msg.html = render_template(template + '.html', **kwargs)
	# thr = Thread(target=send_async_email, args=[app, msg])
	# thr.start()
	# return thr
