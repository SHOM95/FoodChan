# all the imports
from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, render_template, flash
from contextlib import closing

#configuration
DATABASE = './tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


#application
app = Flask(__name__)
app.config.from_object(__name__)


#checking error is None
def render_redirect(template, url, error):
	if error == None:
		return redirect(url_for(url))
	return render_template(template, year='2016',error=error)

# check user with login and register
class User (object):

	# you must put this!!
	def __init__(self, username, password):
		self.username = username
		self.password = password

	# check login session
	def login (self, username, password):
		error = None
		u_name = g.db.execute(u"SELECT EXISTS ( SELECT username FROM accounts where username = ?)", (self.username, ) ).fetchone()    
		if u_name[0] == 0:
			error = "Your name is not exist!!"
		else :
			p_word = g.db.execute(u"SELECT password FROM accounts where username = ?", (self.username, ) ).fetchone()   
			if p_word[0] != self.password :
				error = "Your password is not correct!!"
			else :
				session['logged_in'] = True
				session['username'] = username 
				flash( str(self.username) + ' were logged in !!')
		return error

	# check new account
	def signup(self, username, password, repass, email):
		error = None
		u_name = g.db.execute(u'SELECT EXISTS (SELECT username FROM accounts WHERE username = ?)',(self.username,)).fetchone()
		p_word = g.db.execute(u'SELECT EXISTS (SELECT password FROM accounts WHERE username = ?)',(self.username,)).fetchone()
		e_mail = g.db.execute(u'SELECT EXISTS (SELECT email FROM accounts WHERE email = ?)',(email,)).fetchone()
		if self.password != repass : 
			error = 'your re-password is not correct!!'
		elif e_mail[0] != 0:
			error = 'your email is already exist!!'  
		elif u_name[0] == 0 and p_word[0] == 0 :
			flash('Account Created!!')
			g.db.execute('insert into accounts (username, password, email) values (?, ?, ?)', [username,password,email])
			g.db.commit()
		else :
			error = 'Already Exist!!'
		return error




#DB connection function 
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#initialize DB
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read())
		db.commit()

#before request connect to DB
@app.before_request
def before_request():
	g.db = connect_db()

#when the network connection is lost
@app.teardown_request
def teardown_request(exception):
	g.db.close()


"""
	from this, view part
"""

# Go to homepage 
@app.route('/', methods=['GET', 'POST'])
def home ():
	error = None    # error message
	if session.get('logged_in'):
		return redirect(url_for('show_entries'))
	else:
		if request.method == 'POST':
			name = request.form['username']
			pwss = request.form['password']
			if "" in [name,pwss]:
				error = "Empty Filed !!"
			else:
				user = User(name,pwss)
				error = user.login(name,pwss)
			return render_redirect('index.html','show_entries',error)
		else :
			return render_template('index.html', year='2016', error=error)

# show DB from entries
@app.route('/board')
def show_entries():
	cur = g.db.execute('SELECT * FROM entries')
	entries = [dict(id=row[0],title=row[1], writer=row[3]) for row in cur.fetchall()]
	return render_template('show_entries.html', year='2017', entries=entries)

@app.route('/remove/<string:title>')
def rm_entry(title):
	g.db.execute('DELETE FROM entries where title = (?) ',[title])
	g.db.commit()
	flash('Message : The post was deleted!! ')
	return redirect(url_for('show_entries'))

#add new record
@app.route('/add', methods=['POST'])
def add_entry():
	#exception
	if not session.get('logged_in'):
		abort(401)
	title_ = request.form['title']
	text_ = request.form['text']
	#check empty space
	if "" in [title_,text_] :
		flash('Your post has empty space!! One more time!!')
		return redirect(url_for('show_entries'))
	# check post title has already exist
	htitle = g.db.execute(u'SELECT EXISTS (SELECT title FROM entries WHERE title = ?)',(title_,)).fetchone()
	if htitle[0] != 0:
		flash('Your post title has already exist!! ')
		return redirect(url_for('show_entries'))
	# insert post
	g.db.execute('INSERT INTO entries (title, text, writer) values (?, ?, ?)',
			[ title_ , text_ ,session.get('username')])
	g.db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

#show your written doc
@app.route('/post/<string:title>')
def show_posts(title):
	cur = g.db.execute('SELECT * FROM entries where title = (?) ', [title])
	entries = [dict(title=row[1],writer=row[3], text=row[2]) for row in cur.fetchall()]
	return render_template('posts.html', year='2016', entries=entries)

#register part
@app.route('/register', methods=['GET','POST'])
def register():
	error = None # error message
	if session.get('logged_in'):
		return redirect(url_for('show_entries'))
	else :
		if request.method == 'POST':
			username = request.form['username']
			password = request.form['password']
			repass = request.form['password_confirm']
			email = request.form['email']

			if "" in [username, password,repass,email]:
				error = 'You have empty field'
			else :
				user = User(username,password)
				error = user.signup(username,password,repass,email)
			return render_redirect('register.html','show_entries',error)
		else :
			#error = 'One more time please!'
			return render_template('register.html', year='2016', error=error)

# Erase Login part
"""
#login part
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None    # error message
	if request.method == 'POST':
		name = request.form['username']
		pwss = request.form['password']
		if "" in [name,pwss]:
			error = "Empty Filed !!"
		else:
			user = User(name,pwss)
			error = user.login(name,pwss)
		return render_redirect('login.html','show_entries',error)
	else :
		return render_template('login.html', year='2016', error=error)
"""

#logout part
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('home'))

#run server
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 1234)


