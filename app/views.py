import json
from pathlib import Path
from init import app
from flask import jsonify


@app.route("/menu", methods=['GET'])
def menu_index():
    menu_path = Path("static", "menu.json")
    with open(menu_path) as fp:
        menu = json.loads(fp.read())
        return jsonify(menu)


@app.route("/", methods=['GET'])
def root():
    return jsonify({"msg": "Hello world!"})
