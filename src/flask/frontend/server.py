import sys
sys.path.append('.')
import flask
from flask import request, jsonify, Flask, render_template, redirect, url_for, request

import uuid

#other imports
from src.microservices.authentication import authenticate

server_storage = {}
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return ''' <h1>Welcome</h1>'''




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if authenticate(request.form['username'], request.form['password'])!= False:
            
            return redirect(url_for('dash',token=token)
        else:
            error = 'Wrong Username / Password'

    return render_template('login.html', error=error)

app.run()
