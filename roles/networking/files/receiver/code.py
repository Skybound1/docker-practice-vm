import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 200


@app.route('/flag', methods=['POST'])
def flag():
    return flask.request.values.get('flag', 'Gimme flag')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
