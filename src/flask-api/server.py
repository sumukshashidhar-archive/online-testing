import sys
sys.path.append('.')
import flask
from flask import request, jsonify, Flask, render_template, redirect, url_for, request


#other imports
from src.microservices.authentication import authenticate


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
            return redirect(url_for('dash', args='admin'))
    return render_template('login.html', error=error)

@app.route('/dash', methods=['GET'])
def dash():
    return render_template('teacher_dash.html', name=request.args['args'])

app.run()
