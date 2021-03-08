import models
from init import app
from flask import jsonify


@app.route("/menu", methods=['GET'])
def menu_index():
    categories = models.Category.all()
    products = models.Product.all()
    return jsonify({"categories": categories, "products": products})


@app.route("/", methods=['GET'])
def root():
    return jsonify({"msg": "Hello world!"})
