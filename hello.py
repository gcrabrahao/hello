#!flask/bin/python
import re
from flask import Flask, jsonify
from flask import abort

app = Flask(__name__)

def find_user(userid):
	if userid == "john1":
		return "1234"
	else:
		return ""

@app.route('/test/v1/extension/<string:userid>', methods=['GET'])
def get_extension(userid):
	if not re.search(r'^[A-Za-z0-9]{5}$',userid):
		abort(400)
	
	extension = find_user(userid)
	
	if not extension:
		abort(404)
	
	data = {
		'userid': userid,
		'extension': extension
	}
	return jsonify(data)
	
@app.route('/test/v1/version')
def get_version():
	return "1.0"

if __name__ == '__main__':
    app.run(debug=True)