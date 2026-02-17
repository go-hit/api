# Rules of a reST API
# 1. Data is transfered key value pairs.
# Sending from JS as JSON Object - from python as dictionary
# 2. You must define routes/URL
# 3. You must define a http method. eg GET, POST, DELETE, PATCH
# 4. You must define a status code. eg 200, 201, 404, 401, 500

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Flask API Version":"1.0"}),200

app.run()