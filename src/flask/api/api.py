import sys
import flask
from flask import request, jsonify

from src.flask.api.controllers import auth

app = flask.Flask(__name__)
app.config["DEBUG"] = True
sys.path.append('.')

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/auth/login', methods=['GET'])
def login():
    if 'username' in request.args and 'password' in request.args:
        uname = str(request.args['username'])
        pwd = str(request.args['password'])
        res = auth.login(username=uname, password=pwd)
        if res['status']:
            return jsonify({})
        else:
            return jsonify({
                "status":403, 
                "message":res['message']
            })
    else:
        return jsonify({
            "status": 400, 
            "message":"Either no username or password in arguments"
        })

app.run()