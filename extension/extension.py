#!flask/bin/python
import re
from flask import Flask, jsonify
from flask import abort
from models import User

app = Flask(__name__)

def get_extension(userid):
	u = User.query.filter(User.userid == userid).first()
	if u:
		return u.extension
	else:
		return ""

@app.route('/v1/extension/<string:userid>', methods=['GET'])
def main(userid):
	if not re.search(r'^[A-Za-z0-9]{5}$',userid):
		abort(400)
	
	extension = get_extension(userid)
	
	if not extension:
		abort(404)
	
	data = {
		'userid': userid,
		'extension': extension
	}
	return jsonify(data)
	
@app.route('/v1/version')
def get_version():
	return "1.0"

if __name__ == '__main__':
    app.run(debug=True)
