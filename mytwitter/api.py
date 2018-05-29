import flask

app = flask.Flask(__name__)


@app.route('/')
def shobolan():
	return flask.jsonify(
		{'message': 'Ce shobolan esti... '})


@app.route('/tweets/<user_id>')
def get_tweets(user_id):
	return flask.jsonify({
		'user_id': user_id,
		'tweets': ['chitz chitz.'],
		})
