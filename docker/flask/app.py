# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, flash, render_template
import couchdb
import logging
from hello import Hello

app = Flask(__name__)
app.config.from_envvar('APP_CONF')

def connect_db():
    db_server = couchdb.Server(app.config['COUCHDB_URL'])
    db_name = app.config['DB_NAME']
    if db_name not in db_server:
        db_server.create(db_name)
    return db_server[db_name]

def get_db():
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db

@app.before_request
def before_request():
    g.db = connect_db()
    
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.save(
        {'title': request.form['title'],
         'text': request.form['text']}
    )
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route("/")
def show_entries():
    db = g.db
    return render_template("show_entries.html", entries=[db[id] for id in db])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['FLASK_APP_USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['FLASK_APP_PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in %s' % Hello().say())
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
