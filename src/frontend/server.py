import flask
import requests
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Online Testing Website!"


@app.route('/internal_test', methods=['GET'])
def internal_test():
    response = requests.get('http://localhost:5000/internal')
    response = response.json()
    if response['status'] == 200:
        return "<h1>Able to connect to the API. All systems Go!"
    else:
        return "<h1>Something went wrong>"

app.run(debug=True, port=80)