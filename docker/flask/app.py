from flask import Flask, render_template
from os import environ
import couchdb
import logging

app = Flask(__name__)

COUCHDB_URL = environ['COUCHDB_URL'] if 'COUCHDB_URL' in environ \
                                     else 'http://localhost:5984/'
DB_NAME = 'sample_db'
db_server = couchdb.Server(COUCHDB_URL)
if DB_NAME not in db_server:
    db_server.create(DB_NAME)

@app.route("/")
def hello():
    return "Hello World!\n"

@app.route("/list")
def list():
    db = db_server[DB_NAME]
    return render_template("list_data.html", docs=[db[id] for id in db])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
