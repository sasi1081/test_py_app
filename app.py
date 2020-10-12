from flask import Flask,request,jsonify
import os
import json
import subprocess
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/' ,  methods=['GET'])
def home():
    return "<h1>Hello , Greetings from Sasi!</p>"

@app.route('/version', methods=['GET'])

def ver():
    process = subprocess.Popen(['git', 'rev-parse', 'HEAD'], shell=False, stdout=subprocess.PIPE)
    # jsonS = json.dumps(process.communicate()[0].strip())
    git_head_hash = process.communicate()[0].strip()
    git = git_head_hash.decode()
    app_version = "v1"
    message = "Practice Test"
    return jsonify({'SHA':git , 'app_version':app_version , 'Description': message})

if __name__ == "__main__":
    app.run(host='127.0.0.1')
