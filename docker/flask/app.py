from flask import Flask
from os import environ
import couchdb

app = Flask(__name__)

COUCHDB_URL = environ['COUCHDB_URL'] if 'COUCHDB_URL' in environ \
                                     else 'http://localhost:5984/'
server = couchdb.Server(COUCHDB_URL)

DB_NAME = 'sample_db'
if DB_NAME not in server:
    server.create(DB_NAME)

@app.route("/")
def hello():
    body = ""
    db = server[DB_NAME]
    for id in db:
        body += "document %s\n" % id
    return "Hello World!\n" + body

if __name__ == "__main__":
    app.run(host='0.0.0.0')
