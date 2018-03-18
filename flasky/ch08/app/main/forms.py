# -*- conding:utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
app.config['SECRET_KEY'] = 'hugh_config_Key_string'

class NameForm(Form):
	name = StringField('What is you name?', validators=[Required()])
	#name = StringField('What is you name?', [validator.Required()]
	submit = SubmitField('Submit')
'''
ch4.3
@app.route('/')
def index():
	return render_template('index04.html')

ch4.4
@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	#return render_template('index04.html')
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		#form.name.data = ''
	return render_template('index04.html', form=form, name=name)

ch4.5
from flask import session, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index04.html', form=form, name=session.get('name'))
'''

from flask import Flask, render_template, session, redirect, url_for, flash
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have change your name!')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index04.html', form=form, name=session.get('name'))# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from flask_moment import Moment
moment = Moment(app)


from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
#form = Form(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required])
    submit = SubmitField('Submit')

'''
@app.route('/')
def index():
    #form = NameForm()
    return render_template('index04.html',name = "name-form")
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index04.html', form = form, name = name)