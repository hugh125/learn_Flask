# -*- coding:utf-8 -*-

from flask import Flask
import os
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

from flask_mail import Mail, Message
mail = Mail(app)

if __name__ == '__main__':
    msg = Message('test subject', sender='hugh182@qq.com', recipients=['hugh182@qq.com'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    with app.app_context():
        mail.send(msg)
