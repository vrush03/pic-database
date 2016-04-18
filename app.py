from flask import Flask
import os
from flask import Flask, render_template, json, request, redirect, session
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
app.secret_key = 'ssh...Big secret!'
#MySQL configurations

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tekken5'
app.config['MYSQL_DATABASE_DB'] = 'pictureapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/', methods=['GET'])
def hello_world():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT img FROM User ")
	data = cursor.fetchone()[0]
	# print data
	return render_template('show.html',data = data)
if __name__ == '__main__':
    app.debug = True
    app.run()