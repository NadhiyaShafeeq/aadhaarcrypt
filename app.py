from flask import Flask, render_template, Response, request
import Engine
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate-token', methods=["POST", "GET"])
def generate_token():
    if request.method == "GET":
        return Response('{"error" : "post data not sent"}', mimetype="application/json")
    else:
        data = request.data
        data = data.decode('utf-8')
        print(data)
        details = {
            "name" : data[0],
            "email" : data[1]
        }
        user = Engine.User(details)
        resp = {
            "key" : user.generate_key
        }
        return Response(json.dumps(resp), mimetype="application/json")

app.run(debug=True)
