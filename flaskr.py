# all the imports
from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, render_template, flash
from contextlib import closing

#configuration
DATABASE = '/tmp/flaskr.db'
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
                flash( str(self.username) + ' were logged in !!')
        return error

    # check new account
    def signup(self, username, password):
        error = None
        u_name = g.db.execute(u'SELECT EXISTS (SELECT username FROM accounts WHERE username = ?)',(username,)).fetchone()
        p_word = g.db.execute(u'SELECT EXISTS (SELECT password FROM accounts WHERE username = ?)',(password,)).fetchone()
        if u_name[0] == 0 and p_word[0] == 0 :
            flash('Account Created!!')
            g.db.execute('insert into accounts (username, password) values (?, ?)', [username,password])
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
#show DB
@app.route('/')
def show_entries():
    cur = g.db.execute('SELECT title, text FROM entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', year='2016', entries=entries)


#add new record
@app.route('/add', methods=['POST'])
def add_entry():
    #exception
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('INSERT INTO entries (title, text) values (?, ?)',
            [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

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

            if "" in [username, password]:
                error = 'You have empty field'
            else :
                user = User(username,password)
                error = user.signup(username,password)
            return render_redirect('register.html','show_entries',error)
        else :
            #error = 'One more time please!'
            return render_template('register.html', year='2016', error=error)


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

#logout part
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


#run server
if __name__ == '__main__':
    app.run()


