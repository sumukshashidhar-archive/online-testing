import sys
import flask
from flask import request, jsonify
from src.flask.api.controllers.implementations.binary_search import binary_search as bs
from src.flask.api.controllers import auth

app = flask.Flask(__name__)
app.config["DEBUG"] = True
sys.path.append('.')

#list of unique sessions
sessions = ['abcdefg', 'xyz123']
# sessions = []

#each session, mapped to its time
mapper = {
    'abcdefg':{
        'username':'Mr Abc',
        'school':'SKPS'
    },
    'xyz123':{
        'username':'Mr Xyz',
        'school':'DPS'
    }
}
mapper = {

}

def protect(request):
    # we check if the token exists at first, then we go ahead and we extract the session data
    if 'token' in request.args:
        res = bs(sessions, request.args['token'])
        if res != -1:
            return True
        else:
            return False
    else:
        return False


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/retrieve/test')
def get_test():
    '''
    Retrieves a test link for a given id
    :return: string
    '''
    if protect(request):
        return jsonify({'status':200})
    else:
        return jsonify({'status': 403})


@app.route('/api/v1/deatuh')
def destroy_token():
    pass


app.run()
