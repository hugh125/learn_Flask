'''
delte migrations data-dev.sqlite
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
python manage.py shell

User.query.all()
u1 = User(email='test1@test.com', username='test1', password='pwd1')
u2 = User(email='test2@test.com', username='test2', password='pwd2')
db.session.add(u1)
db.session.add(u2)
db.session.commit()
User.query.all()
python manage.py runserver

	https://github.com/miguelgrinberg/flasky/tree/8d
	u = User(username='test', email='test.test.com', password='pwd1')

'''