# Rules of a reST API
# 1. Data is transfered key value pairs.
# Sending from JS as JSON Object - from python as dictionary
# 2. You must define routes/URL
# 3. You must define a http method. eg GET, POST, DELETE, PATCH
# 4. You must define a status code. eg 200, 201, 404, 401, 500

from flask import Flask, jsonify, request

app = Flask(__name__)

allowed_methods = ["GET", "POST", "PUT", "PATCH"]
user_list=[]

@app.route("/", methods=allowed_methods)
def home():
    method=request.method.lower()
    if method=="get":
        return jsonify({"Flask API Version":"1.0"}),200
    else:
        return jsonify({"msg":"Method not allowed"}),405


@app.route("/users", methods=allowed_methods)
def users():
    try:
        method=request.method.lower()
        if method=="get":
            return jsonify({"data" : user_list}),200
        elif method=="post":
            data=request.get_json()
            if data["name"]=="" or data["location"]=="":
                return jsonify({"msg":"name and location field required."}),403
            else:
                user_list.append(data)
                return jsonify({"msg":"successfully added user."}),201
        else:
            jsonify({"msg":"Method not allowed"}),405
    except Exception as e:
        return jsonify({"error": str(e)}),500






app.run(debug=True)