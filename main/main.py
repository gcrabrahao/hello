#!flask/bin/python
import os
import re
from flask import Flask, jsonify
from flask import abort
import requests
import json

name_url = os.environ.get('NAME_SVC')
extension_url = os.environ.get('EXTENSION_SVC')

app = Flask(__name__)

def get_name(userid):
    headers = {'Content-type': 'application/json'}
    response = requests.get(name_url+'/'+userid, headers=headers)    
    if response.ok:
        data = json.loads(response.content)
        return data['name']

def get_extension(userid):
    headers = {'Content-type': 'application/json'}
    response = requests.get(extension_url+'/'+userid, headers=headers)
    if response.ok:
        data = json.loads(response.content)
        return data['extension']

@app.route('/v1/main/<string:userid>', methods=['GET'])
def main(userid):
    if not re.search(r'^[A-Za-z0-9]{5}$',userid):
        abort(400)
	
    name = get_name(userid)
    extension = get_extension(userid)
	
    if not name or not extension:
        abort(404)
	
    data = {
        'userid': userid,
        'name': name,
        'extension': extension
    }
    return jsonify(data)
	
@app.route('/v1/version')
def get_version():
    return "1.0"

if __name__ == '__main__':
    app.run(debug=True)
