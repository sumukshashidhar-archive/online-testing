# MODULE LEVEL IMPORTS
import sys
import flask
from flask import request, jsonify


# FILE MODULE IMPORTS
from src.flask.api.controllers.route_guard import protect

from src.flask.api.controllers import auth


# CONFIGURATIONS
app = flask.Flask(__name__)
app.config["DEBUG"] = True
sys.path.append('.')


# GLOBAL VAR DECLARATIONS

# list of unique sessions
sessions = []

# each session, mapped to its time
mapper = {

}

# ROUTES

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
    if protect(sessions, request):
        return jsonify({'status':200})
    else:
        return jsonify({'status': 403})


@app.route('/api/v1/deatuh')
def destroy_token():
    pass


app.run()
