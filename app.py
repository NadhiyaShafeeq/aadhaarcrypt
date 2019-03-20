from flask import Flask, render_template, Response, request
import Engine
import json
from flask_cors import CORS
import base64
import argparse

app = Flask(__name__)
CORS(app)

@app.route('/generate-token', methods=["POST", "GET"])
def generate_token():
    if request.method == "GET":
        return Response('{"error" : "post data not sent"}', mimetype="application/json")
    elif request.method == "POST":
        data = request.data
        data = data.decode('utf-8')
        details = {
            "name" : data[0],
            "email" : data[1]
        }
        user = Engine.User(details)
        resp = {
            "key" : user.generate_key
        }
        return Response(json.dumps(resp), mimetype="application/json")
    else:
        return Response("{\"error\" : \"request not allowed\"}", mimetype="application/json")


@app.route('/encrypt-data', methods=["POST", "GET"])
def encrypt_data():
    if request.method == "GET":
        return Response('{"error" : "post data not sent"}', mimetype="application/json")
    elif request.method == "POST":
        data = request.data
        data = data.decode('utf-8')
        data = json.loads(data)
        key = data["key"]
        print("This is key:"+key)
        details = {
            "aadhaarno" : data["aadhaarno"],
            "name" : data["name"],
            "dob" : data["dob"],
            "address" : data["address"]
        }
        card = Engine.Card(key, details)

        resp = {"encrypted_text" : card.encrypt_data}
        return Response(json.dumps(resp), mimetype="application/json")
    else:
        return Response("{\"error\" : \"request not allowed\"}", mimetype="application/json")

@app.route('/decrypt-data', methods=["POST", "GET"])
def decrypt_data():
    if request.method == "GET":
        return Response('{"error" : "post data not sent"}', mimetype="application/json")
    elif request.method == "POST":
        data = request.data
        data = data.decode('utf-8')
        data = json.loads(data)
        key = data["key"]

        card = Engine.Card(key)
        print(key)
        resp = {"decrypted_text" : card.decrypt_data(key, data["data"])}
        return Response(json.dumps(resp), mimetype="application/json")
    else:
        return Response("{\"error\" : \"request not allowed\"}", mimetype="application/json")

app.run(debug=True)
