from init import app
from flask import jsonify


@app.route("/", methods=['GET'])
def root():
    return jsonify({"msg": "Hello world!"})
