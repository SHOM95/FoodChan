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
    return render_template('show_entries.html', entries=entries)


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

#login part
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None    # error message
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:  # Username should be in DB
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:    # Password should be in DB
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

#logout part
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))





#run server
if __name__ == '__main__':
    app.run()


