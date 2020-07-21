from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps
app = Flask(__name__)

app.config['SECRET_KEY'] = 'pass'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token ')


@app.route('/unprotected')
def unprotected():
    return ''''''


@app.route('/protected')
def protected():
    return ''''''

@app.route('/login')
def login():
    auth = request.authorization
    if True:
        token = jwt.encode({'user':'test','exp':datetime.datetime.utcnow() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'])
        return jsonify(
            {
                'token' : token.decode('UTF-8')
            }
        )
    return make_response('Could not verify', 401, {'www-authenticate' : 'Basic Realm:"Login reqd"'})


if __name__ == '__main__':
    app.run(debug=True)